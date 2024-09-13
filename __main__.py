import os

from messages import *
from paths import *
from updater import *

def main():
    clear_console()
    console_loop()

def clear_console():
    if os.name == 'nt':  # Per Windows
        os.system('cls')
    else:  # Per Linux e macOS
        os.system('clear')

def console_loop():
    command = "start"
    while command not in termination_commands :
        if command not in legal_commands:
            print (illegal_command_message)
        if command == 'update':
            update_pages()
        if command == 'add':
            add_tour()
        if command == 'list':
            list_tours('active')
        if command == 'close':
            deactivate_tour()
        if command == 'archive':
            list_tours('archived')
        if command == 'help':
            print(help_message)
        command = input(command_input_message).strip().lower()
    print(goodbye_message,end='')

def update_pages():
    print('wip')
    DEEZ_NUTS(CHATdir)


if __name__ == "__main__":
    main()