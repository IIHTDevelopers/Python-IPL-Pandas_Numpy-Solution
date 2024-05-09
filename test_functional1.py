import unittest
import pandas as pd
from matches import *
from TestUtils import TestUtils

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

        # Test assertion using yakshaAssert
        if winner_of_max_win_by_runs == expected_winner:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_run", True, "functional")
            print("test_winner_of_max_win_by_runs = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_run", False, "functional")
            print("test_winner_of_max_win_by_run = Failed")

if __name__ == '__main__':
    unittest.main()
