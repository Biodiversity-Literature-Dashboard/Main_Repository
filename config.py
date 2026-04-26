# Configuration file for dashboard settings
# Define data paths, constants, and application settings here

import os
import json

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
THREAT_CODES_JSON = os.path.join(PROCESSED_DIR, 'threat_codes.json')
with open(THREAT_CODES_JSON, 'r', encoding='utf-8') as f:
    _threat_data = json.load(f)
    THREAT_CODES = _threat_data['threat_codes']
    THREAT_CATEGORIES = _threat_data['threat_categories']

# App settings
APP_TITLE = "Biodiversity Interactive Dashboard"
DEBUG_MODE = True

# Wordcloud settings — modify these to customise the word cloud without touching chart code
WORDCLOUD_MAX_WORDS = 80
WORDCLOUD_COLORMAP = 'viridis'   # any matplotlib colormap name, e.g. 'Blues', 'plasma', 'magma'
WORDCLOUD_STOPWORDS = {
    # Generic academic words
    'study', 'studies', 'using', 'based', 'analysis', 'data', 'results',
    'effect', 'effects', 'impact', 'impacts', 'new', 'also', 'one', 'two',
    'three', 'across', 'within', 'among', 'due', 'associated', 'used',
    'review', 'systematic', 'evidence', 'literature', 'paper', 'research',
    'different', 'high', 'low', 'large', 'small', 'use', 'show', 'shows',
    # Domain-generic (too common to be informative)
    'marine', 'terrestrial', 'freshwater', 'environmental', 'biodiversity',
    'species', 'population', 'habitat', 'area', 'global', 'local',
    'change', 'changes', 'management', 'conservation',
}
# Text columns available for wordcloud source — add new columns here if dataset grows
WORDCLOUD_SOURCE_COLS = {
    'Title': 'Article Titles',
    'Direct_driver': 'Direct Drivers',
    'Indirect_driver': 'Indirect Drivers',
    'Threat': 'Threats',
}
