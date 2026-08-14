from ui.menus import add_items_menu, exit_program, show_items_menu, remove_items_menu, search_items_menu
from utils.logic import load_shopping_list

def get_router():
    shopping_list = load_shopping_list()
    return {
        1: lambda: add_items_menu(shopping_list),
        2: lambda: show_items_menu(shopping_list),
        3: lambda: remove_items_menu(shopping_list),
        4: lambda: search_items_menu(shopping_list),
        0: exit_program
    }