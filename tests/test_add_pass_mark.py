"""The script is for unit testing."""

import csv
import unittest
from add_pass_mark import *
from add_pass_mark import increase_score, increase_score_v2
import os


class TestScoreIncrease(unittest.TestCase):

    def test_file_not_found(self):
        """Test whether the input file exists or not."""
        testcase1 = increase_score_v2()
        self.assertTrue(testcase1, os.path.exists('new_students_results.csv'))
    
    def test_increase_score_V2(self):
        """Test version V2 increase score"""
        # open('new_students_results.csv', 'r', encoding="utf-8") as output_file;
        # testcase1 = increase_score_v2()
        
        # self.assertEqual(testcase1, open('new_students_results.csv', 'r', encoding="utf-8"))
        with open('new_students_results.csv', 'r', encoding="utf-8") as test_file:
            reader = csv.reader(test_file)
            next(reader)
            
            row_1 = next(reader)
            self.assertEqual(row_1, ["toyin", " 41"])

            row_2 = next(reader)
            self.assertEqual(row_2, ["tutu", " 77"])



    def test_increase_score(self):
        """Test version V1 increase score"""

        testcase2 = increase_score()
        self.assertEqual(testcase2,  {'toyin': 41, 'tutu': 77, 'ade': 92, 'yemi': 54,
                                      'sola': 39, 'dejo': 100, 'joba': 71, 'wasiu': 59, 'uthman': 73})


if __name__ == "__main__":
    unittest.main()
