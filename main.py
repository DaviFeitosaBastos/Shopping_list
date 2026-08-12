from ui.menus import main_menu
from utils.validations import get_options
from rich import print
from router import router
from utils.logic import load_shopping_list



def main():
    while True:
        main_menu()
        choose = get_options()

        if choose not in [0, 1, 2, 3, 4]:
            continue
            
        # Save the choices
        action = router.get(choose)

        if action is None:
            print("[#c01c28]Invalid option, try again.")
            continue

        action()


if __name__ == "__main__":
    load_list = load_shopping_list("database/shopping_list.json")
    main()