# menu_driven_program_functions.py

"""
This module implements a simple menu-driven program that allows users to 
choose from a list of options. Based on the user's choice, different 
actions are performed.
"""

def display_menu():
    """
    Display a menu with options for the user.
    """
    print("1. Option 1")
    print("2. Option 2")
    print("3. Exit")


def process_choice(choice: int):
    """
    Process the user's menu choice.
    
    Args:
        choice (int): The user's menu choice.
    """
    if choice == 1:
        print("You chose Option 1")
    elif choice == 2:
        print("You chose Option 2")
    elif choice == 3:
        print("Exiting...")
    else:
        print("Invalid choice")


def main():
    """
    Main function that runs the menu-driven program.
    """
    while True:
        display_menu()
        try:
            choice = int(input("Enter your choice: "))
            if choice == 3:
                process_choice(choice)
                break  # Exiting the loop
            # Removed unnecessary `else` after `break`
            process_choice(choice)  # If not exit, continue processing the choice
        except ValueError:
            print("Please enter a valid integer.")


# If the script is being run directly, call the main function
if __name__ == "__main__":
    main()
