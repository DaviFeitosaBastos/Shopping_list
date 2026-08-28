import json
import os
from json.decoder import JSONDecodeError
from typing import TypedDict, cast

from log.logging_setup import get_logger

utils_dir = os.path.dirname(os.path.abspath(__file__))
list_path = "database/shopping_list.json"
log = get_logger(__name__)


class ShoppingItem(TypedDict):
    Id: int
    Item: str
    Amount: float
    Measures: str


class FileHandler:
    absolute_path: str = os.path.dirname(os.path.abspath(__file__))
    
    def __init__(self, filename: str) -> None:
        self.file:str = os.path.join(self.absolute_path, f"database/{filename}")
    
    def load_files(self):
        try:
            with open(self.file, "r", encoding="utf-8") as f:
                return cast(list[ShoppingItem], json.load(f))
                
        except (FileNotFoundError, JSONDecodeError):
            with open(self.file, "w", encoding="utf-8") as f:
                json.dump([], f, indent=4)
                return cast(list[ShoppingItem], [])

    def generate_id(self):
        return len(self.load_files()) + 1

    def add_item_to_list(
        self,
        item_name: str,
        quantity: float,
        measure: str
    ):
        shopping_list = self.load_files()
        
        item: ShoppingItem = {
            "Id": self.generate_id(),
            "Item": item_name,
            "Amount": quantity,
            "Measures": measure
        }

        shopping_list.append(item)

        with open(self.file, 'w', encoding='utf8') as f:
            json.dump(shopping_list, f, indent=2)

    def remove_items(self, id: int):
        shopping_list = self.load_files()

        for index, item in enumerate(shopping_list):
            if item["Id"] == id:
                del shopping_list[index]
                break
                
        with open(self.file, 'w', encoding='utf-8') as f:
            json.dump(shopping_list, f, indent=4)
    



