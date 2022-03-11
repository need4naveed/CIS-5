#Number guessing game. Asks for number range and allows user to guess the number.
#User can quit by entering -1 as a guess, and can replay the game multiple times.
#yo naveeds code goes kinda crazy ngl
import RPi.GPIO as GPIO
import time
import random

ledy = 11 #assigning pins to LEDs
ledg = 15
ledr = 37
GPIO.setmode(GPIO.BOARD) #gpio setup
GPIO.setwarnings(False)
GPIO.setup(ledg, GPIO.OUT)
GPIO.setup(ledy, GPIO.OUT)
GPIO.setup(ledr, GPIO.OUT)


def guessgame():
    print("Number guessing game. Enter '-1' as a guess to quit.")
    smin,smax = eval(input("Enter the range of numbers seperated by comma: ")) 
    print("\nGenerating number...") #style points
    rando = random.randint(smin,smax) #random number assigned between min and max
    guess = rando + 1 #reassign guess to not match random number
    while guess != rando: #loops until user guesses correctly
        guess = eval(input("\nWhat is your guess: "))
        gcheck(guess,rando)
        if guess == -1: #quits if user enters -1
            break
    game = input("Play again? Y/N: ").lower() 
    if game == "y": guessgame() #entering y will restart the game
    else: print("\nThanks for playing!") #end-game message the game if y is not entered

def gcheck(g,r): #function for checking guess
    if g > r:
        GPIO.output(ledr, True)
        print("Guess too high")
        time.sleep(2)
        GPIO.output(ledr, False)
        time.sleep(1)
    elif g < r:
        GPIO.output(ledy, True)
        print("Guess too low")
        time.sleep(2)
        GPIO.output(ledy, False)
        time.sleep(1)
    elif g == r:
        GPIO.output(ledg, True)
        print("Wow you're so smart, you got it!")
        time.sleep(2)
        GPIO.output(ledg, False)
        time.sleep(1)
        
    
guessgame() #plays game when program is opened
