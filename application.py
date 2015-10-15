"""I GUESS NUMBER"""
print "Welcome to Game Guess Number"
import random #This module will generate a random NUMBER

GAME = True
while GAME == True: #This will run while the user want to play

    RANDOM = random.randint(1, 20) #This variable saves the generated NUMBER from 1 to 20
    TURN = 1 #This counts the opportunities of the player
    while TURN <= 4: #The player only has 4 TURNs
        try:
            print TURN, "TURN"
            print RANDOM, "I Guess NUMBER"
            NUMBER = int(raw_input("Enter a NUMBER from 1 to 20: "))
            #This condition checksif the user guesses the NUMBER
            if NUMBER == RANDOM:
                print "You win!"
                WINNER = True
                while WINNER == True:
                	#When of the player wins the GAME asks if want to play again
                    ANSWER = raw_input("Do you want to play again? yes or no:  ")
                    ANSWER = ANSWER.lower()
                    if ANSWER == "yes":
                        WINNER = False #If the ANSWER of the player is "yes" no longer will ask
                        GAME = True #This will run the GAME again
                        TURN = 1
                    elif ANSWER == "no":
                        WINNER = False
                        GAME = False
                        TURN = 5 #This will stop the GAME
                        print "Thanks for to play!"
                    else:
                        print "Only can enter yes or no "
                        WINNER = True #The GAME only can accept "yes" or "no"
            elif NUMBER > RANDOM:
            	#This compares if the NUMBER entered is higher than the generated NUMBER
                print "You guessed too high, please try again"
                TURN += 1
            elif NUMBER < RANDOM:
            	#This compares if the NUMBER entered is lower than the generated NUMBER
                print "You guessed too low, please try again"
                TURN += 1
        except ValueError:
            print "Only can enter NUMBERs"
    if GAME == False:
        break
    else:
        print "GAME Over"
        print "The NUMBER was: %d" % RANDOM
    LOSER = True
    while LOSER == True: #when the player loses the GAME will ask if want to play again
        ANSWER = raw_input("Do you want to play again? yes or no")
        ANSWER = ANSWER.lower()
        if ANSWER == "yes":
            LOSER = False
            GAME = True
        elif ANSWER == "no":
            LOSER = False
            GAME = False
            print "Thanks for to play"
        else:
            print "Only can enter yes or no"
            LOSER = True
