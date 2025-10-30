import unittest
from  mainCode import *
import os


# define the unit tests
class my_unit_tests(unittest.TestCase):

#FILE HANDLING

        # tests if the csv file has been saved
    def test_csv_file_exists(self):
        self.assertTrue(os.path.isfile('usData.csv'))

    # run the tests
if __name__ == "__main__":
    unittest.main()


# y = 4.07x -0.67