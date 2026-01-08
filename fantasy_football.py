import pandas as pd
import numpy as np
from openpyxl import load_workbook
# NFL Import
from espn_api.football import League

# private league with cookies
league = League(league_id=1071885550, year=2025, espn_s2='AECC%2FBwhIYKESJcGzKKE70Ce9FDn1Vy37qzSwDVz2gWjVqxhMsnhmY0QwVyGFtfJbtrh3gPbHHUJT2LD5RHW3zO0YO3fk6LdRvoUfojTWF1VGVCvOeSQcj%2FLMbRvOeBKPM%2BZY81ZbiUTUSHwGHWVtQ2%2FRNsCs96r9xH2vcjwi2l0L8vvH1rR7pc1kV5%2Bnf1IW6DTmg2sSbNews4xZcv2uZzWILu0z%2FmxAu%2B7PePF%2FgB4b%2FxkmFJBaSxWy5AxjeAIzka%2FfzvDitsmPNYRnpztlfKeH5%2FUa0nFGxww2630gt5%2Fk9RwPOy2tVBlNRCDGnSJ0%2B4q8i4QuMF906YMR%2FpPeZiE', swid='{A658FF59-0794-4A8B-B918-16D44884A8FB}')

'''
# All Teams
#print(league.teams)

# Specific teams
JacksBacks = league.teams[11]
#print(JacksBacks.roster)

# See box score from Week 11 against Nick
box_scores = league.box_scores(11)
#print(box_scores)
print(box_scores[2].home_team)
print(box_scores[2].away_team)
print(box_scores[2].home_lineup)
# benched Courtland Sutton in week 11
# started Ja'Marr Chase in week 11
print(box_scores[2].home_lineup[3].name, ":", box_scores[2].home_lineup[3].lineupSlot)
print(box_scores[2].home_lineup[0].name, ":", box_scores[2].home_lineup[0].lineupSlot)
'''

# Generate a pandas dataframe of high level matchup stats
regular_season_length = 14

# Instantiate empty lists and the week counter
weeks = list(range(1, regular_season_length + 1)) * 12
opponents, scores, outcomes, teamnames = [], [], [], []

# Iterate through all 12 teams
for i in range(0, 12):
    teamnames = teamnames + [league.teams[i].team_name] * regular_season_length                             # Generate 14 copies of the Team name
    opponents = opponents + [team.team_name for team in league.teams[i].schedule][:regular_season_length]   # Populate all reg season matchups
    scores = scores + league.teams[i].scores[:regular_season_length]                                        # Populate all reg season scores
    outcomes = outcomes + league.teams[i].outcomes[:regular_season_length]                                  # Populate all reg season outcomes

# Zip into a pandas dataframe
schedule_2025 = pd.DataFrame(list(zip(teamnames, weeks, opponents, scores, outcomes)), columns = ['Team', 'Week', 'Opponent', 'Score', 'Outcome'])
print(schedule_2025)

# Write the data to csv within codespace
schedule_2025.to_csv("schedule_2025.csv", index=False)



