import pandas as pd
import numpy as np
from openpyxl import load_workbook
# NFL Import
from espn_api.football import League

# private league with cookies
league = League(league_id=1071885550, year=2025, espn_s2='AECC%2FBwhIYKESJcGzKKE70Ce9FDn1Vy37qzSwDVz2gWjVqxhMsnhmY0QwVyGFtfJbtrh3gPbHHUJT2LD5RHW3zO0YO3fk6LdRvoUfojTWF1VGVCvOeSQcj%2FLMbRvOeBKPM%2BZY81ZbiUTUSHwGHWVtQ2%2FRNsCs96r9xH2vcjwi2l0L8vvH1rR7pc1kV5%2Bnf1IW6DTmg2sSbNews4xZcv2uZzWILu0z%2FmxAu%2B7PePF%2FgB4b%2FxkmFJBaSxWy5AxjeAIzka%2FfzvDitsmPNYRnpztlfKeH5%2FUa0nFGxww2630gt5%2Fk9RwPOy2tVBlNRCDGnSJ0%2B4q8i4QuMF906YMR%2FpPeZiE', swid='{A658FF59-0794-4A8B-B918-16D44884A8FB}')

# Generate dataframe with high-level team stats
# team.stats gives lots of interesting stats!!
ids, names, wins, losses, ties, pf, pa, acquisitions, drops, trades, standing, draft_projected_rank = [], [], [], [], [], [], [], [], [], [], [], []
teamstats = []
for team in league.teams:
    ids.append(team.team_id); names.append(team.team_name)
    wins.append(team.wins); losses.append(team.losses); ties.append(team.ties)
    pf.append(team.points_for); pa.append(team.points_against)
    acquisitions.append(team.acquisitions); drops.append(team.drops); trades.append(team.trades)
    standing.append(team.standing); draft_projected_rank.append(team.draft_projected_rank)
    # add stats dictionary to list, with fantasy team ID added
    stats_w_ID = team.stats
    stats_w_ID['Team_ID'] = team.team_id
    teamstats.append(stats_w_ID)
#print(ids, names, wins, losses, ties, pf, pa, acquisitions, drops, trades, standing, draft_projected_rank)

# Zip into a pandas dataframe
teams_2025 = pd.DataFrame(list(zip(ids, names, wins, losses, ties, pf, pa, acquisitions, drops, trades, standing, draft_projected_rank))
                          , columns = ["Team_ID", "Team", "Wins", "Losses", "Ties", "Points_For", "Points_Against", "Acquisitions", "Drops", "Trades", "Standing", "Draft_Projected_Rank"])
print(teams_2025)

temporary = pd.DataFrame(teamstats)
print(temporary)

# Write the data to csv within codespace
#schedule_2025.to_csv("schedule_2025.csv", index=False)