from log.logging_setup import get_logger  
from rich.console import Console
from rich import print
from time import sleep


cs = Console()
log = get_logger(__name__)


def get_options() -> int | None:
    options = [0, 1, 2, 3, 4]
    
    while True:
        try:
            choose = int(cs.input("[#57e389]Select one of those: ").lower())

            if choose in options:
                return choose
            
        except ValueError:
            log.info("Invalid option try only integer")
            sleep(0.8)


def get_name() -> str:
    while True:
        
        name = cs.input("[#57e389]name: ").capitalize()
        
        if not name:
            print("[#c01c28]You can't let this field blank")
            sleep(0.8)
            continue
            
        return name
        
    
def get_amout() -> float:
    while True:
        try:
            amount = cs.input("[#57e389]Amount: ")
            return float(amount)
            
        except ValueError:
            log.error("Error letters are not allowed! try again")
            sleep(0.8)


def get_measures() -> str:
    MEASURES = ['kg', 'g', 'lb', 'oz', 'm', 'cm', 'mm', 'in', 'ft', 'l', 'ml']
    
    while True:
        measure = cs.input("[#57e389]Measure: ").lower()
        
        if measure == "":
            return "unit"
        
        if measure in MEASURES:
            return measure.capitalize()
        
        print(f"Invalid measure '{measure}'. Choose from: [#57e389]{', '.join(MEASURES)}")
        sleep(0.8)
            
                

        