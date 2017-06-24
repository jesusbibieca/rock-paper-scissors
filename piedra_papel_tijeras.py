##Rock, paper o scissors##

#Written by Jesus Bibieca on 6/21/2017...

import random # I import the necessary library
import time #This will import the module time to be able to wait

#chose = "" #Initializing variables

def computer(): #This function will get a rand value between 1-99 and depending on the number I'll select either "piedra, papel o tijeras"
    for i in range(1): #Determines the amount of numbers that will be returned
        rand_value = random.randint(1, 99) #Set the limits of the random library 

        if rand_value <= 33:
            chose = "piedra"
        elif rand_value <= 66:
            chose = "papel"
        else:
            chose = "tijeras"
       
        return chose #Gives back an answer with the computer's selection

def game(): #This function is the game perce
    print
    print "Este es el juego de piedra, papel o tijeras escrito por Jesus Bibieca." #Display msgs
    #print "n\"
    user = raw_input("Escoja piedra, papel o tijeras y digitelo a continuacion: ")#Takes user's entry

    selection = computer()#Look for a rand selection


    if user == selection:#Here below I've set a way to determine who wins
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Fue un empate."

    elif user == "piedra" and selection == "papel":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted perdio."

    elif user == "piedra" and selection == "tijeras":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted gano!"

    elif user == "papel" and selection == "piedra":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted gano!"

    elif user == "papel" and selection == "tijeras":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted perdio."

    elif user == "tijeras" and selection == "piedra":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted perdio."

    elif user == "tijeras" and selection == "papel":
        print "Usted eligio: ", user, " y la computadora eligio: ", selection
        print "Usted gano!"

    else:
        print
        print "Usted eligio: ", user, " y esto no es una opcion valida"

    time.sleep(3) #The game waits for 3 secs and then starts again. 
    play_again()

def play_again():
    print 
    keep_play = raw_input("Deseas volver a jugar? (Digita si o no) ")
    if keep_play == "si":
        time.sleep(2)
        game()
    elif keep_play == "no":
        print
        print "Gracias por jugar!"
        time.sleep(2)
        exit()
    else:
        print
        print "Esta no es una opcion valida. Por favor introduce si o no."
        play_again()

game()#The game executes.
