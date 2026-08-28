from router import get_router
from ui.menus import main_menu
from utils.validations import get_options


def main():
    router = get_router()
    while True:
        main_menu()
        
        choose = get_options()
            
        action = router.get(choose)
        if action:
            _ = action()

if __name__ == "__main__":
    main()