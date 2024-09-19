# funzioni per aggiornare gli html

from paths import *
from mgmt import *


def update_pages():
    print('wip')
    DEEZ_NUTS(CHATdir)

def DEEZ_NUTS(directory):
    """
    single page update logic
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

def tours_print(indexfile,type):
    tours = list_tours(type)
    for line in tours:
        indexfile.write(f'<a href=".\\tornei\\{line.split(";")[0]}"><li>{line.split(';')[1]}</li></a>\n')