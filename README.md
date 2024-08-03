# Rock, Paper, Scissors
A bit about the game here
Live site can be found [Here](address)

## Contents:
[UX(User Experience)](UX)  
[Flow Chart](Flow)  
[Design](Design)
## UX(User Experience)
### First time User Goals:
As a first time user, I would like to:
1. Have clear instructions on what I need to do
2. Choose an option, and that option display as expected
3. Learn or remind myself of the rules
4. Go straight to playing the game if I already know the rules
5. Be able to see a tally of my score
6. Be able to play again or exit the game if I am finished

### Developer Goals:
As a developer, I would like:
1. To make the game more personal, by asking the user's name
2. Make the options clear and consise for the user to choose from
3. Have the rules as an option, so players can go straight to gameplay should they already be familiar with the rules
4. Give the computer a bit of personality for better user experience ie.The computer will call the user by their name

### Return User Goals:
As a return user, I would like to:
1. Add some here

## Flow Chart
I used a flow chart to visualise the functions I would need to use, and to try to predict any user/computer errors before they arise.
Enter screenshot here

## Design
Design ideas here
Banner using

## Features
Welcome screenshot
Add name
Rules Page
Game Scores after each
### Future Features
ideas here

## Bugs(Call this something else?)
1. The first bug I came across was on the Banner I created. I kept getting an "invalid escape sequence" and my code would not run.  I found the answer on Stack Overview which suggested I use 2 trailing backslashes where the issue was and that seemed to fix it.
2. On the first go, the code was jumping straight into the game, without giving the menu option - with the help of my tutor, we figured that it was because my variables num_games, player_score and comp_score, could not be accessed until I made them Global, this fixed the issue.
3. Using int(input), I wrongly presumed the user would input an integer when asked. During testing, when I put in an alpha letter, my game crashed due to lack of input validation and error handling. To solve this, I used the isdigit() method and displayed a message to the user.

## Technologies Used
1. Python
2. Github
3. Gitpod
4. Heroku
5.

## Testing
table here

## Validation
pep8

## Deployment
I deployed the project through Heroku. The project was developed on Gitpod and committed and pushed to Github. Heroku automatically updates once deployed.

The Deployment Process is as follows:
1. Log into Github and open the repo to be deployed
2. Log into Heroku etc etc

## Credits
Mentor
tutors
sites

## Libraries Used
random
gspread etc etc