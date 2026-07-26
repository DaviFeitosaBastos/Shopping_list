from rich.panel import Panel
from rich.console import Console
from rich import print
import os, sys
from time import sleep
from utils.logic import add_items_to_list, generate_id, load_list, list_path
from utils.validations import validate_ask_the_user, get_options, get_name, get_amout

cs = Console()

def clear():
    os.system("clear") if sys.platform == 'linux' else os.system('cls')

def main_menu() -> None:
    clear()
    print(Panel(f"[#57e389]Options bellow:[/]\n"
                f"[#57e389]1 🞄 Add items to the list[/]\n"
                f"[#57e389]2 🞄 List the items saved\n"
                f"[#57e389]3 🞄 Remove items to the list\n"
                f"[#57e389]4 🞄 Search up\n"
                f"[#57e389]0 🞄 Cose the app", 
                style='#10d610', 
                title='★ Shopping list ★',
                subtitle="Select here",
                width=35
    ))
    
def add_items_menu():
    while True:
        clear()
        print(Panel(
                f"[#57e389]Would you like to add an item?\n"
                f"[#57e389]1 -> Yes\n" 
                f"[#57e389]2 -> No", 
                style='#10d610',
                title="★ Add items ★",
                subtitle="Informations here",
                width=40,
        ))
        choice = get_options()
        if choice == 1:
            clear()
            name = get_name()
            amount = get_amout()
            add_items_to_list(name, amount, generate_id(load_list), load_list, list_path)    

        elif choice == 2:
            break
        else:
            print("[#c01c28]Invalid input try only 1 or 2")



def exit_program() -> None | bool:
    while True:
        clear()
        print(Panel(f"Are you sure you want to leave?",title="Exit",style="#c01c28",))

        user_input = validate_ask_the_user(cs.input("[#c01c28](Y)es or (N)ot: ").lower())

        if user_input:
            clear()
            exit()

        elif user_input is None:
            print("[#c01c28]Invalid input. Please type 'yes' or 'no'.")
            sleep(0.8)

        else: 
            clear()
            print('Returning!')
            sleep(0.8)
            return False
            

