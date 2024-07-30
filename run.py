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

name = input(f"{PURPLE}Please enter your name here:\n")
print(f"{CYAN}Hey {name.title()}! Let's get started!")

def menu():
    """
    Gives options to read Rules of game or Start game
    Calls for function depending on choice made
    """

    print(f"{PURPLE}Main Menu:\n Choose from the following options:\n")
    print(f"{CYAN} 1. View Game Rules\n")
    print(f"{YELLOW} 2. Start the game\n")

    choice = int(input("Enter your choice:\n"))

    while choice > 2:
        choice = int(input(f"{PURPLE}Please enter number 1 or 2:\n"))

    if choice == 1:
        get_rules()
    elif choice == 2:
        start_game()
        

# Display Rules
def get_rules():
    """
    Prints rules of the game to terminal if user input is 1
    from main menu
    """
    print(f"{PURPLE}Winning Rules of the game are as follows:\n"
        + f"{CYAN}Rock vs Paper --> Paper wins\n"
        + f"{YELLOW}Rock vs Scissors --> Rock wins\n"
        + f"{CYAN}Scissors vs Paper --> Scissors Wins\n")

player_score = 0
comp_score = 0
num_games = 0


# Main Game Function
def start_game():
    """
    Main Game Play against computer. User inputs number corresponding
    to 3 options, computer randomly chooses an option 
    and compares to see who wins
    """
while num_games < 5:
    
    print(f"{YELLOW}Please choose an option from the following:\n")
    print(f"{CYAN}\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n")

    option = int(input(f"{PURPLE}Choose 1,2 or 3:\n"))

    while option > 3 or option < 1:
        option = int(input(f"{PURPLE}Invalid number, Please choose 1,2 or 3:\n"))

    if option == 1:
        user_option = "Rock"
    elif option == 2:
        user_option = "Paper"
    else:
        user_option = "Scissors"


    print("Rock, Paper, Scissors....")
    print("SHOOT!!")
    print(f"{CYAN}{name.title()} : {user_option}")

#Computer chooses random selection
    computer = random.randint(1,3)

    if computer == 1:
        comp_option = "Rock"
    elif computer == 2:
        comp_option = "Paper"
    else:
        comp_option = "Scissors"

    print(f"{YELLOW}Computer: {comp_option}")
    num_games += 1

    #Compare both answers to determine the winner
    if user_option == comp_option:
        print("It's a tie!")
    elif user_option == "Paper" and comp_option == "Rock":
        print(f"{name.title()}, you win!")
        player_score += 1
    elif user_option == "Rock" and comp_option == "Scissors":
        print(f"{name.title()}, you win!")
        player_score += 1
    elif user_option == "Scissors" and comp_option == "Paper":
        print(f"{name.title()}, you win!")
        player_score += 1
    else:
        print(f"Sorry {name.title()}, you lose!")
        comp_score += 1
    

print(f"\n{name.title()}: {player_score} | Computer: {comp_score}")
print("===============================")
print("")
if num_games == 5:
    start_game=False

if player_score == comp_score:
  print("It's a Draw!!")
elif player_score > comp_score:
  print(f"Congrats {name.title()}, You won the game!!")
else:
  print(f"Oops Computer won the game!! Better luck next time {name.title()}!") 

# Ask user to play again
if not input(f"Would you like to play again? (Type y/n)\n").lower()=="y":
        start_game = False
        print("Thanks for playing!")  
    


def main():
    menu()
    start_game()

main()
