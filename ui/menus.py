from rich.panel import Panel
from rich.console import Console
from rich.live import Live
from rich.table import Table
from rich import print
import subprocess
import sys
from time import sleep
from utils.logic import add_items_to_list, generate_id, load_shopping_list, remove_items
from utils.validations import get_options, get_name, get_amout, get_measures, get_id





cs = Console()
list_loaded = load_shopping_list()

def clear():
    subprocess.run(['clear']) if sys.platform == 'linux' else subprocess.run(['cls'])


def main_menu() -> None:
    clear()
    print(Panel("[#57e389]Options bellow:[/]\n"+
                "[#57e389]1 🞄 Add items to the list[/]\n"+
                "[#57e389]2 🞄 List the items saved\n"+
                "[#57e389]3 🞄 Remove items to the list\n"+
                "[#57e389]4 🞄 Search up\n"+
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
            "[#57e389]Would you like to add something?\n"+
            "[#57e389]1 - to add\n"+
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
                "[#57e389]Here you can name the item[/] [bold](e.g: Milk, Snacks)\n"+
                "[#57e389]Obs. You can type lower either way",
                style='#10d610',
                title='★ Adding items Menu ★',
                subtitle='Type the name here',
                width=50
            ))
            name = get_name()
            print(f"[#57e389]Name added {name}")
            sleep(0.8)
            clear()
            
            print(Panel(
                "[#57e389]Now type the amount and its measure (e.g: 15 ml etc...)[/]\n"+
                "[#57e389]Obs. Only integer or float (e.g: 1, 1.5, 2.3, 4 etc..)\n\n"+
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

            add_items_to_list(
                name, 
                amount, 
                generate_id(list_loaded),
                measure , 
                list_loaded
            )
            
        
def show_items_menu() -> None:
    clear()
    print('[#57e389]⎯' * 40)
    
    if not list_loaded:
        print("[#c01c28]The list is empty")
        print('[#57e389]⎯' * 40)      
        
    for items in list_loaded:       
        print(f'[#57e389]Item:[/] {items['Id']} [green]|[/] [bold]- {items['Item']}[/] {items['Amount']} {items['Measures']}')
        print('[#57e389]⎯' * 40)      
        
    _ = cs.input("[#57e389]Press enter to go back")


def remove_items_menu():
    while True:
        clear()
        print(Panel(
            "Would you like to remove any item?\n"+
            "1 - to remove\n"+
            "0 - to return",
            style='#57e389',
            title='[#57e389]★ Remove items ★',
            subtitle='[#57e389]select here',
            width=39
        ))
        choice = get_options()
    
        if choice == 0:
            clear()
            break
            
        elif choice == 1:
            clear()
            if not list_loaded:
                print(Panel("[#c01c28]The list is empty", 
                    style='#c01c28',
                    title='[#c01c28]★ Remove items ★',
                    width=40
                ))
                _ = cs.input("[#c01c28]Press enter to return")
                continue
            
            # CREATE TABLE HERE, FRESH EACH TIME
            table = Table()
            table.style='#57e389'
            table.add_column("[#57e389]Id")
            table.add_column("[#57e389]Item")
            
            with Live(table, refresh_per_second=4):
                for item in list_loaded:
                    sleep(0.1)
                    table.add_row(f"[bold blue]{item['Id']}", f"{item['Item']}")
                    
            id = get_id()
            remove_items(id, list_loaded)
            
            print("[#57e389]Deleted with success")
            sleep(0.8)
        
       
def exit_program() -> None | bool:
    yes = ['yes', 'y']
    no = ['no', 'n']
    while True:
        clear()
        print(Panel("Are you sure you want to leave?",title="Exit",style="#c01c28", width=35, subtitle='Type here'))

        user_input = cs.input("[#c01c28]Type Yes or No: ").lower()

        if user_input in yes:
            clear()
            exit()

        elif user_input in no:
            clear()
            return False
            
        print("[#c01c28]Invalid input. Please type 'yes' or 'no'.")
        sleep(0.8)
        continue

        
            

