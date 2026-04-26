# Visualization and chart creation functions
# Functions to create various chart types using Plotly (bar charts, line charts, pie charts, etc.)

#pre-made packages
import io
import base64
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
from wordcloud import WordCloud

# local imports
#from sections.dataframes import top_10_authors
from utils.data_loader import extract_threat_category_from_code, get_threat_categories
from utils.dataframes import bib_table



# EMPTY CHARTS



def create_empty_chart(title):
    """Create an empty chart placeholder"""
    fig = go.Figure()
    fig.update_layout(
        title=title,
        height=300,
        annotations=[{
            'text': 'No data to display',
            'xref': 'paper',
            'yref': 'paper',
            'showarrow': False,
            'font': {'size': 14, 'color': 'gray'}
        }]
    )
    return fig


def create_empty_chart_column(ind, title, width=6):
    chart_col = dbc.Col([
        dcc.Graph(
            id=ind,
            figure=create_empty_chart(title),
            config={'displayModeBar': False}
        )
    ], width=width)
    return chart_col

# BAR CHARTS

def create_threat_distribution_chart(df):
    """
    Create bar chart showing distribution of threat categories.
    Counts all threats (articles can have multiple).
    """
    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            height=400,
            annotations=[{
                'text': 'No data matches filters',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 14, 'color': 'gray'}
            }]
        )
        return fig
    
    # If dataset has no Threat column, return empty chart
    if 'Threat' not in df.columns:
        return create_empty_chart("Threat Category Distribution")

    # Extract all threat categories from all articles
    all_threats = []
    for threat_code in df['Threat'].dropna():
        categories = extract_threat_category_from_code(threat_code)
        all_threats.extend(categories)
    
    # Count occurrences
    threat_counts = pd.Series(all_threats).value_counts().reset_index()
    threat_counts.columns = ['Category', 'Count']
    
    # Add numbered labels and full names
    threat_cat_dict = dict(get_threat_categories())
    threat_counts['Name'] = threat_counts['Category'].map(
        lambda x: threat_cat_dict.get(x, 'Unknown')
    )
    threat_counts['Num'] = [str(i + 1) for i in range(len(threat_counts))]

    # Build legend text for annotation
    legend_text = '<br>'.join(
        f"{row['Num']}. {row['Name']}" for _, row in threat_counts.iterrows()
    )

    fig = px.bar(
        threat_counts,
        x='Num',
        y='Count',
        labels={'Num': 'Category #', 'Count': 'Number of Articles'}
    )

    fig.add_annotation(
        text=legend_text,
        xref='paper', yref='paper',
        x=1.02, y=1.0,
        showarrow=False,
        align='left',
        font=dict(size=9),
        xanchor='left',
        yanchor='top'
    )

    fig.update_layout(
        height=400,
        margin=dict(r=230),
        showlegend=False
    )

    return fig

# PIE CHARTS
def create_study_design_chart(df):
    """
    Create pie chart showing distribution of study designs.
    """
    if df.empty:
        fig = go.Figure()
        fig.update_layout(
            height=400,
            annotations=[{
                'text': 'No data matches filters',
                'xref': 'paper',
                'yref': 'paper',
                'x': 0.5,
                'y': 0.5,
                'showarrow': False,
                'font': {'size': 14, 'color': 'gray'}
            }]
        )
        return fig

    design_counts = df['Study_design'].value_counts().reset_index()
    design_counts.columns = ['Design', 'Count']
    # Rename S_Review for display
    design_counts['Design'] = design_counts['Design'].replace({'S_Review': 'Systematic Review'})

    fig = px.pie(
        design_counts,
        values='Count',
        names='Design',
        hole=0.3  # Donut chart
    )

    fig.update_layout(height=400)

    return fig


# WORDCLOUD


def create_wordcloud_chart(filtered_df=None):
    """Generate a wordcloud from article titles."""

    if filtered_df is None or filtered_df.empty:
        titles = ' '.join(bib_table['Title'].dropna().astype(str).tolist())
    else:
        titles = ' '.join(filtered_df['Title'].dropna().astype(str).tolist())

    fig = go.Figure()

    if not titles.strip():
        fig.update_layout(
            height=400,
            margin=dict(l=0, r=0, t=0, b=0),
            xaxis=dict(visible=False, range=[0, 1]),
            yaxis=dict(visible=False, range=[0, 1])
        )
        return fig

    try:
        wc = WordCloud(width=800, height=360, background_color='white').generate(titles)

        buf = io.BytesIO()
        wc.to_image().save(buf, format='PNG')
        buf.seek(0)
        img_b64 = base64.b64encode(buf.read()).decode()

        fig.add_layout_image(dict(
            source=f'data:image/png;base64,{img_b64}',
            xref='paper', yref='paper',
            x=0, y=1, sizex=1, sizey=1,
            sizing='stretch', layer='below'
        ))
    except BaseException:
        pass

    fig.update_layout(
        height=400,
        margin=dict(l=0, r=0, t=0, b=0),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1])
    )
    return fig


