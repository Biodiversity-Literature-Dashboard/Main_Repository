import unittest

from utils.logic.filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter
from utils.data_loader import df_ridley

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.shape = (1069, 19)

    def test_continent_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = continent_filter(df_ridley, 'all').shape
        self.assertEqual(df_shape, self.shape)

    def test_ecoregion_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = ecoregion_filter(df_ridley, ['Terrestrial', 'Marine', 'Freshwater']).shape
        self.assertEqual(df_shape, self.shape)

    def test_study_design_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = study_design_filter(df_ridley, ['Observational', 'Experimental','S_Review']).shape
        self.assertEqual(df_shape, self.shape)

    def test_threat_category_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = threat_category_filter(df_ridley, 'all').shape
        self.assertEqual(df_shape, self.shape)
