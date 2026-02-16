# Configuration file for dashboard settings
# Define data paths, constants, and application settings here

import os

# Data paths
DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')
GROSSI_CSV = os.path.join(DATA_DIR, 'Grossi_et_al_Piloted_data_extraction_strategy.csv')
RIDLEY_CSV = os.path.join(DATA_DIR, 'Ridley_et_al_13750_2022_279_MOESM4_ESM.csv')

# Key columns for Grossi dataset
GROSSI_COLUMNS = {
    'location': ['Continent_Ocean', 'Country'],
    'threats': ['Threat', 'Threat_metric', 'Threat_data'],
    'taxonomy': ['Plant_group', 'Animal_group'],
    'ecology': ['Ecological_level', 'Ecoregion', 'Spatial_Scale'],
    'study': ['Study_design', 'Authors', 'Article_ID'],
    'drivers': ['Direct_driver', 'Indirect_driver']
}

# Filter options (will populate from data)
FILTER_DEFAULTS = {
    'continent': 'All',
    'threat': 'All',
    'study_design': 'All',
    'ecological_level': 'All'
}

# App settings
APP_TITLE = "Biodiversity Threats Evidence Map"
DEBUG_MODE = True


