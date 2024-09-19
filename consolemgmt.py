import os

from messages import *
from paths import *

from updater import *
from mgmt import *
from backupFun import *


termination_commands = {'end','stop'}
legal_commands = {'start','update','help','add','list','archive','close','mgmt','backup'}

active_tour_id = -1



def clear_console():
    if os.name == 'nt':  # Per Windows
        os.system('cls')
    else:  # Per Linux e macOS
        os.system('clear')


def console_loop():
    command = "start"
    clear_console()
    while command not in termination_commands :
        if command not in legal_commands:
            print (illegal_command_message)
        if command == 'update':
            update_pages()
        if command == 'backup':
            create_backup(db_dir,backup_dir)
        if command == 'add':
            add_tour()
        if command == 'list':
            list_tours('active')
        if command == 'close':
            id = input(id_question)
            set_tour(id,'keep','archived','keep')
        if command == 'archive':
            list_tours('archived')
        if command == 'mgmt':
            list_tours('active')
            mgmt_console_loop(mgmt_console_loop_msg,'start')
        if command == 'help':
            print(help_message)

        command = input(command_input_message).strip().lower()
    print(goodbye_message,end='')



def mgmt_console_loop(input_msg,level):
    global active_tour_id
    command = 'start'

    if level =='start':
        id = input(input_msg+' '+id_question)
        if tour_exists(int(id)):
            active_tour_id = int(id)
            mgmt_console_loop(input_msg+f"{id}-{tour_dict[id]['name']}>",'tour')
        else:
            print(wrong_tour_id)
            return

    if level == 'tour':
        
        while command not in termination_commands:
            #if command == 'modify':


            if command == 'back':
                return
            command = input(input_msg).strip().lower()