from messages import *

CHATdir = ".\\CHAT"

toursfile = CHATdir + "\\tours.txt"




def add_tour():
    name = input("Nome del torneo: ")       #FIXME:
    sport = input("Sport del torneo: ")     #FIXME:
    infile = open(toursfile,'r')
    lines = ""
    id_counter=0
    for line in infile:
        lines += line
        id_counter+=1
    lines+=f'\n{id_counter};{name};active;{sport}'  #FIXME: gestione ';'
    infile.close()
    outfile = open(toursfile,'w')
    outfile.write(lines)
    outfile.close()

def list_tours(status):
    print(active_tour_message)
    returnable = set()
    infile = open(toursfile,'r')
    for line in infile:
        splatline = line.strip().split(';')
        if splatline[2] == status:
            returnable.add(line)
            print(f'[{splatline[0]}]-{splatline[1]}-{splatline[3]}')
    infile.close()
    return returnable

def deactivate_tour():
    id = int(input("Id del torneo: "))       #FIXME: messaggio + controllo correttezza input
    infile = open(toursfile,'r')
    lines = ""
    id_counter=0
    for line in infile:
        if id_counter!=id:
            lines += line
        else:
            splatline = line.strip().split(';')
            lines+=f'{id_counter};{splatline[1]};archived;{splatline[3]}\n'  #FIXME: gestione ';'
        id_counter+=1
    
    infile.close()
    outfile = open(toursfile,'w')
    outfile.write(lines)
    outfile.close()
    
