from time import sleep
from log.logging_setup import get_logger
from typing import cast, TypedDict
import os
import json

utils_dir = os.path.dirname(os.path.abspath(__file__))
list_path = "database/shopping_list.json"
log = get_logger(__name__)


class ShoppingItem(TypedDict):
    Id: int
    Item: str
    Amount: float
    Measures: str
    

def load_shopping_list(relative_path: str=list_path) -> list[ShoppingItem]:
    list_name = os.path.join(utils_dir, relative_path)
    
    try:
        with open(list_name, "r", encoding="utf-8") as f:
            return cast(list[ShoppingItem], json.load(f))
            
    except FileNotFoundError:
        with open(list_name, "w", encoding="utf-8") as f:
            json.dump([], f, indent=4)
            return cast(list[ShoppingItem], [])

 
def generate_id(shopping_list: list[ShoppingItem]):
    return len(shopping_list) + 1


def add_items_to_list(
    item_name: str, 
    quantity: float, 
    id_: int, measure: str, 
    shopping_list: list[ShoppingItem],
    path: str=list_path, 
):
    list_name = os.path.join(utils_dir, path)
    item: ShoppingItem = {
        "Id": id_,
        "Item": item_name,
        "Amount": quantity,
        "Measures": measure
    }
    shopping_list.append(item)
    
    with open(list_name, 'w', encoding="utf-8") as f:
        json.dump(shopping_list, f, indent=4)
    


def remove_items(id: int, shopping_list: list[ShoppingItem], path: str=list_path,) -> None:
    list_name = os.path.join(utils_dir, path)
    for index, item in enumerate(shopping_list):
        if item["Id"] == id:
            del shopping_list[index]
            break
    with open(list_name, 'w', encoding='utf-8') as f:
        json.dump(shopping_list, f, indent=4)
        

