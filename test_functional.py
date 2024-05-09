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
        self.test_utils = TestUtils()
    def test_winner_of_max_win_by_runs(self):
        # Get the winner of the match with maximum win by runs
        winner_of_max_win_by_runs = self.matches_df.iloc[self.matches_df['win_by_runs'].idxmax()]['winner']
        expected_winner = 'Mumbai Indians'  # Expected winner for maximum win by runs

        # Test assertion using yakshaAssert
        if winner_of_max_win_by_runs == expected_winner:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_runs", True, "functional")
            print("test_winner_of_max_win_by_runs = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_runs", False, "functional")
            print("test_winner_of_max_win_by_runs = Failed")

    def test_winner_of_max_win_by_wickets(self):
        # Get the winner of the match with maximum win by wickets
        winner_of_max_win_by_wickets = self.matches_df.iloc[self.matches_df['win_by_wickets'].idxmax()]['winner']
        expected_winner = 'Kolkata Knight Riders'  # Expected winner for maximum win by wickets

        # Test assertion using yakshaAssert
        if winner_of_max_win_by_wickets == expected_winner:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_wickets", True, "functional")
            print("test_winner_of_max_win_by_wickets = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_winner_of_max_win_by_wickets", False, "functional")
            print("test_winner_of_max_win_by_wickets = Failed")

    def test_most_matches_season(self):
        # Identify the season with the most number of matches played
        most_matches_season = self.matches_df['season'].value_counts().idxmax()
        expected_most_matches_season = '2013'  # Expected season with most number of matches played

        # Test assertion using yakshaAssert with if-else format
        if str(most_matches_season) == expected_most_matches_season:
            self.test_utils_instance.yakshaAssert("test_most_matches_season", True, "functional")
            print("test_most_matches_season = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_most_matches_season", False, "functional")
            print("test_most_matches_season = Failed")


    def test_most_played_venue(self):
        # Calculate the most played venue
        most_played_venue = self.matches_df['venue'].value_counts().idxmax()

        # Expected result
        expected_most_played_venue = 'M Chinnaswamy Stadium'  # Update with the actual expected most played venue

        # Check if the obtained venue matches the expected venue
        if most_played_venue == expected_most_played_venue:
            self.test_utils_instance.yakshaAssert("test_most_played_venue", True, "functional")
            print("test_most_played_venue = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_most_played_venue", False, "functional")
            print("test_most_played_venue = Failed")

    def test_winner_of_IPL_2010(self):
        temp_df = self.matches_df.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']].reset_index(
            drop=True)
        winner_2010 = temp_df[temp_df['season'] == 2010]['winner'].values[0]
        expected_winner = 'Chennai Super Kings'  # Expected winner of IPL 2010

        # Check if the obtained winner matches the expected winner
        if winner_2010 == expected_winner:
            self.test_utils_instance.yakshaAssert("test_winner_of_IPL_2010", True, "functional")
            print("test_winner_of_IPL_2010 = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_winner_of_IPL_2010", False, "functional")
            print("test_winner_of_IPL_2010 = Failed")

    def test_second_most_player_of_match(self):
        temp_series = self.matches_df['player_of_match'].value_counts()
        # Extracting the second most frequent player of the match awardee
        second_most_player_of_match = temp_series.index[1]

        # Expected second most frequent player of the match awardee
        expected_second_most_player = 'YK Pathan'

        # Check if the obtained second most player of the match matches the expected value
        if second_most_player_of_match == expected_second_most_player:
            self.test_utils_instance.yakshaAssert("test_second_most_player_of_match", True, "functional")
            print("test_second_most_player_of_match = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_second_most_player_of_match", False, "functional")
            print("test_second_most_player_of_match = Failed")

    def test_number_of_tied_matches(self):
        # Calculate the number of tied matches
        num_tied_matches = (self.matches_df['result'] == 'tie').sum()
        expected_tied_matches = 7  # Update with the actual expected count of tied matches

        # Test assertion using if-else
        if num_tied_matches == expected_tied_matches:
            self.test_utils.yakshaAssert("test_number_of_tied_matches", True, "functional")
            print("test_number_of_tied_matches = Passed")
        else:
            self.test_utils.yakshaAssert("test_number_of_tied_matches", False, "functional")
            print("test_number_of_tied_matches = Failed")

    def test_win_percentage_batting_second(self):
        num_of_wins = (self.matches_df['win_by_wickets'] > 0).sum()
        num_of_loss = (self.matches_df['win_by_wickets'] == 0).sum()
        total_matches = num_of_wins + num_of_loss

        win_percentage_batting_second = (num_of_wins / total_matches) * 100

        # Expected win percentage
        expected_win_percentage = 53.301886792452834

        # Check if the calculated win percentage matches the expected value
        if round(win_percentage_batting_second, 2) == round(expected_win_percentage, 2):
            self.test_utils_instance.yakshaAssert("test_win_percentage_batting_second", True, "functional")
            print("test_win_percentage_batting_second = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_win_percentage_batting_second", False, "functional")
            print("test_win_percentage_batting_second = Failed")

    def test_win_percentage_batting_second(self):
        num_of_wins = (self.matches_df['win_by_wickets'] > 0).sum()
        num_of_loss = (self.matches_df['win_by_wickets'] == 0).sum()
        total_matches = num_of_wins + num_of_loss

        win_percentage_batting_second = (num_of_wins / total_matches) * 100

        # Expected win percentage
        expected_win_percentage = 53.301886792452834

        # Check if the calculated win percentage matches the expected value
        if round(win_percentage_batting_second, 2) == round(expected_win_percentage, 2):
            self.test_utils_instance.yakshaAssert("test_win_percentage_batting_second", True, "functional")
            print("test_win_percentage_batting_second = Passed")
        else:
            self.test_utils_instance.yakshaAssert("test_win_percentage_batting_second", False, "functional")
            print("test_win_percentage_batting_second = Failed")

if __name__ == '__main__':
    unittest.main()
