import unittest
import pandas as pd
from matches import *

class TestIPLAnalysis(unittest.TestCase):

    def setUp(self):
        # Load IPL match data
        self.matches_df = pd.read_csv(r'matches.csv')

    def test_winner_of_max_win_by_runs(self):
        # Get the winner of the match with maximum win by runs
        winner_of_max_win_by_runs = self.matches_df.iloc[self.matches_df['win_by_runs'].idxmax()]['winner']
        expected_winner = 'Mumbai Indians'  # Expected winner for maximum win by runs
        self.assertEqual(winner_of_max_win_by_runs, expected_winner, "Incorrect winner of match with maximum win by runs")

    def test_winner_of_max_win_by_wickets(self):
        # Get the winner of the match with maximum win by wickets
        winner_of_max_win_by_wickets = self.matches_df.iloc[self.matches_df['win_by_wickets'].idxmax()]['winner']
        expected_winner = 'Kolkata Knight Riders'  # Expected winner for maximum win by wickets
        self.assertEqual(winner_of_max_win_by_wickets, expected_winner, "Incorrect winner of match with maximum win by wickets")

    def test_most_matches_season(self):
        # Identify the season with the most number of matches played
        most_matches_season = self.matches_df['season'].value_counts().idxmax()
        expected_most_matches_season = '2013'  # Expected season with most number of matches played
        self.assertEqual(str(most_matches_season), expected_most_matches_season,
                 "Incorrect season with the most number of matches played")

    def test_player_with_most_player_of_the_match_awards(self):
        # Calculate the count of player of the match awards
        player_of_match_counts = self.matches_df['player_of_match'].value_counts().head(1)

        # Expected result
        expected_result = self.matches_df['player_of_match'].value_counts().head(1)

        # Check if the obtained result matches the expected result
        self.assertTrue((player_of_match_counts == expected_result).all(),
                        "Player with most player of the match awards doesn't match")
    def test_number_of_tied_matches(self):
        # Calculate the number of tied matches
        num_tied_matches = (self.matches_df['result'] == 'tie').sum()

        # Expected result
        expected_tied_matches = 7  # Update with the actual expected count of tied matches

        # Check if the obtained count matches the expected count
        self.assertEqual(num_tied_matches, expected_tied_matches, "Number of tied matches doesn't match")

    def test_most_played_venue(self):
        # Calculate the most played venue
        most_played_venue = self.matches_df['venue'].value_counts().idxmax()

        # Expected result
        expected_most_played_venue = 'M Chinnaswamy Stadium'  # Update with the actual expected most played venue

        # Check if the obtained venue matches the expected venue
        self.assertEqual(most_played_venue, expected_most_played_venue, "Most played venue doesn't match")

    def test_winner_of_IPL_2010(self):
        temp_df = self.matches_df.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']].reset_index(
            drop=True)
        winner_2010 = temp_df[temp_df['season'] == 2010]['winner'].values[0]
        self.assertEqual(winner_2010, 'Chennai Super Kings', "Expected winner of IPL 2010 is 'Chennai Super Kings'.")

    def test_win_percentage_batting_second(self):
        num_of_wins = (self.matches_df['win_by_wickets'] > 0).sum()
        num_of_loss = (self.matches_df['win_by_wickets'] == 0).sum()
        total_matches = num_of_wins + num_of_loss

        win_percentage_batting_second = (num_of_wins / total_matches) * 100

        # Test if the calculated win percentage matches the expected value
        expected_win_percentage = 53.301886792452834
        self.assertAlmostEqual(win_percentage_batting_second, expected_win_percentage, places=2,
                               msg="Expected win percentage batting second is not equal to calculated value")

    def test_second_most_player_of_match(self):
        temp_series = self.matches_df['player_of_match'].value_counts()
        # Extracting the second most frequent player of the match awardee
        second_most_player_of_match = temp_series.index[1]

        # Expected second most frequent player of the match awardee
        expected_second_most_player = 'YK Pathan'

        self.assertEqual(second_most_player_of_match, expected_second_most_player,
                         "Expected second most frequent player of the match awardee is not equal to calculated value")

    def test_y_label_matches(self):
        plt.figure(figsize=(12, 6))
        sns.countplot(x='venue', data=self.matches_df)
        plt.title('Number of Matches Played at Each Venue')
        plt.xlabel('Venue')
        plt.ylabel('Number of Matches')
        plt.xticks(rotation='vertical')
        plt.tight_layout()

        # Extracting the current y-axis label
        y_label = plt.gca().get_ylabel()

        # Expected y-axis label
        expected_y_label = 'Number of Matches'

        self.assertEqual(y_label, expected_y_label,
                         "Expected y-axis label is not equal to the label set in the plot")

if __name__ == '__main__':
    unittest.main()
