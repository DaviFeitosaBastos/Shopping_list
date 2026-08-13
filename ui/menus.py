from rich.panel import Panel
from rich.console import Console
from rich import print
import subprocess
import sys
from time import sleep
from utils.logic import add_items_to_list, generate_id, load_list, list_path
from utils.validations import validate_ask_the_user, get_options, get_name, get_amout, get_measures





cs = Console()


def clear():
    subprocess.run(['clear']) if sys.platform == 'linux' else subprocess.run(['cls'])


def main_menu() -> None:
    clear()
    print(Panel("[#57e389]Options bellow:[/]\n"
                "[#57e389]1 🞄 Add items to the list[/]\n"
                "[#57e389]2 🞄 List the items saved\n"
                "[#57e389]3 🞄 Remove items to the list\n"
                "[#57e389]4 🞄 Search up\n"
                "[#57e389]0 🞄 Cose the app", 
                style='#10d610', 
                title='★ Shopping list ★',
                subtitle="Select here",
                width=35
    ))


def add_items_menu():
    while True:
        clear()
        print(Panel(
            "[#57e389]Would you like to add something?\n"
            "[#57e389]1 - to add\n"
            "[#57e389]0 - to return"
            ,style='#10d610',
            title='★ Adding items Menu ★',
            subtitle='Type here',
            width=40
        ))

        option = get_options()

        if option == 0:
            clear()
            break
            
        if option == 1:               
            clear()
            print(Panel(
                "[#57e389]Here you can name the item[/] [bold](e.g: Milk, Snacks)\n"
                "[#57e389]Obs. You can type lower either way"
                ,style='#10d610',
                title='★ Adding items Menu ★',
                subtitle='Type the name here',
                width=50
            ))
            name = get_name()
            if name is None:
                continue
            print(f"[#57e389]Name added {name}")
            sleep(0.8)
            clear()
            
            print(Panel(
                "[#57e389]Now type the amount and its measure (e.g: 15 ml etc...)[/]\n"
                "[#57e389]Obs. Only integer or float (e.g: 1, 1.5, 2.3, 4 etc..)\n\n"
                "If you don't type the measure it's going to be 'unit'",
                style='#10d610',
                title='★ Adding items Menu ★',
                subtitle='Type the amount/measure here',
                width=60
            ))
            
            amount = get_amout()
            measure = get_measures()
            print(f"[#57e389]The amount of {name} is {amount} {measure}")
            sleep(1)
            clear()

            add_items_to_list(name, amount, generate_id(load_list),measure ,load_list, list_path)
        

def show_items_menu():
    clear()
    print('[#57e389]⎯' * 40)
    
    if not load_list:
        print("[#c01c28]The list is empty")
        print('[#57e389]⎯' * 40)      
        
    for i, items in enumerate(load_list):       
        print(f'[#57e389]Item:[/] {i + 1} [green]|[/] [bold]- {items['Item']}[/] {items['Amount']} {items['Measures']}')
        print('[#57e389]⎯' * 40)      
        
    cs.input("[#57e389]Press enter to go back")

       
def exit_program() -> None | bool:
    while True:
        clear()
        print(Panel("Are you sure you want to leave?",title="Exit",style="#c01c28", width=35))

        user_input = validate_ask_the_user(cs.input("[#c01c28](Y)es or (N)ot: ").lower())

        if user_input:
            clear()
            exit()

        elif user_input is None:
            print("[#c01c28]Invalid input. Please type 'yes' or 'no'.")
            sleep(0.8)
            continue

        clear()
        return False
            