# SANKEY DIAGRAM

def create_driver_sankey(df, df_threats):
    """
    Create Sankey diagram: Indirect Driver → Direct Driver → Threat.
    df         : filtered articles DataFrame (must have Direct_driver_clean, Indirect_driver_clean)
    df_threats : full Threats_Clean DataFrame (ArticleID, Threat1_decoded)
    """
    if df.empty:
        return create_empty_chart("Driver Causal Chain (Sankey)")

    # Filter threats to articles in filtered df
    article_ids = df['ArticleID'].astype(str).unique()
    threats_filtered = df_threats[df_threats['ArticleID'].astype(str).isin(article_ids)]

    # Aggregate Threat1_decoded per article
    df_threats_agg = (
        threats_filtered.groupby('ArticleID', as_index=False)
        .agg({'Threat1_decoded': lambda x: '; '.join(sorted(set(x.dropna().astype(str))))})
    )
    df_threats_agg['ArticleID'] = df_threats_agg['ArticleID'].astype(str)

    df_work = df.copy()
    df_work['ArticleID'] = df_work['ArticleID'].astype(str)
    df_work = df_work.merge(df_threats_agg, on='ArticleID', how='left')

    # Build edge list
    sankey_rows = []
    for _, row in df_work.iterrows():
        # deduplicate within each article's driver/threat list
        indirects = list(dict.fromkeys(
            i.strip() for i in str(row.get('Indirect_driver', '')).split(';')
            if i.strip() and i.strip().lower() not in ('unknown', 'nan', 'none', '')
        ))
        directs = list(dict.fromkeys(
            d.strip() for d in str(row.get('Direct_driver', '')).split(';')
            if d.strip() and d.strip().lower() not in ('unknown', 'nan', 'none', '')
        ))
        threats = list(dict.fromkeys(
            t.strip() for t in str(row.get('Threat1_decoded', '')).split(';')
            if t.strip() and t.strip().lower() not in ('unknown', 'nan', 'none', '')
        ))
        for ind in indirects:
            for dir_ in directs:
                sankey_rows.append({'source': f'IND: {ind}', 'target': f'DIR: {dir_}'})
        for dir_ in directs:
            for thr in threats:
                sankey_rows.append({'source': f'DIR: {dir_}', 'target': f'THR: {thr}'})

    if not sankey_rows:
        return create_empty_chart("Driver Causal Chain (Sankey)")

    df_sankey = (
        pd.DataFrame(sankey_rows)
        .groupby(['source', 'target'])
        .size()
        .reset_index(name='value')
    )

    all_nodes  = list(dict.fromkeys(df_sankey['source'].tolist() + df_sankey['target'].tolist()))
    node_idx   = {n: i for i, n in enumerate(all_nodes)}

    def node_color(label):
        if label.startswith('IND:'): return 'rgba(255, 160, 86, 0.85)'
        if label.startswith('DIR:'): return 'rgba(70, 145, 210, 0.85)'
        return 'rgba(100, 180, 120, 0.85)'

    node_colors = [node_color(n) for n in all_nodes]
    node_labels = [n.split(':', 1)[1] for n in all_nodes]

    fig = go.Figure(go.Sankey(
        arrangement='snap',
        node=dict(
            pad=18, thickness=20,
            line=dict(color='white', width=0.5),
            label=node_labels,
            color=node_colors,
        ),
        link=dict(
            source=[node_idx[s] for s in df_sankey['source']],
            target=[node_idx[t] for t in df_sankey['target']],
            value=df_sankey['value'].tolist(),
            color='rgba(180, 180, 180, 0.3)',
        ),
    ))

    fig.update_layout(
        height=620,
        margin=dict(t=60, b=20, l=10, r=10),
        font=dict(size=11),
        annotations=[
            dict(x=0.01, y=1.06, xref='paper', yref='paper',
                 text='<b>Indirect Drivers</b>', showarrow=False,
                 font=dict(color='rgba(255,140,40,1)', size=12)),
            dict(x=0.50, y=1.06, xref='paper', yref='paper',
                 text='<b>Direct Drivers</b>', showarrow=False,
                 font=dict(color='rgba(50,120,200,1)', size=12)),
            dict(x=0.99, y=1.06, xref='paper', yref='paper',
                 text='<b>Threats</b>', showarrow=False,
                 font=dict(color='rgba(60,150,80,1)', size=12)),
        ],
    )
    return fig
