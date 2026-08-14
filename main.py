from ui.menus import main_menu
from utils.validations import get_options
from router import router





def main():
    while True:
        main_menu()
        
        choose = get_options()
            
        # Save the choices
        action = router[choose]

        _ = action()


if __name__ == "__main__":
    main()