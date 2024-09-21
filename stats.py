from paths import *
from messages import *

from mgmt import *

def update_tour_stats(tour_id):
    data_in()

    teams = get_teams_by_tour(tour_id)

    for id in teams:
        rank_score = 0
        score_in = 0
        score_out = 0
        win = 0
        draw = 0
        lose = 0

        for gid in games_dict:
            game = games_dict[gid]
            valid = str(game['tour_id']) ==  str(tour_id)
            team1 = int(game['team1_id']) == (teams[id]['team_id'])
            team2 = int(game['team2_id']) == (teams[id]['team_id'])
            team1win = int(game['team1_score']) > int(game['team2_score'])
            result_draw = int(game['team1_score']) == int(game['team2_score'])
            if valid and team1:
                if team1win:
                    win +=1
                    rank_score+=3
                elif result_draw:
                    draw +=1
                    rank_score+=1
                else:
                    lose+=1
                score_in+=game['team2_score']
                score_out+=game['team1_score']
            if valid and team2:
                if team1win:
                    lose +=1
                elif result_draw:
                    draw +=1
                    rank_score+=1
                else:
                    win+=1
                    rank_score+=3
                score_in+=game['team2_score']
                score_out+=game['team1_score']

        teams_dict[id]['rank-score'] = rank_score
        teams_dict[id]['rank-score'] = rank_score
        teams_dict[id]['rank-score'] = rank_score
        teams_dict[id]['rank-score'] = rank_score
        teams_dict[id]['rank-score'] = rank_score



    data_out()