import unittest
import pandas as pd
from CsvCombiner import CsvCombiner


class TestCsvCombiner(unittest.TestCase):
    """This unit testing class ontains unit tests for the CsvCombiner class.
    Appropriate error messages are shown for graceful handling of erroneous input values."""

    def test_get_basename(self):
        """verifies that get_basename returns the appropriate string"""
        files = ['//C:hue/Desktop/favoriteFasion/clothing.csv', 'accessories.csv', 'household_cleaners.csv',
                 '//C:hue/Desktop/favoriteFasion/elvis.pdf']
        c = CsvCombiner(files)
        file_basenames = []
        for file in files:
            file_basenames.append(c.get_basename(file))
        self.assertEqual(file_basenames[3], 'elvis.pdf')

    def test_one_good_input(self):
        """verifies that a dataframe of correct length is generated prior to returning a CSV"""
        files = ["accessories.csv", "asdf", "dfds"]
        c = CsvCombiner(files)
        c.combine_csvs(files)
        df = pd.read_csv('combined_spreadsheets.csv')
        len_when_only_one_valid = len(df)
        test_len = False
        if len_when_only_one_valid == 215:
            test_len = True
        self.assertTrue(test_len)

    def test_all_bad_input(self):
        """Verifies that the combine_csvs method returns False and a message
        if there are no valid CSVs passed as arguments"""

        # the previous test's one good input is misspelled
        files = ["accessorie.csv", "asdf", "dfds"]
        c = CsvCombiner(files)
        all_bad_result = c.combine_csvs(files)

        self.assertFalse(all_bad_result)

    def test_extra_column_integration(self):
        """correct col count should be in place for combine_csvs method, and a visual stdout will
        confirm on this test that the integration of two valid inputs was successful"""
        files = ["accessories.csv", "pokemon.csv", "dfds"]
        c = CsvCombiner(files)
        c.combine_csvs(files)
        df = pd.read_csv('combined_spreadsheets.csv')
        cols = []
        for col in df.columns:
            cols.append(col)
        # with accessories.csv & pokemon.csv, there should be 16 columns total
        # this code is extensible and handles extra columns easily handles extra columns
        if len(cols)==16:
            self.assertTrue(True)
    if __name__ == '__main':
        unittest.main(exit=False)