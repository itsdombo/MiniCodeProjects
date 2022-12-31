# Author:   Dominic Rousseau
#           https://www.github.com/itsdombo
#
# Purpose:  Prompts the user for scissors/paper/rock.
#           Plays a rock, paper, scissors game with the program.
#           When finished, asks to play again.

from random import randint
import time

playAgain = "yes"
scoreUser = 0
scoreBot = 0

while (playAgain in ["yes", "y"]):
    userInput = None
    
    # Asks for user to input rock/paper/scissors
    while (userInput not in ["rock", "paper", "scissors"]):
        userInput = input("Please input choice (rock/paper/scissors): ")
    
    
    index = 3
    print("Revealing in:")
    time.sleep(0.3)
    while (index > 0):
        print(index, end="")
        
        indexDots = 3
        while (indexDots > 0):
            print(".", end="")
            if (index == 3):
                time.sleep(.1)
            elif (index == 2):
                time.sleep(0.2)
            else:
                time.sleep(0.3)
            indexDots -= 1
        print("")
        
        time.sleep(0.2)
        index -= 1
    time.sleep(0.2)
    
    #add convsertion of bot int to string
    botInput = randint(0, 2)
    if (botInput == 0):
        botInput = "rock"
    elif (botInput == 1):
        botInput = "paper"
    else:
        botInput = "scissors"
    
    # Draws the two opponents choices and concludes the outcome.
    print(f"User chose {userInput}!")
    print(f"Bot chose {botInput}!")
    time.sleep(1)
    if ((userInput == "rock" and botInput == "scissors") or (userInput == "paper" and botInput == "rock") or (userInput == "scissors" and botInput == "paper")):
        print("User won!")
        scoreUser += 1
    elif (userInput == botInput):
        print("Tied!")
    else:
        print("Bot won!")
        scoreBot += 1
    time.sleep(1)
    
    #Displays score
    print(f"\nThe current score is:\nUser's points: {scoreUser}.\nBot's points: {scoreBot}.")
    time.sleep(1)
    
    # Prompts user if they want to play again.
    playAgain = input("\nWant to play again?\nAnswer (yes/no): ")
    while (playAgain not in ["yes", "y", "no", "n"]):
        playAgain = input("Input is not valid.\nWant to play again?\nAnswer (yes/no): ")
    print("\n")
    if (playAgain in ["no", "n"]):
        print("Goodbye!")
