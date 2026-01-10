import pandas as pd
import numpy as np
from openpyxl import load_workbook
# NFL Import
from espn_api.football import League

# private league with cookies
league = League(league_id=1071885550, year=2025, espn_s2='AECC%2FBwhIYKESJcGzKKE70Ce9FDn1Vy37qzSwDVz2gWjVqxhMsnhmY0QwVyGFtfJbtrh3gPbHHUJT2LD5RHW3zO0YO3fk6LdRvoUfojTWF1VGVCvOeSQcj%2FLMbRvOeBKPM%2BZY81ZbiUTUSHwGHWVtQ2%2FRNsCs96r9xH2vcjwi2l0L8vvH1rR7pc1kV5%2Bnf1IW6DTmg2sSbNews4xZcv2uZzWILu0z%2FmxAu%2B7PePF%2FgB4b%2FxkmFJBaSxWy5AxjeAIzka%2FfzvDitsmPNYRnpztlfKeH5%2FUa0nFGxww2630gt5%2Fk9RwPOy2tVBlNRCDGnSJ0%2B4q8i4QuMF906YMR%2FpPeZiE', swid='{A658FF59-0794-4A8B-B918-16D44884A8FB}')

'''
# See box score from Week 11 against Nick
box_scores = league.box_scores(11)
#print(box_scores)
print(box_scores[2].home_team)
print(box_scores[2].away_team)
print(box_scores[2].home_lineup)
# benched Courtland Sutton in week 11
# started Ja'Marr Chase in week 11
print(box_scores[2].home_lineup[3].name, ":", box_scores[2].home_lineup[3].lineupSlot)
print(box_scores[2].home_lineup[0].name, ":", box_scores[2].home_lineup[0].lineupSlot) # gives the same thing as slot_position
print(box_scores[2].home_lineup[0].name, ":", box_scores[2].home_lineup[0].slot_position) # slot_position is box player var
'''



# Want df of:
# Team information: Week, Team
# Player information: name, position, (eligibleSlots?), proTeam
# Box Player information: slot_position, points, projected_points, pro_opponent, pro_pos_rank, game_played, game_date, on_bye_week, active_status

### Gather necessary information for all home and away teams in each week

# Instantiate the lists for each column
weeks, teams, player_names, positions, proTeams, slot_positions, points, projected_points, pro_opponents, pro_pos_ranks, games_played, game_dates, bye_weeks, active_statuses = [], [], [], [], [], [], [], [], [], [], [], [], [], []
#print(weeks, teams, player_names, positions, proTeams, slot_positions, points, projected_points, pro_opponents, pro_pos_ranks, games_played, game_dates, bye_weeks, active_statuses, sep = "\n")

# Iterate through each week
for week in range(1, 15):
    print(week)
    box_scores = league.box_scores(week)
    #print(box_scores)
    # Iterate through each matchup
    for matchup in box_scores:
        # Start with home_team stats
        for p in matchup.home_lineup:
            # Add one copy of week and fantasy team name per lineup slot
            weeks.append(week) # add one copy of the week
            teams.append(matchup.home_team.team_name) # add one copy of fantasy team name
            player_names.append(p.name); positions.append(p.position); proTeams.append(p.proTeam); slot_positions.append(p.slot_position)
            # Add each element to its respective list
            if p.on_bye_week:
                points.append(None); projected_points.append(None); pro_opponents.append(None); pro_pos_ranks.append(None)
                games_played.append(None); game_dates.append(None); bye_weeks.append(None); active_statuses.append(None)
            else:
                points.append(p.points); projected_points.append(p.projected_points)
                pro_opponents.append(p.pro_opponent); pro_pos_ranks.append(p.pro_pos_rank)
                games_played.append(p.game_played); game_dates.append(p.game_date.strftime("%Y-%m-%d %H:%M:%S"))
                bye_weeks.append(p.on_bye_week); active_statuses.append(p.active_status)

        # Next, do away team stats
        for p in matchup.away_lineup:
            # Add one copy of week and fantasy team name per lineup slot
            weeks.append(week) # add one copy of the week
            teams.append(matchup.away_team.team_name) # add one copy of fantasy team name
            player_names.append(p.name); positions.append(p.position); proTeams.append(p.proTeam); slot_positions.append(p.slot_position)
            # Add each element to its respective list
            if p.on_bye_week:
                points.append(None); projected_points.append(None); pro_opponents.append(None); pro_pos_ranks.append(None)
                games_played.append(None); game_dates.append(None); bye_weeks.append(None); active_statuses.append(None)
            else:
                points.append(p.points); projected_points.append(p.projected_points)
                pro_opponents.append(p.pro_opponent); pro_pos_ranks.append(p.pro_pos_rank)
                games_played.append(p.game_played); game_dates.append(p.game_date.strftime("%Y-%m-%d %H:%M:%S"))
                bye_weeks.append(p.on_bye_week); active_statuses.append(p.active_status)

print(weeks, teams, player_names, positions, proTeams, slot_positions, points, projected_points, pro_opponents, pro_pos_ranks, games_played, game_dates, bye_weeks, active_statuses, sep = "\n")


### Zip into a pandas dataframe
stats_2025 = pd.DataFrame(list(zip(weeks, teams, player_names, positions, proTeams, slot_positions, points, projected_points, pro_opponents, pro_pos_ranks, games_played, game_dates, bye_weeks, active_statuses))
                          , columns = ["Week", "Team", "Player", "Position", "Pro_Team", "Lineup Position", "Points", "Projected_Points", "Pro_Opponent", "Pro_Position_Rank", "Game_Played", "Game_Date", "On_Bye", "Active_Status"])
print(stats_2025)

### Write the data to csv within codespace
stats_2025.to_csv("stats_2025.csv", index=False)



'''
# start with home_team (use [2] as example, but will iterate)
print("Week ", week)
print("Home Team: ", box_scores[2].home_team.team_name) # team name
for p in box_scores[2].home_lineup:
    if p.on_bye_week: # make everything game-related null
        print(p.name, p.position, p.proTeam, 
            p.slot_position, None, None, None, None, None, None, p.on_bye_week, p.active_status, sep = ", ")
    else:
        print(p.name, p.position, p.proTeam, 
            p.slot_position, p.points, p.projected_points, 
            p.pro_opponent, p.pro_pos_rank, 
            p.game_played, getattr(p, 'game_date', None), p.on_bye_week, p.active_status,
            sep = ", ")

# do the same for away_team
print("Away Team: ", box_scores[2].away_team.team_name) # team name
for p in box_scores[2].away_lineup:
    if p.on_bye_week: # make everything game-related null
        print(p.name, p.position, p.proTeam, 
            p.slot_position, None, None, None, None, None, None, p.on_bye_week, p.active_status, sep = ", ")
    else:
        print(p.name, p.position, p.proTeam, 
            p.slot_position, p.points, p.projected_points, 
            p.pro_opponent, p.pro_pos_rank, 
            p.game_played, getattr(p, 'game_date', None), p.on_bye_week, p.active_status,
            sep = ", ")
'''