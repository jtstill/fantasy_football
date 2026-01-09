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

# Gather necessary information for all home and away teams in each week (use week (11) as example, but will iterate)
week = 11
box_scores = league.box_scores(week)
#print(box_scores)

# start with home_team (use [2] as example, but will iterate)
print("Week ", week)
print("Team: ", box_scores[2].home_team.team_name) # team name
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
away = box_scores[2].away_team