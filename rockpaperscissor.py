
# import for the random.choice() method
import random

### Main method to call the interface() method

def main():

    # keeps track of both the user and the computer's score
    playerScore = 0
    computerScore = 0

    # loop structure to re-run the program if the user wants to
    while True:
        loopCheck, playerScore, computerScore = interface(playerScore, computerScore)

        print(f"Player Score: {playerScore}\nComputer Score: {computerScore}\n")

        if loopCheck is False:
            break


### The interface() method takes in two arguments, the player's and computer's
### score throughout the program's execution. It calls the method check() to see
### who won based on their choice.

def interface(playerScore, computerScore):

    # prepares the lists of answers possible for the game and the looping
    choices = ["ROCK", "PAPER", "SCISSOR"]
    loopChoices = ["YES", "NO"]

    print("\nWelcome to Rock, Paper, and Scissor Game!")

    # checks for appropriate input from user
    while True:
        answer = input("Enter your pick: ").upper()

        if answer not in choices:
            print("Invalid choice. Try again!\n")
        else:
            break

    # chooses an answer for the computer randomly
    computerAnswer = random.choice(choices)

    # calls the check() function, which returns a value that determines the winner
    winner = check(choices, answer, computerAnswer)

    # conditional statements to check who won
    if winner == 0:
        print("\nYou won!")
        playerScore += 1
    elif winner == 1:
        print("\nYou Lost!")
        computerScore += 1
    elif winner == -1:
        print("\nTie!")

    # loop structure to ask if they want to play again
    while True:
        loopCheck = input("\nDo you want to try again? Yes or No: ").upper()

        if loopCheck not in loopChoices:
            print("Invalid choice. Try again!\n")
        elif loopCheck == "YES":
            return True, playerScore, computerScore
        elif loopCheck == "NO":
            return False, playerScore, computerScore


### The check method takes in the list of choices, and the answer of both the
### player and the computer. It then checks using conditionals who won.

def check(choices, player, computer):

    # if they both have the same answer, return -1 (tie)
    if player == computer:
        return -1
    
    # if the player's answer is rock
    elif player == choices[0]:
        # if the computer's answer is scissor
        if computer == choices[2]:
            return 0
        else:
            return 1
    
    # if the player's answer is paper
    elif player == choices[1]:
        # if the computer's answer is rock
        if computer == choices[0]:
            return 0
        else:
            return 1
        
    # if the player's answer is scissor
    else:
        # if the player's answer is paper
        if computer == choices[1]:
            return 0
    
    return 1



if __name__ == "__main__":
    main()