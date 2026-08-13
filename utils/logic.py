from log.logging_setup import get_logger    
import os, json




# Variables default
utils_dir = os.path.dirname(os.path.abspath(__file__))
list_path = "database/shopping_list.json"
log = get_logger(__name__)


# Load the dictionary/make a new one when it doesn't exist yet
def load_shopping_list(relative_path: str):
    list_name = os.path.join(utils_dir, relative_path)
    
    try:
        with open(list_name, "r", encoding="utf-8") as f:
            return json.load(f)
            
    except FileNotFoundError:
        with open(list_name, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
            return []    
            
load_list = load_shopping_list(list_path)



def generate_id(shopping_list):
    seen = 1
    
    if shopping_list:
        for i, _ in enumerate(shopping_list, start=1):
            seen = i + 1
    return seen



def add_items_to_list(item_name, quantity, id_, measure,  shopping_list, relative_path):
    list_name = os.path.join(utils_dir, relative_path)

    items = {
        "Id": id_,
        "Item": item_name,
        "Amount": quantity,
        "Measures": measure,
    }

    shopping_list.append(items)

    with open(list_name, 'w', encoding="utf-8") as f:
        json.dump(shopping_list, f, indent=4)
        return shopping_list
    


