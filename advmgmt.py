

from paths import *
from messages import *

from mgmt import *
from mgmt import tours_dict,teams_dict,games_dict,players_dict,staff_dict #non li importa in automatico



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
    
    
#######

def add_tour():         #TODO: aggiungere dir tour
    """
    aggiunge un torneo al db
    """
    adv_data_in()
    name = input(tour_name_question)       
    sport = input(sport_question)
    id = 0
    while str(id) in tours_dict:
        id+=1     
    insertable = dict()
    insertable['name']=name
    insertable['status']='active'
    insertable['sport']=sport
    tours_dict[str(id)] = insertable     #FIXME: gestione ';'  <- dovrebbe essere risolto<-???
    data_out()
    adv_data_out()

def list_tours(status):     #TODO: aggiungere filtraggio su sport
    """
    lista e ritorna tutti i tornei del tipo status
    """
    adv_data_in()
    print(active_tour_message) #TODO: generalizzare
    returnable = dict()
    for id in tours_dict:
        if tours_dict[id]['status'] == status:
            returnable[id]=tours_dict[id]
            print(f'[{id}]-{tours_dict[id]['name']}-{tours_dict[id]['status']}-{tours_dict[id]['sport']}'.strip())
    return returnable

def set_tour(id,nome,status,sport):
    """
    modifica tornei esistenti
    se nome, status o sport sono 'keep' non vengono modificati
    """
    adv_data_in()
    previous_name = tours_dict[id]['name']
    previous_status = tours_dict[id]['status']
    previous_sport = tours_dict[id]['sport']
    
    if nome =='keep':
        nome = previous_name
    if status =='keep':
        status = previous_status
    if sport =='keep':
        sport = previous_sport
    tours_dict[id]={'name':nome,'status':status,'sport':sport}  #FIXME: gestione ';' <- dovrebbbe essere risolto<-non so più quanto sia valido
    data_out()
    adv_data_out()

def tour_exists(id):
    return (str(id) in tours_dict)
    
def remove_tour(id):
    adv_data_in()
    if id in tours_dict:
        conferma = input(f'Removing tournament [{id}]-{tours_dict[id]['name']} - {tours_dict[id]['status']} - {tours_dict[id]['sport']} \n Are you sure? Y/N')        #FIXME:TODO: mark
        if conferma.lower().strip() == 'y':
            tours_dict.pop(id)
    else:
        print(wrong_tour_id)
    data_out()
    adv_data_out()

def get_tour(id):
    return tours_dict[str(id)]

############

def add_team(tour_id):      #TODO: aggiungere dir team
    adv_data_in()

    name = input(team_name_question)       
    sport = get_tour(tour_id)['sport']    

    team_id = 0
    while str(team_id) in teams_dict:
        team_id+=1       #FIXME: <- agigungere logica calcolo id
    
    insertable = dict()
    insertable['name']=name
    insertable['tour_id'] = str(tour_id)
    insertable['team_id'] = str(team_id)
    insertable['sport']=sport
    insertable['rank-score']=insertable['win']=insertable['draw']=insertable['lose']=insertable['points-in']=insertable['points-out']='0'
    teams_dict[str(team_id)] = insertable
    data_out()
    adv_data_out()

def remove_team():
    return

def manage_team():
    return

def get_teams_by_tour(tour_id):
    result = dict()

    for id in teams_dict:
        if str(teams_dict[id]['tour_id']) == str(tour_id):
            result[id] = teams_dict[id]
    
    return result






#########
#stats

def update_tour_stats():
    adv_data_in()
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