# Visualization and chart creation functions
# Functions to create various chart types using Plotly (bar charts, line charts, pie charts, etc.)

#pre-made packages
from dash import dcc
import plotly.express as px
import plotly.graph_objects as go
import dash_bootstrap_components as dbc
import pandas as pd
import io
import base64
from wordcloud import WordCloud

# local imports
#from sections.dataframes import top_10_authors
from utils.data_loader import extract_threat_category_from_code, get_threat_categories
from sections.dataframes import ridley_bib_table



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


def create_empty_chart_column(id, title, width=6):
    chart_col = dbc.Col([
        dcc.Graph(
            id=id,
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
            title="Threat Category Distribution",
            height=300,
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
        title='Threat Category Distribution',
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
        height=300,
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
            title="Study Design Distribution",
            height=300,
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
    
    fig = px.pie(
        design_counts,
        values='Count',
        names='Design',
        title='Study Design Distribution',
        hole=0.3  # Donut chart
    )
    
    fig.update_layout(height=300)
    
    return fig


# WORDCLOUD


def create_wordcloud_chart():
    """Generate a wordcloud from Ridley bibliography article titles."""

    titles = ' '.join(ridley_bib_table['Title'].dropna().tolist())
    wc = WordCloud(width=500, height=260, background_color='white').generate(titles)

    buf = io.BytesIO()
    wc.to_image().save(buf, format='PNG')
    buf.seek(0)
    img_b64 = base64.b64encode(buf.read()).decode()

    fig = go.Figure()
    fig.add_layout_image(dict(
        source=f'data:image/png;base64,{img_b64}',
        xref='paper', yref='paper',
        x=0, y=1, sizex=1, sizey=1,
        sizing='stretch', layer='below'
    ))
    fig.update_layout(
        title='Article Keywords Wordcloud',
        height=300,
        margin=dict(l=0, r=0, t=40, b=0),
        xaxis=dict(visible=False, range=[0, 1]),
        yaxis=dict(visible=False, range=[0, 1])
    )
    return fig
