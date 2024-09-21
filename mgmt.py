# funzioni per la gestione (db?)

from messages import *
from paths import *

# gestione tornei

tours_dict = dict()
teams_dict = dict()
players_dict = dict()
staff_dict = dict()


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
        teams_dict[f'{splatline[0]};{splatline[1]}']={'name':splatline[2],'sport':splatline[3],'tour_id':splatline[0],'team_id':splatline[1],'rank-score':splatline[4],'win':splatline[5],'draw':splatline[6],'lose':splatline[7],'points-in':splatline[8],'points-out':splatline[9]}
    file.close()
    file = open(stafffile,'r')
    for line in file:
        splatline = line.strip().split(';')
        staff_dict[f'{splatline[0]};{splatline[1]};{splatline[2]}']=splatline[3]        #aggiungere gli altri dati??
    file.close()
    file = open(playersfile,'r')
    for line in file:
        splatline = line.strip().split(';')
        players_dict[f'{splatline[0]};{splatline[1]};{splatline[2]}']=splatline[3]
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
        file.write(f'{ids};{teams_dict[ids]['name']};{teams_dict[ids]['sport']}')
        file.write(f';{teams_dict[ids]['rank-score']};{teams_dict[ids]['win']};{teams_dict[ids]['draw']};{teams_dict[ids]['lose']}')
        file.write(f';{teams_dict[ids]['points-in']};{teams_dict[ids]['points-out']}')
    file.close()
    file = open(stafffile,'w')
    first = True
    for ids in staff_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{ids};{staff_dict[ids]}')
    file.close()
    file = open(playersfile,'w')
    first = True
    for ids in players_dict:
        if not first:
            file.write('\n')
        else:
            first = not first
        file.write(f'{ids};{players_dict[ids]}')
    file.close()
    
#######

def add_tour():
    """
    aggiunge un torneo al db
    """
    data_in()
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

def list_tours(status):     #TODO: aggiungere filtraggio su sport
    """
    lista e ritorna tutti i tornei del tipo status
    """
    data_in()
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
    data_in()
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
    
def tour_exists(id):
    return (str(id) in tours_dict)
    
def remove_tour(id):
    data_in()
    if id in tours_dict:
        conferma = input(f'Removing tournament [{id}]-{tours_dict[id]['name']} - {tours_dict[id]['status']} - {tours_dict[id]['sport']} \n Are you sure? Y/N')        #FIXME:TODO: mark
        if conferma.lower().strip() == 'y':
            tours_dict.pop(id)
    else:
        print(wrong_tour_id)
    data_out()

def get_tour(id):
    return tours_dict[str(id)]

############

def add_team(tour_id):
    data_in()

    name = input(team_name_question)       
    sport = get_tour(tour_id)['sport']    

    team_id = 0
    teams = get_teams_by_tour(str(tour_id))
    while str(team_id) in teams:
        team_id+=1 
    id = str(tour_id) + ';' + str(team_id)      #FIXME: <- agigungere logica calcolo id
    
    insertable = dict()
    insertable['name']=name
    insertable['tour_id'] = str(tour_id)
    insertable['team_id'] = str(team_id)
    insertable['sport']=sport
    insertable['rank-score']=insertable['win']=insertable['draw']=insertable['lose']=insertable['points-in']=insertable['points-out']='0'
    teams_dict[id] = insertable
    data_out()

def remove_team():
    return

def manage_team():
    return

def get_teams_by_tour(tour_id):
    result = dict()

    for id in teams_dict:
        if str(teams_dict[id]['tour_id']) == str(tour_id):
            result[id.split(';')[1]] = teams_dict[id]
    
    return result