import gspread
from google.oauth2.service_account import Credentials
import random
import time

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file("creds.json")
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open("RockPaperScissors")

# Connect to Google sheets
scores = SHEET.worksheet("scores")

# colour codes
CYAN = '\033[36m'
YELLOW = '\033[93m'
RED = '\033[0;31m'
MAGENTA = '\u001b[35m'
WHITE = '\u001b[37m'

# banner for game
banner = f"""{MAGENTA}
   ___           __     ___                      ____    _
  / _ \___  ____/ /__  / _ \___ ____  ___ ____  / __/___(_)__ ______  _______
 / , _/ _ \/ __/  '_/ / ___/ _ `/ _ \/ -_) __/ _\ \/ __/ (_-<(_-< _ \/ __(_-<
/_/|_|\___/\__/_/\_\ /_/   \_,_/ .__/\__/_/   /___/\__/_/___/___|___/_/ /___/
                              /_/
"""
print(banner)

name = input(f"{MAGENTA}Please enter your name here:\n")
print(f"{CYAN}Hey {name.title()}! Let's get started!")


def menu():
    """
    Give options to read Rules of game, Start game or see Scores.

    Call for function depending on choice made
    """

    print(f"{MAGENTA}\n Main Menu:\n Choose from the following options:\n")
    print(f"{CYAN} 1. View Game Rules\n")
    print(f"{CYAN} 2. Start the game\n")
    print(f"{CYAN} 3. See Score Sheet\n")

    # Check user inputs a number
    choice = input(f"{MAGENTA}Enter your choice here:\n")
    if choice.isdigit() and choice == "1":
        get_rules()
    elif choice.isdigit() and choice == "2":
        start_game()
    elif choice.isdigit() and choice == "3":
        # print(data)
        get_scoresheet()
        menu()
    else:
        print(f"{RED}Please enter number 1 or 2:\n")
        menu()


def get_scoresheet():
    """Return data from Google Sheets.

    Display list of names and scores that have been saved
    in Google Sheets
    """
    scores = SHEET.worksheet("scores")
    column = []
    for ind in range(1 , 3):
        column = scores.col_values(ind)
        column.append(column)
        print(f"{CYAN}Column {ind}:", column)
        scoreboard = zip(range(0), range(1), range(2))
        print("\nScoreboard:")
        for name, player_score, comp_score in scoreboard:
            print(f"{name}:{player_score}:{comp_score}")
    

    
    # Display Rules
def get_rules():
    """
    Print rules of the game to terminal.

    Call when user inputs is 1 from main menu
    """
    print(f"{MAGENTA}\n**Winning Rules of the game are as follows: **\n"
            + f"{CYAN}Rock vs Paper --> Paper wins\n"
            + f"{YELLOW}Rock vs Scissors --> Rock wins\n"
            + f"{CYAN}Scissors vs Paper --> Scissors Wins\n")
    return menu()

    # All scores start at zero - Global Variables
player_score = 0
comp_score = 0
num_games = 0

    # Main Game Function
def start_game():
    """
    Main Game Play against computer.

    User inputs number corresponding to 3 options, computer randomly
    chooses an option and compares to see who wins
    """
    global num_games
    global player_score
    global comp_score

    player_score = 0
    comp_score = 0
    num_games = 1

    while num_games < 6:
    # Get user option and check it is a number
        time.sleep(1)
        print(f"{CYAN}We're going to play five rounds, Good Luck!")
        print(f'{MAGENTA}\n******************* ROUND',num_games,'*******************')       
        print(f"\n{YELLOW}Please choose an option from the following:\n")
        print(f"{CYAN}\n 1 - Rock\n 2 - Paper\n 3 - Scissors\n")

        option = input(f"{MAGENTA}Choose 1,2 or 3:\n")
        if option.isdigit() and option == "1":
            user_option = "Rock"
        elif option.isdigit() and option == "2":
            user_option = "Paper"
        elif option.isdigit() and option == "3":
            user_option = "Scissors"
        else:
            print(f"{RED}**Please choose number 1,2 or 3\n")
            # menu()

    # Print user option
        print("Rock, Paper, Scissors....")
        time.sleep(1)
        print(f"\n{YELLOW}    SHOOT!!")
        print(f"\n{CYAN}{name.title()} : {user_option}")

    # Computer chooses random selection
        computer = random.randint(1,3)

        if computer == 1:
            comp_option = "Rock"
        elif computer == 2:
            comp_option = "Paper"
        else:
            comp_option = "Scissors"

        print(f"{YELLOW}Computer: {comp_option}\n")
        num_games += 1

    # Compare both answers to determine the winner
        if user_option == comp_option:
            time.sleep(1)
            print("It's a tie!")
        elif user_option == "Paper" and comp_option == "Rock":
            time.sleep(1)
            print(f"{name.title()}, you win this round!")
            player_score += 1
        elif user_option == "Rock" and comp_option == "Scissors":
            time.sleep(1)
            print(f"{name.title()}, you win this round!")
            player_score += 1
        elif user_option == "Scissors" and comp_option == "Paper":
            time.sleep(1)
            print(f"{name.title()}, you win this round!")
            player_score += 1
        else:
            time.sleep(1)
            print(f"Sorry {name.title()}, you lose this round!")
            comp_score += 1

        # Print Score Board
        print(f"\n{CYAN}*******************************")
        print("")
        print(f"{name.title()}: {player_score} | Computer: {comp_score}")
        print("===============================")
        print("")
        if num_games == 6:
            get_score()


def get_score():
    """
    Print win or lose message.

    Get final score from five rounds and ask user if they would like to 
    play again
    """
    if player_score == comp_score:
        print("It's a Draw!!")
    elif player_score > comp_score:
        print(f"*.*.*Congrats {name.title()}, You won the game!!*.*.*\n")
    else:
        print(f"Oh No! Computer won the game!! Better luck next time{name.title()}!") 
    # Ask user to play again
    while True:
        user_input = input(f"{MAGENTA}Would you like to play again? (yes/no): \n")
        if user_input.lower() in ["yes", "y"]:
            print("Ok, Awesome!")
            start_game()
        elif user_input.lower() in ["no", "n"]:
            print(f"\n{YELLOW}Ok, Thanks for playing!")
            allow_score = input(f"\n{CYAN}Would you like to add your score to the Score Sheet?(yes/no):\n")
            if allow_score.lower() in ["yes", "y"]:
                print("Ok, Super, we'll add it now")
                update_score()
            elif allow_score.lower() in ["no", "n"]:
                print("Cool...See you again soon!")
            else:
                print(f"{RED}**Invalid input. Please enter yes/no.")
            menu()
        else:
            print(f"{RED}**Invalid input. Please enter yes/no.")


def update_score():
    """
    Update Google Sheets with name and score.

    When users agrees to input name and score, update sheet
    """
    global name
    global player_score
    global comp_score
    time.sleep(1)
    print("Updating score sheet...")
    scores_worksheet = SHEET.worksheet("scores")
    scores.append_row([name, player_score,comp_score])
    time.sleep(2)
    print("Score worksheet updated successfully\n")


# Put all functions into one
def main():
    """
    Run all program functions
    """
    menu()
    start_game()
    get_score()
    get_new_score()
    update_score()
    #data = scores.get_all_values()


main()
