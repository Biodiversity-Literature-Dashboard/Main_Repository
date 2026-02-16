# Interactive Dashboard for Indirect Threats to Biodiversity Literature

## Project Info

- **Client:** Helsinki Lab of Interdisciplinary Conservation Science
- **Contact:** Federico Grossi, federico.grossi@helsinki.fi
- **Framework:** Plotly Dash (Python)
- **Reference:** https://naturalandenvironmentalscience.shinyapps.io/ThreatMapping_SM/

## Objective

Build an interactive dashboard to visualize and explore systematic literature on indirect threats to biodiversity. Enable expert users to filter, analyze, and interpret scientific evidence from reviewed articles.

## Datasets

### 1. Grossi et al. - Piloted Data Extraction Strategy
- 15 articles (training dataset)
- 27 columns including: threats, taxonomic groups, ecological levels, spatial scale, study design
- Contains extracted text fields (indirect drivers, spatial scale sources)
- Keywords already extracted and saved in Excel sheets (Bibliography, Typologies, Extended definitions)
- **Status:** Ready for dashboard development

### 2. Ridley et al. - 13750_2022_279_MOESM4_ESM
- CSV format
- **Status:** Needs exploration and integration

## Scope

**Current Scale:** ~20 articles  
**Target Scale:** 250-500 articles, 25+ data categories

## Core Features

1. Interactive global map (geographic distribution)
2. Filter controls (location, threats, study type, ecological level)
3. Statistical visualizations (threat types, study designs, ecological levels)
4. Data table view with filtering
5. Text analysis (word clouds, keyword frequencies, co-occurrence networks)

## Technical Stack

- Python 3.13
- Plotly Dash 4.0.0
- Pandas for data processing
- Plotly for visualizations
- Excel/CSV data sources

## Success Criteria

- Scalable architecture for 250-500 articles
- Effective filtering and exploration
- Insightful visualizations revealing patterns
- User-friendly interface for researchers
