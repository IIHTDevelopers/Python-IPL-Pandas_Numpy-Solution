import unittest
import pandas as pd
from matches import *
from test.TestUtils import TestUtils

class TestIPLAnalysis(unittest.TestCase):

    def setUp(self):
        # Load IPL match data
        self.matches_df = pd.read_csv(r'matches.csv')
        # Instantiate an object of TestUtils
        self.test_utils_instance = TestUtils()

    def test_winner_of_max_win_by_runs(self):
        # Get the winner of the match with maximum win by runs
        winner_of_max_win_by_runs = self.matches_df.iloc[self.matches_df['win_by_runs'].idxmax()]['winner']
        expected_winner = 'Mumbai Indians'  # Expected winner for maximum win by runs
        result = winner_of_max_win_by_runs == expected_winner

        # Assert the test result using yakshaAssert method
        self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_runs", result, "Functional")

        # Print pass/fail message based on the test result
        if result:
            print("test_winner_of_max_win_by_runs = Passed")
        else:
            print("test_winner_of_max_win_by_runs = Failed")

if __name__ == '__main__':
    unittest.main()
