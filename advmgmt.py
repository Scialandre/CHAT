

from paths import *
from messages import *

from mgmt import *
from stats import *


def adv_data_in():

    """legge dati da file"""
    
    file = open(adv_toursfile,'r')      #lettura file tornei

    id = ''
    name = ''
    status = ''
    sport = ''

    for line in file:       
        
        if line.strip().startswith('#'):
            tours_dict[id] = {'name':name,'status':status,'sport':sport}

        if line.strip().startswith('ID:'):
            id = line.replace('ID:','').strip()
        
        if line.strip().startswith('NAME:'):
            name = line.replace('NAME:','').strip()

        if line.strip().startswith('STATUS:'):
            status = line.replace('STATUS:','').strip()

        if line.strip().startswith('SPORT:'):
            sport = line.replace('SPORT:','').strip()

        if line.strip().startswith('GAMES:'):
            splat = line.replace('GAMES:','').strip().split(',')
            for i in range(0,len(splat),2):
                entry = splat[i:i+2]
                if len(entry) == 2:
                    splot = entry[1].split('/')         #ho finito i nomi per le variabili
                    games_dict[entry[0]] = {'game_id':entry[0].strip(),'tour_id':id,'team1_id':splot[0].split('-')[0].strip(),'team2_id':splot[0].split('-')[1].strip(),'type':'norm','team1_score':splot[1].split('-')[0].strip(),'team2_score':splot[1].split('-')[1].strip()}
                

    file.close()

    
    
    file = open(adv_teamsfile,'r')      #lettura file squadre

    id = ''
    name = ''
    tour_id = ''
    sport = ''
    rank_score = ''
    win = ''
    draw = ''
    lose = ''
    score_out = ''
    score_in = ''

    for line in file:       #lettura file tornei
        
        if line.strip().startswith('#'):                ## FIXME:? la prima linea del file può caricare una entry nulla nei dict
            teams_dict[id] = {'name':name,'tour_id':tour_id,'sport':sport,'rank_score':rank_score,'win':win,'draw':draw,'lose':lose,'points_out':score_out,'points_in':score_in}

        if line.strip().startswith('ID:'):
            id = line.replace('ID:','').strip()
        
        if line.strip().startswith('NAME:'):
            name = line.replace('NAME:','').strip()

        if line.strip().startswith('TOUR_ID:'):
            tour_id = line.replace('TOUR_ID:','').strip()

        if line.strip().startswith('SPORT:'):
            sport = line.replace('SPORT:','').strip()

        if line.strip().startswith('PLAYERS:'):
            splat = line.replace('PLAYERS:','').split(',')
            for i in range(0,len(splat),2):
                entry = splat[i:i+2]
                if len(entry) == 2:
                    players_dict[f'{id}-{entry[0].split('-')[0].strip()}'] = {'role':entry[0].split('-')[1],'name':entry[1].strip()}

        if line.strip().startswith('STAFF:'):
            splat = line.replace('STAFF:','').split(',')
            for i in range(0,len(splat),2):
                entry = splat[i:i+2]
                if len(entry) == 2:
                    staff_dict[f'{id}-{entry[0].split('-')[0].strip()}'] = {'role':entry[0].split('-')[1].strip(),'name':entry[1].strip()}

        if line.strip().startswith('RANK_SCORE:'):
            rank_score = line.replace('RANK_SCORE:','').strip()

        if line.strip().startswith('WIN:'):
            win = line.replace('WIN:','').strip()

        if line.strip().startswith('DRAW:'):
            draw = line.replace('DRAW:','').strip()

        if line.strip().startswith('LOSE:'):
            lose = line.replace('LOSE:','').strip()

        if line.strip().startswith('SCORE_OUT:'):
            score_out = line.replace('SCORE_OUT:','').strip()

        if line.strip().startswith('SCORE_IN:'):
            score_in = line.replace('SCORE_IN:','').strip()

    file.close()

def adv_data_out():

    """scrive dati sui file"""

    update_tour_stats()

    spacer = '\n##########\n'

    file = open(adv_toursfile,'w')      ## scrittura file tornei
    file.write(spacer)
    for id in tours_dict:

        first = True

        file.write(f'ID: {id}\n')
        file.write(f'NAME: {tours_dict[id]['name']}\n')
        file.write(f'STATUS: {tours_dict[id]['status']}\n')
        file.write(f'SPORT: {tours_dict[id]['sport']}\n')
        file.write('GAMES: ')
        for gid in games_dict:
            if str(games_dict[gid]['tour_id']).strip() == str(id).strip():
                if first:
                    first = not first
                else:
                    file.write(',')
                file.write(f' {gid.strip()}, {games_dict[gid]['team1_id'].strip()}-{games_dict[gid]['team2_id'].strip()}/{games_dict[gid]['team1_score'].strip()}-{games_dict[gid]['team2_score'].strip()}')

            ##aggiungere eventuale logica per  partite di tipo diverso

        file.write(f'\n{spacer}')
    file.close()

    #return     #<-evita aggiornamento teams per evitare casini con i ruoli

    file = open(adv_teamsfile,'w')      ## scritture file squadre
    file.write(spacer)
    for id in teams_dict:

        first = True

        file.write(f'ID: {id}\n')
        file.write(f'NAME: {teams_dict[id]['name']}\n')
        file.write(f'TOUR_ID: {teams_dict[id]['tour_id']}\n')
        file.write(f'SPORT: {teams_dict[id]['sport']}\n')
        file.write('PLAYERS: ')
        for pid in players_dict:
            if pid.split('-')[0] == id:
                if first:
                    first = not first
                else:
                    file.write(',')
                file.write(f' {pid.split('-')[1]}-{players_dict[pid]['role']}, {players_dict[pid]['name']}')
        file.write('\n')
        file.write('STAFF: ')
        first = True
        for sid in staff_dict:
            if sid.split('-')[0] == id:
                if first:
                    first = not first
                else:
                    file.write(';')
                file.write(f' {sid.split('-')[1]}-{staff_dict[sid]['role']}, {staff_dict[sid]['name']}')
        file.write('\n')
        file.write(f'RANK_SCORE: {teams_dict[id]['rank_score']}\n')
        file.write(f'WIN: {teams_dict[id]['win']}\n')
        file.write(f'DRAW: {teams_dict[id]['draw']}\n')
        file.write(f'LOSE: {teams_dict[id]['lose']}\n')
        file.write(f'SCORE_OUT: {teams_dict[id]['points_out']}\n')
        file.write(f'SCORE_IN: {teams_dict[id]['points_in']}\n')




        file.write(f'{spacer}')
    file.close()







    
    #file.write(f'{ids};{teams_dict[ids]['tour_id']};{teams_dict[ids]['name']};{teams_dict[ids]['sport']}')
    #file.write(f';{teams_dict[ids]['rank_score']};{teams_dict[ids]['win']};{teams_dict[ids]['draw']};{teams_dict[ids]['lose']}')
    #file.write(f';{teams_dict[ids]['points_out']};{teams_dict[ids]['points_in']}')
    
    