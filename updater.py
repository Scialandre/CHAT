# funzioni per aggiornare gli html
import os
import shutil

from paths import *
from htmlLineTemplates import *
from messages import *

from mgmt import *
from stats import *


def update_pages():
    print('wip')
    main_page_UD(CHATdir)
    update_tour_stats()
    for id in tours_dict:
        tour_page_UD(f'{tours_dir}\\{id}',id)
    for id in teams_dict:
        team_page_UD(f'{teams_dir}\\{id}',id)

def main_page_UD(directory):
    """
    main page update logic
    """
    indexfile = open(directory+'\\index.html','w')
    templatefile = open(directory+'\\template.html','r')

    for line in templatefile:
        if not line.strip().startswith('#'):
            indexfile.write(line)
        else:
            if line.strip().startswith('#active-tours'):
                tours_print(indexfile,'active')
            if line.strip().startswith('#archived-tours'):
                tours_print(indexfile,'archived')

            
    indexfile.close()
    templatefile.close()

def tour_page_UD(directory,id):
    """
    tour page update logic
    """
    if not os.path.isdir(directory):
        shutil.copytree(tours_template_dir,directory)       #crea la directory in caso in cui non esista

    indexfile = open(directory+'\\index.html','w')
    templatefile = open(tours_template_file,'r')

    for line in templatefile:
        if not line.strip().startswith('#'):
            indexfile.write(line)
        else:
            if line.strip().startswith('#page-title'):
                indexfile.write(page_title.replace('#TITOLO#',tours_dict[id]['name']))
            if line.strip().startswith('#ranking-header'):
                indexfile.write(ranking_header.replace('#NOME-TORNEO#',tours_dict[id]['name']))
            if line.strip().startswith('#rankings-table-body'):
                indexfile.write(rank_table_body_gen(id))

            
    indexfile.close()
    templatefile.close()

def team_page_UD(directory,id):
    """
    team page update logic
    """
    if not os.path.isdir(directory):
        shutil.copytree(teams_template_dir,directory)       #crea la directory in caso in cui non esista

    indexfile = open(directory+'\\index.html','w')
    templatefile = open(teams_template_file,'r')

    for line in templatefile:
        if not line.strip().startswith('#'):
            indexfile.write(line)
        else:
            if line.strip().startswith('#page-title'):
                indexfile.write(page_title.replace('#TITOLO#',teams_dict[id]['name']))
            if line.strip().startswith('#back-button'):
                try:
                    indexfile.write(team_page_back_button.replace('#TOUR-ID',teams_dict[id]['tour_id']).replace('#TOUR-NAME#',tours_dict[teams_dict[id]['tour_id']]['name']))
                except KeyError as ke:
                    pass
            if line.strip().startswith('#name-header'):
                indexfile.write(f'<h1>{teams_dict[id]['name']}</h1>')
            if line.strip().startswith('#team-logo'):
                indexfile.write(team_image_or_logo.replace('#FOLDER#','team-logo').replace('#TEAM-ID#',id))
            if line.strip().startswith('#staff-list'):
                indexfile.write(staff_list_gen(id))
            if line.strip().startswith('#players-list'):
                indexfile.write(players_list_gen(id))
            if line.strip().startswith('#team-image'):
                indexfile.write(team_image_or_logo.replace('#FOLDER#','team-image').replace('#TEAM-ID#',id))
            
    indexfile.close()
    templatefile.close()

def tours_print(indexfile,type):
    tours = list_tours(type)
    for id in tours:
        indexfile.write(tour_list_entry.replace('#TOUR-ID#',id).replace('#NOME#',tours[id]['name']))

def rank_table_body_gen(tour_id):
    result = ''
    teams =dict(sorted(get_teams_by_tour(str(tour_id)).items(), key=lambda x: (x[1]['rank_score'], x[1]['points_out']), reverse=True)) 
    rank =1
    


    for id in teams:
        result+= team_table_entry.replace('#TEAM-ID#',teams[id]['team_id']).replace('#RANK#',str(rank)).replace('#NOME#',teams[id]['name']).replace('#GAMES-PLAYED#',str(int(teams[id]['win'])+int(teams[id]['draw'])+int(teams[id]['lose']))).replace('#GAMES-WON#',teams[id]['win']).replace('#GAMES-DRAW#',teams[id]['draw']).replace('#GAMES-LOST#',teams[id]['lose']).replace('#PUNTI-SEGNATI#',teams[id]['points_out']).replace('#PUNTI-SUBITI#',teams[id]['points_in']).replace('#RANK-SCORE#',teams[id]['rank_score'])
        rank +=1
    return result

def staff_list_gen(team_id):
    result = ''
    for ids in staff_dict:      #TODO: restructure staff e player
        splat = ids.split(';')
        if splat[1] == str(team_id):
            result += staff_list_entry.replace('#NOME#',staff_dict[ids])


    return result.strip('\n')

def players_list_gen(team_id):
    result = ''
    for ids in players_dict:      #TODO: restructure staff e player
        splat = ids.split(';')
        if splat[1] == str(team_id):
            result += player_list_entry.replace('#MAGLIA#',splat[2]).replace('#NOME#',players_dict[ids])

    return result.strip('\n')