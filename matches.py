import logging
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

matches_df = pd.read_csv("matches.csv")

total_matches = matches_df.shape[0]
print("Total number of matches:", total_matches)


winner_of_max_win_by_runs = matches_df.iloc[matches_df['win_by_runs'].idxmax()]['winner']
print("Winner of the match with maximum win by runs:", winner_of_max_win_by_runs)

winner_of_max_win_by_wickets = matches_df.iloc[matches_df['win_by_wickets'].idxmax()]['winner']
print("Winner of the match with maximum win by wickets:", winner_of_max_win_by_wickets)



most_matches_season = matches_df['season'].value_counts().idxmax()
print("Season with the most number of matches played:", most_matches_season)


# Number of tied matches
print("\nNumber of tied matches:")
print(matches_df['result'].value_counts())



# Finding the most played venue
most_played_venue = matches_df['venue'].value_counts().idxmax()
print("Most played venue:", most_played_venue)


temp_df = matches_df.drop_duplicates(subset=['season'], keep='last')[['season', 'winner']].reset_index(drop=True)

# Filter for the IPL season 2010
winner_2010 = temp_df[temp_df['season'] == 2010]['winner'].values[0]
print("Winner of IPL 2010:", winner_2010)


num_of_wins = (matches_df['win_by_wickets'] > 0).sum()
num_of_loss = (matches_df['win_by_wickets'] == 0).sum()
total_matches = num_of_wins + num_of_loss

win_percentage_batting_second = (num_of_wins / total_matches) * 100

print("Win percentage batting second:", win_percentage_batting_second)

temp_series = matches_df['player_of_match'].value_counts()[:10]

# Extracting the second most frequent player of the match awardee
second_most_player_of_match = temp_series.index[1]

print("Second most frequent player of the match awardee:", second_most_player_of_match)
