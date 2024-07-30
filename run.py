import random

# colour codes
PURPLE = '\033[0;35m'
CYAN = "\033[36m"
YELLOW = "\033[93m"

# banner for game
banner = f"""{PURPLE} 


 
   ____            _       ____                          ____       _                        
 |  _ \ ___   ___| | __  |  _ \ __ _ _ __   ___ _ __   / ___|  ___(_)___ ___  ___  _ __ ___ 
 | |_) / _ \ / __| |/ /  | |_) / _` | '_ \ / _ \ '__|  \___ \ / __| / __/ __|/ _ \| '__/ __|
 |  _ < (_) | (__|   <   |  __/ (_| | |_) |  __/ |      ___) | (__| \__ \__ \ (_) | |  \__ \\
 |_| \_\___/ \___|_|\_\  |_|   \__,_| .__/ \___|_|     |____/ \___|_|___/___/\___/|_|  |___/
                                    |_|                                                     
"""

print(banner)

def menu():
    """
    Gives options to read Rules of game or Start game
    Calls for function depending on choice made
    """
    print(f"{PURPLE}Main Menu:\n Choose from the following options:\n")
    print(f"{CYAN} 1. View Game Rules\n")
    print(f"{YELLOW} 2. Start the game\n")

    choice = int(input("Enter your choice:")(choice))

    if choice == 1:
        get_rules()
    elif choice == 2:
        start_game()

def get_rules():
    """
    Prints rules of the game to terminal if user input is 1
    from main menu
    """
    print("Winning Rules of the game are as follows:\n"
        + "Rock vs Paper --> Paper wins\n"
        + "Rock vs Scissors --> Rock wins\n"
        + "Scissors vs Paper --> Scissors Wins\n")







menu()
get_rules()
