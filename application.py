print "Welcome to game Guess Number"
import random #This module will generate a random number

New_Game = True
while New_Game == True: #This will run while the user want to play

    Random_Number = random.randint(1, 20) #This variable saves the generated number from 1 to 20
    Turn = 1 #This counts the opportunities of the player
    while Turn <= 4: #The player only has 4 Turns
        try: 
            print Turn, "Turn"
            print Random_Number,"I Guess Number"
            Number = int(raw_input("Enter a number from 1 to 20: ")) #This condition checks if the user guesses the number
            
            if Number == Random_Number:
                print "You win!"

                Winner = True
                while Winner == True: #When of the player wins the game asks if want to play again
                    
                    Answer = raw_input("Do you want to play again? yes or no:  ")
                    Answer = Answer.lower()

                    if Answer == "yes":
                        Winner = False #If the answer of the player is "yes" no longer will ask
                        New_Game = True #This will run the game again
                        Turn= 1
                    elif Answer == "no":
                        Winner = False 
                        New_Game = False
                        Turn = 5 #This will stop the game
                        print "Thanks for to play!"
                    else:
                        print "Only can enter yes or no "
                        Winner = True #The game only can accept "yes" or "no"
            elif Number > Random_Number: #This compares if the number entered is higher than the generated number
                print "You guessed too high, please try again"
                Turn+= 1 
                
            elif Number < Random_Number:#This compares if the number entered is lower than the generated number
                print "You guessed too low, please try again"
                Turn+= 1
                
        except ValueError:
            print "Only can enter numbers"

    if New_Game == False:
        break
    else:
        print "Game Over"
        print "The number was: %d" % Random_Number
    Loser = True
    while Loser == True: #when the player loses the game will ask if want to play again
        Answer = raw_input("Do you want to play again? yes or no")
        Answer = Answer.lower()

        if Answer == "yes":
            Loser = False
            New_Game = True
        elif Answer == "no":
            Loser = False
            New_Game = False
            print "Thanks for to play"
        else:
            print "Only can enter yes or no"
            Loser = True
