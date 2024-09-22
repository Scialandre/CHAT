from paths import *
from messages import *

from mgmt import *

def update_tour_stats():
    data_in()
    zero_stats()
        
    for key in games_dict:
        game = games_dict[key]

        valid = game['tour_id']==teams_dict[game['team1_id']]['tour_id'] and game['tour_id']==teams_dict[game['team2_id']]['tour_id']
        game_result = int(game['team1_score'])-int(game['team2_score'])
        
        if valid:
            if game_result > 0:
                teams_dict[game['team1_id']]['win'] = str(int(teams_dict[game['team1_id']]['win']) + 1)
                teams_dict[game['team1_id']]['rank_score'] = str(int(teams_dict[game['team1_id']]['rank_score']) + 3)

                teams_dict[game['team2_id']]['lose'] = str(int(teams_dict[game['team2_id']]['lose']) + 1)
            elif game_result < 0:
                teams_dict[game['team2_id']]['win'] = str(int(teams_dict[game['team2_id']]['win']) + 1)
                teams_dict[game['team2_id']]['rank_score'] = str(int(teams_dict[game['team2_id']]['rank_score']) + 3)

                teams_dict[game['team1_id']]['lose'] = str(int(teams_dict[game['team1_id']]['lose']) + 1)
            elif game_result == 0:
                teams_dict[game['team1_id']]['draw'] = str(int(teams_dict[game['team1_id']]['draw']) + 1)
                teams_dict[game['team1_id']]['rank_score'] = str(int(teams_dict[game['team1_id']]['rank_score']) + 1)

                teams_dict[game['team2_id']]['draw'] = str(int(teams_dict[game['team2_id']]['draw']) + 1)
                teams_dict[game['team2_id']]['rank_score'] = str(int(teams_dict[game['team2_id']]['rank_score']) + 1)

            teams_dict[game['team1_id']]['points_out'] = str(int(teams_dict[game['team1_id']]['points_out']) + int(game['team1_score']))
            teams_dict[game['team2_id']]['points_out'] = str(int(teams_dict[game['team2_id']]['points_out']) + int(game['team2_score']))
            
            teams_dict[game['team1_id']]['points_in'] = str(int(teams_dict[game['team1_id']]['points_in']) + int(game['team2_score']))
            teams_dict[game['team2_id']]['points_in'] = str(int(teams_dict[game['team2_id']]['points_in']) + int(game['team1_score']))

    data_out()

def zero_stats():
    for key in teams_dict:
        teams_dict[key]['win']='0'
        teams_dict[key]['draw']='0'
        teams_dict[key]['lose']='0'
        teams_dict[key]['rank_score']='0'
        teams_dict[key]['points_in']='0'
        teams_dict[key]['points_out']='0'