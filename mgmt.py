# funzioni per la gestione dati, versione datata, possibile rimozione

from messages import *
from paths import *



# gestione tornei

tours_dict = dict()
teams_dict = dict()
players_dict = dict()
staff_dict = dict()
games_dict = dict()


def data_in():
    """
    legge dati dai file
    """
    file = open(toursfile,'r')
    for line in file:
        splatline = line.strip().split(';')
        tours_dict[splatline[0]]={'name':splatline[1],'status':splatline[2],'sport':splatline[3]}
    file.close()
    file = open(teamsfile,'r')
    for line in file:
        splatline = line.strip().split(';')
        teams_dict[f'{splatline[0]}']={'name':splatline[2],'sport':splatline[3],'tour_id':splatline[1],'team_id':splatline[0],'rank_score':splatline[4],'win':splatline[5],'draw':splatline[6],'lose':splatline[7],'points_out':splatline[8],'points_in':splatline[9]}
    file.close()
    file = open(stafffile,'r')
    for line in file:
        splatline = line.strip().split(';')
        staff_dict[f'{splatline[0]}-{splatline[1]}']={'name':splatline[2],'role':splatline[3]}        
    file.close()
    file = open(playersfile,'r')
    for line in file:
        splatline = line.strip().split(';')
        players_dict[f'{splatline[0]}-{splatline[1]}']={'name':splatline[2],'role':splatline[3]}
    file.close()
    file = open(gamesfile,'r')
    for line in file:
        splatline = line.strip().split(';')
        games_dict[f'{splatline[0]}']={'game_id':splatline[0],'tour_id':splatline[1],'team1_id':splatline[2],'team2_id':splatline[3],'type':splatline[4],'team1_score':splatline[5],'team2_score':splatline[6]}
    file.close()

def data_out():
    """
    scrive dati sui file
    """
    file = open(toursfile,'w')
    first = True
    for id in tours_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{id};{tours_dict[id]['name']};{tours_dict[id]['status']};{tours_dict[id]['sport']}')
    file.close()
    file = open(teamsfile,'w')
    first = True
    for ids in teams_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{ids};{teams_dict[ids]['tour_id']};{teams_dict[ids]['name']};{teams_dict[ids]['sport']}')
        file.write(f';{teams_dict[ids]['rank_score']};{teams_dict[ids]['win']};{teams_dict[ids]['draw']};{teams_dict[ids]['lose']}')
        file.write(f';{teams_dict[ids]['points_out']};{teams_dict[ids]['points_in']}')
    file.close()
    file = open(stafffile,'w')
    first = True
    for ids in staff_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{ids.replace('-',';')};{staff_dict[ids]['name']};{staff_dict[ids]['role']}')
    file.close()
    file = open(playersfile,'w')
    first = True
    for ids in players_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{ids.replace('-',';')};{players_dict[ids]['name']};{players_dict[ids]['role']}')
    file.close()
    file = open(gamesfile,'w')
    first = True
    for id in games_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{id};{games_dict[id]['tour_id']};{games_dict[id]['team1_id']};{games_dict[id]['team2_id']};{games_dict[id]['type']};{games_dict[id]['team1_score']};{games_dict[id]['team2_score']}')
    file.close()
    
