import unittest

from utils.logic.filters import continent_filter, ecoregion_filter, study_design_filter, threat_category_filter, column_exists
from utils.data_loader import df

class TestFilters(unittest.TestCase):
    def setUp(self):
        self.shape = (1069, 25)

    def test_continent_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = continent_filter(df, 'all').shape
        self.assertEqual(df_shape, self.shape)

    def test_ecoregion_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = ecoregion_filter(df, ['Terrestrial', 'Marine', 'Freshwater']).shape
        self.assertEqual(df_shape, self.shape)

    def test_study_design_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = study_design_filter(df, ['Observational', 'Experimental','S_Review']).shape
        self.assertEqual(df_shape, self.shape)

    def test_threat_category_filter_returns_correct_amount_of_rows_and_columns(self):
        df_shape = threat_category_filter(df, 'all').shape
        self.assertEqual(df_shape, self.shape)

    def test_use_continent_filter_africa(self):
        df_shape = continent_filter(df, 'africa').shape
        self.assertEqual(df_shape, df[df['Continent_Ocean'].str.contains("africa",case=False)].shape)

    def test_use_continent_filter_none(self):
        df_shape = continent_filter(df, 'all').shape
        self.assertEqual(df_shape, self.shape)

    def test_use_ecoregion_filter_marine(self):
        df_shape = ecoregion_filter(df, ['Marine']).shape
        self.assertEqual(df_shape, df[df['Ecoregion'].str.contains("Marine",case=False)].shape)

    def test_use_ecoregion_filter_terrestial_freshwater(self):
        df_shape = ecoregion_filter(df, ['Terrestrial','Freshwater']).shape
        self.assertEqual(df_shape, df[df['Ecoregion'].str.contains('Terrestrial',case=False) | df['Ecoregion'].str.contains('Freshwater',case=False)].shape)

    def test_use_ecoregion_filter_none(self):
        df_shape = ecoregion_filter(df,None).shape
        self.assertEqual(df_shape, self.shape)

    def test_use_study_design_filter_experimental_s_review(self):
        df_shape = study_design_filter(df, ['Experimental','S_Review']).shape
        self.assertEqual(df_shape, df[df['Study_design'].isin(['Experimental','S_Review']) ].shape)

    def test_use_study_design_filter_empty(self):
        df_shape = study_design_filter(df,[]).shape
        self.assertEqual(df_shape,self.shape)

    def test_use_threat_category_filter_eight(self):
        self.shape = threat_category_filter(df,8)
        

    def test_column_exists_ecoregion(self):
        self.assertEqual(column_exists(df,'Ecoregion'), True)

    def test_column_exists_courses(self):
        self.assertEqual(column_exists(df,'Course'), False)

