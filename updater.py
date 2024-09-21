# funzioni per aggiornare gli html
import os
import shutil

from paths import *
from mgmt import *
from stats import *


def update_pages():
    print('wip')
    main_page_UD(CHATdir)
    for id in tours_dict:
        tour_page_UD(f'{tours_dir}\\{id}',id)

def main_page_UD(directory):       #TODO: separare la logica per tipo di pagina <- coservando questa per la  main page
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
    update_tour_stats()
    if not os.path.isdir(directory):
        shutil.copytree(tours_template_dir,directory)       #crea la directory in caso in cui non esista

    indexfile = open(directory+'\\index.html','w')
    templatefile = open(tours_template_file,'r')

    for line in templatefile:
        if not line.strip().startswith('#'):
            indexfile.write(line)
        else:
            if line.strip().startswith('#page-title'):
                indexfile.write(f"<title>{tours_dict[id]['name']}</title>")
            if line.strip().startswith('#ranking-header'):
                indexfile.write(f"<h1>Classifica {tours_dict[id]['name']}</h1>")
            if line.strip().startswith('#rankings-table-body'):
                indexfile.write(rank_table_body_gen(id))

            
    indexfile.close()
    templatefile.close()

def tours_print(indexfile,type):
    tours = list_tours(type)
    for id in tours:
        indexfile.write(f'<a href=".\\tornei\\{id}"><li>{tours[id]['name']}</li></a>\n')

def rank_table_body_gen(tour_id):      # TODO: spostare template e modificarlo con replace
    result = ''
    teams = get_teams_by_tour(str(tour_id))
    rank =1
    
    #TODO:ordinare in base alla classifica

    for id in teams:
        result+= f' <tr onclick=\"goToTeamPage(\'../../squadre/{tour_id}-{teams[id]['team_id']}\')\"><td>{rank}</td><td>{teams[id]['name']}</td><td>{int(teams[id]['win'])+int(teams[id]['draw'])+int(teams[id]['lose'])}</td><td>{teams[id]['win']}</td><td>{teams[id]['draw']}</td><td>{teams[id]['lose']}</td><td>{teams[id]['points-out']}</td><td>{teams[id]['points-in']}</td><td>{teams[id]['rank-score']}</td></tr>'
        rank +=1
    return result