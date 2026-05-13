# Dashboard Architecture

## File Structure & Responsibilities

### Core Application Files

**`app.py`** - Main entry point
- Initializes Dash application
- Combines layout + callbacks
- Run: `python app.py`

**`tasks.py`** - Add invoke commands, especially useful for long command line inputs

**`config.py`** - Configuration & constants
- Data file paths
- Column mappings
- App settings (title, debug mode, etc.)

**`layout.py`** - UI structure
- Defines dashboard layout (navbar, sidebar, main content)
- All visual components (dropdowns, charts, map containers)

**`callbacks.py`** - Interactivity logic
- Handles user interactions (filters, clicks, updates)
- Connects UI components to data updates

### Data & Processing

**`utils/data_loader.py`** - Data loading
- Ridley dataset
- Cleans column names
- Exports: `df_grossi`, `df`

### Visualizations

**`visualizations/charts.py`** - Chart creation
- Functions to create Plotly charts
- Reusable visualization components

**`sections/overview.py`** - Overview section layout
**`sections/data_section.py`** - Data table section layout

```mermaid
sequenceDiagram
    actor U as User
    participant T as tasks.py
    participant A as app.py
    participant L as /layout
    participant B as Browser
    participant Ut as /utils
    participant SQL as /database
    participant C as /callbacks

    U->>T: invoke start
    T->>A: python app.py
    A-->>L: create_layout()
    L -->>Ut: df, get_threat_categories, bib_table, extract_threat_category_from_code, get_threat_categories
    Ut -->> SQL: SELECT * FROM processed;
    SQL -->> Ut: Return processed SQL table
    Ut -->>L: processed pandas dataframe, threat categories, article table data
    L -->>A: Dashboard layout
    A -->>B: app.run(debug=DEBUG_MODE, host="0.0.0.0", port=8768)
    B -->>A: Update Dashboard
    A -->>C: register_callbacks(app)
    C -->>L: update Dashboard layout
    L -->>C: Updated data
    C -->>B: Updated data
    
```

## Quick Start
(Recommended way using python virtual environment in Readme,md)
1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `python app.py`
3. Open browser: [http://127.0.0.1:8058](http://10.112.29.170:8768)

## Development Guidelines

- **Add new settings** → `config.py`
- **Add new data processing** → `utils/`
- **Add new charts** → `visualizations/charts.py`
- **Add new filters/interactions** → `callbacks.py`
- **Modify UI/layout** → `layout.py` or `sections/`
