# funzioni per la gestione (db?)

from messages import *
from paths import *

# gestione tornei

tour_dict = dict()
teams_dict = dict()
players_dict = dict()
staff_dict = dict()


def data_in():
    """
    legge dati dai file
    """
    file = open(toursfile,'r')
    for line in file:
        splatline = line.split(';')
        tour_dict[splatline[0]]={'name':splatline[1],'status':splatline[2],'sport':splatline[3]}
    file.close()
    file = open(teamsfile,'r')
    for line in file:
        splatline = line.split(';')
        teams_dict[f'{splatline[0]};{splatline[1]}']={'name':splatline[2],'sport':splatline[3]}
    file.close()
    file = open(stafffile,'r')
    for line in file:
        splatline = line.split(';')
        staff_dict[f'{splatline[0]};{splatline[1]};{splatline[2]}']=splatline[3]
    file.close()
    file = open(playersfile,'r')
    for line in file:
        splatline = line.split(';')
        players_dict[f'{splatline[0]};{splatline[1]};{splatline[2]}']=splatline[3]
    file.close()

def data_out():
    """
    scrive dati sui file
    """
    file = open(toursfile,'w')
    for id in tour_dict:
        file.write(f'{id};{tour_dict[id]['name']};{tour_dict[id]['status']};{tour_dict[id]['sport']}')
    file.close()
    file = open(teamsfile,'w')
    for ids in teams_dict:
        file.write(f'{ids};{teams_dict[ids]['name']};{teams_dict[ids]['sport']}')
    file.close()
    file = open(stafffile,'w')
    for ids in staff_dict:
        file.write(f'{ids};{staff_dict[ids]}')
    file.close()
    file = open(playersfile,'w')
    for ids in players_dict:
        file.write(f'{ids};{players_dict[ids]}')
    file.close()
    


def add_tour():
    """
    aggiunge un torneo al db
    """
    data_in()
    name = input(name_question)       
    sport = input(sport_question)     
    id = len(tour_dict)
    tour_dict[id]['name']=name
    tour_dict[id]['status']='active'
    tour_dict[id]['sport']=sport    #FIXME: gestione ';'  <- dovrebbe essere risolto<-???
    data_out()

def list_tours(status):     #TODO: aggiungere filtraggio su sport
    """
    lista e ritorna tutti i tornei del tipo status
    """
    data_in()
    print(active_tour_message) #TODO: generalizzare
    returnable = dict()
    for id in tour_dict:
        if tour_dict[id]['status'] == status:
            returnable[id]=tour_dict[id]
            print(f'[{id}]-{tour_dict[id]['name']}-{tour_dict[id]['status']}-{tour_dict[id]['sport']}'.strip())
    return returnable

def set_tour(id,nome,status,sport):
    """
    modifica tornei esistenti
    se nome, status o sport sono 'keep' non vengono modificati
    """
    previous_name = tour_dict[id]['name']
    previous_status = tour_dict[id]['status']
    previous_sport = tour_dict[id]['sport']
    
    if nome =='keep':
        nome = previous_name
    if status =='keep':
        status = previous_status
    if sport =='keep':
        sport = previous_sport
    tour_dict[id]={'name':nome,'status':status,'sport':sport}  #FIXME: gestione ';' <- dovrebbbe essere risolto<-non so più quanto sia valido

    
def tour_exists(id):
    return (str(id) in tour_dict)
    

def add_team():
    return

def remove_team():
    return

def manage_team():
    return

