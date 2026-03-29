# Dashboard Architecture

## File Structure & Responsibilities

### Core Application Files

**`app.py`** - Main entry point
- Initializes Dash application
- Combines layout + callbacks
- Run: `python app.py`

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
- Loads Grossi and Ridley datasets
- Cleans column names
- Exports: `df_grossi`, `df`

**`sections/dataframes.py`** - Data transformations
- Processes data for visualizations
- Aggregation and filtering functions

### Visualizations

**`visualizations/charts.py`** - Chart creation
- Functions to create Plotly charts
- Reusable visualization components

**`sections/overview.py`** - Overview section layout
**`sections/data_section.py`** - Data table section layout

## Data Flow

```
User starts app
  ↓
config.py → loads paths
  ↓
data_loader.py → loads CSV files into DataFrames
  ↓
layout.py → builds UI components
  ↓
callbacks.py → adds interactivity
  ↓
app.py → combines everything and runs server
  ↓
User interacts with filters
  ↓
callbacks.py → processes filter
  ↓
dataframes.py → transforms data
  ↓
charts.py → updates visualizations
  ↓
layout.py → displays updated UI
```

## Quick Start

1. Install dependencies: `pip install -r requirements.txt`
2. Run app: `python app.py`
3. Open browser: `http://127.0.0.1:8050`

## Development Guidelines

- **Add new settings** → `config.py`
- **Add new data processing** → `utils/` or `sections/dataframes.py`
- **Add new charts** → `visualizations/charts.py`
- **Add new filters/interactions** → `callbacks.py`
- **Modify UI/layout** → `layout.py` or `sections/`
