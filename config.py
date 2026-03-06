# Configuration file for dashboard settings
# Define data paths, constants, and application settings here

import os

# Data paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
PROCESSED_DIR = os.path.join(DATA_DIR, 'processed')
GROSSI_CSV = os.path.join(PROCESSED_DIR, 'grossi_included_clean.csv')
RIDLEY_CSV = os.path.join(PROCESSED_DIR, 'ridley_articles_dashboard.csv')
RIDLEY_BIB = os.path.join(DATA_DIR,'Ridley_bibliography.csv')

# Key columns for Grossi processed dataset
GROSSI_COLUMNS = {
    'location': ['Continent_Ocean', 'Country'],
    'threats': ['Threat', 'Threat_metric', 'Threat_data', 'Quantity_threats', 'Threat_precision', 'Threat_database'],
    'study': ['Study_design', 'Authors', 'Article_ID'],
    'ecology': ['Ecoregion']
}

# Filter options (will populate from data)
FILTER_DEFAULTS = {
    'continent': 'All',
    'threat': 'All',
    'study_design': 'All',
    'ecological_level': 'All'
}

# Load threat code mappings from JSON
import json
THREAT_CODES_JSON = os.path.join(PROCESSED_DIR, 'threat_codes.json')
with open(THREAT_CODES_JSON, 'r', encoding='utf-8') as f:
    _threat_data = json.load(f)
    THREAT_CODES = _threat_data['threat_codes']
    THREAT_CATEGORIES = _threat_data['threat_categories']

# App settings
APP_TITLE = "Biodiversity Interactive Dashboard"
DEBUG_MODE = True


