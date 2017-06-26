##Rock, paper o scissors##

#Written by Jesus Bibieca on 6/21/2017...

import random # I import the necessary library
import time #This will import the module time to be able to wait

#chose = "" #Initializing variables

def computer(): #This function will get a rand value between 1-99 and depending on the number I'll select either "rock, paper o scissors"
    for i in range(1): #Determines the amount of numbers that will be returned
        rand_value = random.randint(1, 99) #Set the limits of the random library 

        if rand_value <= 33:
            chose = "rock"
        elif rand_value <= 66:
            chose = "paper"
        else:
            chose = "scissors"
       
        return chose #Gives back an answer with the computer's selection

def game(): #This function is the game perce
    print
    print "This is the rock, paper, scissors' game written by Jesus Bibieca." #Display msgs
    print
    user = raw_input("Choose rock, paper or scissors and type it to play: ")#Takes user's entry

    selection = computer()#Look for a rand selection


    if user == selection:#Here below I've set a way to determine who wins
        print "You chose: ", user, " and the computer chose: ", selection
        print "It was a tie."

    elif user == "rock" and selection == "paper":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You lost."

    elif user == "rock" and selection == "scissors":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You won!"

    elif user == "paper" and selection == "rock":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You won!"

    elif user == "paper" and selection == "scissors":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You lost."

    elif user == "scissors" and selection == "rock":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You lost."

    elif user == "scissors" and selection == "paper":
        print "You chose: ", user, " and the computer chose: ", selection
        print "You won!"

    else:
        print
        print "You chose: ", user, " and this is not a valid option."

    time.sleep(3) #The game waits for 3 secs and then starts again. 
    play_again()

def play_again():
    print 
    keep_play = raw_input("Do you want to play again? (Type yes or no) ")
    if keep_play == "yes":
        time.sleep(2)
        game()
    elif keep_play == "no":
        print
        print "Thank you for playing!"
        time.sleep(2)
        exit()
    else:
        print
        print "This is not a valid option."
        play_again()

game()#The game executes.
