from log.logging_setup import get_logger  
from typing import Literal
from rich.console import Console
from time import sleep

cs = Console()
log = get_logger(__name__)


def get_options() -> int | None:
    options = [x for x in range(11)]
    
    while True:
        try:
            choose = int(cs.input("[#57e389]Select one of those: ").lower())

            if choose in options:
                return choose
            
        except ValueError:
            log.info("Invalid option try only integer")
            sleep(0.8)
            return None


def get_name() -> str | None:
    name = cs.input("[#57e389]Write the name right here: ").capitalize()
    if isinstance(name, str):
        return name
    else:
        return None

    
def get_amout() -> float:
    while True:
        try:
            amount = cs.input("[#57e389]How much/many would you like: ")
            return float(amount)
            
        except ValueError:
            log.error("Error letters are not allowed! try again")
            sleep(0.8)


def get_measures(measures):
    
    while True:
        try:           
            measure = cs.input("[#57e389]What kind of measures: ").lower()

            if measure == "":
                return "Unity"
            
            if measure in measures:
                return measure
                
            raise ValueError(f"This measure doesn't exist '{measure}'")
                
        except ValueError:
            log.error("Error letters are not allowed! try again")
            sleep(0.8)
            
                
def validate_ask_the_user(prompt: str) -> Literal[True] | Literal[False] | None:
    yes = ['yes', 'y']
    no = ['not', 'no', 'n']

    if prompt in yes:
        return True
        
    elif prompt in no:
        return False
        
    return None  
        