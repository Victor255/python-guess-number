"""I GUESS NUMBER"""
import random #This module will generate a random Number

INSTRUCTIONS = """
*************************************************************
** The objective in this game is you can guess a number    **
** in a range of one and twenty, when you enter the number **
** the game verify if is more high                         **
** or more lower than the generated number.                **
**                                                         **
** Caution have only four chances to guess the number      **
**                                                         **
** Luck trying to guess the number!!                       **
*************************************************************
"""

GAME = True
print INSTRUCTIONS
while GAME == True: #This will run while the user want to play

    RANDOM = random.randint(1, 20) #This variable saves the generated Number from 1 to 20
    TURN = 1 #This counts the opportunities of the player
    while TURN <= 4: #The player only has 4 Turns
        try:
            print "\n----- Your number turn is: %s -----" %TURN,
            print "\n\n----- %s -----" % RANDOM
            NUMBER = int(raw_input("\nEnter a NUMBER from 1 to 20: "))
            #This condition checksif the user guesses the Number
            if NUMBER == RANDOM:
                print "\n\nYou win!"
                TURN = 5
            elif NUMBER > RANDOM:
                #This compares if the Number entered is higher than the generated Number
                print "You guessed too high, please try again"
                TURN += 1
                if TURN > 4:
                    print "\nGame Over"
                    print "\nThe Number was: %d" % RANDOM
            elif NUMBER < RANDOM:
                #This compares if the Number entered is lower than the generated Number
                print "You guessed too low, please try again"
                TURN += 1
                if TURN > 4:
                    print "\nGame Over"
                    print "\nThe Number was: %d" % RANDOM
        except ValueError:
            print "\nOnly can enter Numbers"
    LOSER = True
    while LOSER == True: #when the player loses the Game will ask if want to play again
        ANSWER = raw_input("Do you want to play again? yes or no: ")
        ANSWER = ANSWER.lower()
        if ANSWER == "yes":
            LOSER = False
            GAME = True
        elif ANSWER == "no":
            LOSER = False
            GAME = False
            print "\nThanks for to play"
        else:
            print "\nOnly can enter yes or no"
            LOSER = True
