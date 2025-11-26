# ---------------------------------------------------------------------
# IMPORTED FUNCTIONS USED IN PROGRAM
# ---------------------------------------------------------------------

import unittest
from unittest.mock import Mock, MagicMock, patch
from mainCode import *
import pytest
import os

# ---------------------------------------------------------------------
# Class of unit tests
# ---------------------------------------------------------------------
class my_unit_tests(unittest.TestCase):

    # ---------------------------------------------------------------------
    # File handling unit tests
    # ---------------------------------------------------------------------

    # Tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('usData.csv'))

    # ---------------------------------------------------------------------
    # TESTING: read_election_data()
    # ---------------------------------------------------------------------

    # Tests if the df file has the correct columns
    def test_df_headings(self):
        self.assertEqual(list(election_df), ['state', 'candidate', 'fraction_votes'])

    # ---------------------------------------------------------------------
    # TESTING: number_bins()
    # ---------------------------------------------------------------------

    # Tests to see if function takes correct values
    def test_valid_bins(self):
        with patch("builtins.input", return_value="40"):
            result = get_number_bins()
            assert result == 40

    # Tests to see if users can pass in non_numeric_values
    def test_strings_bins(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = bins_error_message):
                get_number_bins()

    # Tests to see if users can pass values above max_number_bins
    def test_max_bins(self):
        with patch("builtins.input", return_value="55"):
            with pytest.raises(ValueError, match = bins_error_message ):
                get_number_bins()

    # Tests to see if users can pass in values below min_number_bins
    def test_min_bins(self):
        with patch("builtins.input", return_value="3"):
            with pytest.raises(ValueError, match = bins_error_message):
                get_number_bins()

    # ---------------------------------------------------------------------
    # TESTING: get_candidate_name
    # ---------------------------------------------------------------------

    # Tests to see if function takes correct values
    def test_valid_candidate(self):
        with patch("builtins.input", return_value="Donald Trump"):
            result = get_candidate_name()
            assert result == "Donald Trump"

    # Tests to see if users can pass in values not in candidate list
    def test_nonlist_candidate(self):
        with patch("builtins.input", return_value="abc"):
            with pytest.raises(ValueError, match = prompt_error_candidate):
                get_candidate_name()


    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67