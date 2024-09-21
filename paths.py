# path dei file

from messages import *

CHATdir = ".\\CHAT"

db_dir = CHATdir+"\\data-tables"
backup_dir = CHATdir+"\\backups"

tours_dir = CHATdir+"\\tornei"      #separare squadre e tornei
tours_template_dir = tours_dir + "\\template"

teams_dir = CHATdir+"\\squadre"
teams_template_dir = teams_dir +"\\template"

toursfile = db_dir + "\\tours.txt"
teamsfile = db_dir + "\\teams.txt"
stafffile = db_dir + "\\staff.txt"
playersfile = db_dir + "\\players.txt"

tours_template_file = tours_template_dir + "\\index.html"   # <- si chiama index per conservare il nome quando viene copiato