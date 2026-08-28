from ui.menus import add_items_menu, exit_program, show_items_menu, remove_items_menu, search_items_menu

def get_router():
    return {
        1: lambda: add_items_menu(),
        2: lambda: show_items_menu(),
        3: lambda: remove_items_menu(),
        4: lambda: search_items_menu(),
        0: exit_program
    }