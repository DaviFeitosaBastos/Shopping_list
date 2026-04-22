import os
import platform
from time import sleep

shopping_list = []


def clear():
    """Clears the terminal"""
    os.system("cls" if platform.system() == "Windows" else "clear")


def pause(msg="Press Enter to continue..."):
    input(msg)


def get_int_input(prompt, min_val=None, max_val=None):
    """Safely gets an integer input with optional range validation"""
    while True:
        try:
            value = int(input(prompt))
            if min_val is not None and value < min_val:
                print(f"Value must be >= {min_val}")
                continue
            if max_val is not None and value > max_val:
                print(f"Value must be <= {max_val}")
                continue
            return value
        except ValueError:
            print("Invalid input. Please enter a number.")


def stay_or_back():
    """Ask user to stay or go back"""
    while True:
        clear()
        choice = get_int_input("Stay or go back? [1] Stay  [2] Back: ", 1, 2)

        if choice == 1:
            return True
        elif choice == 2:
            print("Returning...")
            sleep(1)
            return False


def menu():
    """Displays the main menu"""
    print("=== SHOPPING LIST ===")
    print("1 - Add item")
    print("2 - Show list")
    print("3 - Remove item")
    print("4 - Exit")


def add_item():
    """Adds items to the list"""
    while True:
        clear()
        item = input("Type your item: ").strip().upper()

        if not item:
            print("Item cannot be empty!")
        elif item in shopping_list:
            print(f"{item} is already in the list!")
        else:
            shopping_list.append(item)
            print(f"{item} added successfully!")

        sleep(1)

        if not stay_or_back():
            break


def show_list():
    """Displays the shopping list"""
    clear()
    print("=== YOUR LIST ===")

    if not shopping_list:
        print("Your list is empty!")
    else:
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")

    print("=================")
    pause()


def remove_item():
    """Removes an item from the list"""
    while True:
        clear()

        if not shopping_list:
            print("The list is empty!")
            sleep(2)
            break

        print("=== REMOVE ITEM ===")
        for i, item in enumerate(shopping_list, start=1):
            print(f"{i}. {item}")
        print("===================")

        choice = get_int_input(
            f"Choose item (1-{len(shopping_list)}) or 0 to cancel: ",
            0,
            len(shopping_list),
        )

        if choice == 0:
            print("Cancelled!")
            sleep(1)
            break

        removed = shopping_list.pop(choice - 1)
        print(f"{removed} removed successfully!")
        sleep(1)

        if not stay_or_back():
            break


def main():
    while True:
        clear()
        menu()

        choice = get_int_input("Choice: ", 1, 4)

        if choice == 1:
            add_item()
        elif choice == 2:
            show_list()
        elif choice == 3:
            remove_item()
        elif choice == 4:
            print("Goodbye!")
            sleep(1)
            break


if __name__ == "__main__":
    main()
