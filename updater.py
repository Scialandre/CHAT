from paths import *

def DEEZ_NUTS(directory):
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

def tours_print(indexfile,mode):
    tours = list_tours(mode)
    for line in tours:
        indexfile.write(f'<a href=".\\tornei\\{line.split(";")[0]}"><li>{line.split(';')[1]}</li></a>\n')