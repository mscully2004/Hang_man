#Hang Man Game
from turtle import*
from random import randint
import math
import time

wordList = ['dog', 'cat', 'bridge', 'overwatch', 'nuclear', 'bloodshed',\
            'xylaphone', 'quokka', 'kangaroo', 'fortnite', 'computer', 'train',\
            'insect', 'absurd', 'oppinion', 'answer', 'zebra', 'turkey', 'foil', \
            'supercalifragalisticexpialidous', 'apple', 'bannana', 'halloween', \
            'fatigue', 'malice', 'monkey', 'boat']

sw = 800
sh = 800
s = getscreen()
s.setup(sw,sh)
s.bgcolor('#42d4f4')
t1=getturtle()
t1.color ('black')
t1.speed(0)
t1.pensize(5)
lAngle = 33
aAngle = 120
RIGHT = True
LEFT = False



#another turtle
tWriter = Turtle()
tWriter.hideturtle()
#another turtle
tBadLetters = Turtle()
tBadLetters.hideturtle()
#variables to play the game
alpha = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
lettersWrong = "" #starting at empty guesses
lettersCorrect = ""
secretWord = ""
displayWord = ""
fails = 6 #guess left
fontS = 15
gameDone = False



def pickSecretWord():
    global secretWord
    secretWord = wordList[randint(0, len(wordList)-1 )]
    print("The secret word is " + secretWord)

def displayText(newText):
    tWriter.clear()
    tWriter.penup()
    tWriter.goto(-int(sw*0.4), -int(sh*0.4) )
    tWriter.write(newText, font = ("Arial", fontS, "bold"))

def displayBadLetters(newText):
    tBadLetters.clear()
    tBadLetters.penup()
    tBadLetters.goto(-int(sw*0.4), int(sh*0.4) )
    tBadLetters.write(newText, font = ("Arial", fontS, "bold"))

def makeWordString():
    global displayWord, alpha
    displayWord = ""
    for l in secretWord:
        if str(l) in alpha:
            if str(l).lower() in lettersCorrect.lower():
                displayWord += str(l) + " "
            else:
                displayWord += "_" + " "

        else:
            displayWord += str(l) + " "
def getGuess():
    boxTitle = "letters Used:" + lettersWrong
    theGuess = s.textinput(boxTitle, "Enter a Guess type $$ to Guess the word")
    return theGuess

                
            

def updateHangman():
    global fails
    if fails == 5:
        drawHead()
    if fails == 4:
        drawTorso()
    if fails == 3:
        drawArm(RIGHT)
    if fails == 2:
        drawArm(LEFT)
    if fails == 1:
        drawLeg(RIGHT)
    if fails == 0:
        drawLeg(LEFT)

def checkWordGuess(): ###Word
    global fails, gameDone
    boxTitle = "Word Guess"
    theGuess = s.textinput(boxTitle, "Guess the Word")
    if theGuess == secretWord:
        displayText("YES!! The word is " + secretWord)
        gameDone = True
    else:
        displayText("No the Word is not:"+ theGuess)
        time.sleep(1)
        displayText(displayWord)
        fails -= 1
        updateHangman()

def restartGame():
    global fails, lettersCorrect, lettersWrong, gameDone
    boxTitle = "Wat to play again?"
    guess = s.textinput(boxTitle, "Type yes  to play again!")

    if guess.lower() == 'y' or guess.lower() =='yes':
        gameDone = False
        lettersCorrect = ""
        lettersWrong = ""
        t1.clear()
        drawGallows()
        pickSecretWord()
        displayText("Pick a letter...")
        displayBadLetters("Not in word: [" + lettersWrong + "]")
        time.sleep(1)
        makeWordString()
        displayText(displayWord)
        fails = 6
    else:
        displayBadLetters("Ok, See you later!")


def playGame():
    global gameDone, fails, alpha, lettersCorrect, lettersWrong, theGuess
    while gameDone == False and fails > 0:
        #get input
        theGuess = getGuess()
        if theGuess == "$$":
            print("let them guess word")
            checkWordGuess()###Word
        elif len(theGuess) > 1 or theGuess == "":
                displayText("sorry I need a letter, guess again")
                time.sleep(1)
                displayText(displayWord)
        elif theGuess not in alpha:
            displayText(theGuess + " is not a letter, guess again")
            time.sleep(1)
            displayText(displayWord)
        elif theGuess.lower() in secretWord.lower():
            lettersCorrect += theGuess.lower()
            makeWordString()
            displayText(displayWord)
        else:
            if theGuess.lower() not in lettersWrong:
                lettersWrong += theGuess.lower() + ","
                fails -= 1
                displayText(theGuess + " is not in the word")
                time.sleep(1)
                updateHangman()
                displayText(displayWord)
                displayBadLetters("Not in word: [" + lettersWrong +"]")
            else:
                displayText(theGuess + " was already guessed. Try again")
                time.sleep(1)
                displayText(displayWord)
                
        if "_" not in displayWord:
            displayText("YES! THE WORD IS: " + secretWord )
            gameDone = True
        if fails <= 0:
            displayText("Sorry Out of Guesses, the Word is: " + secretWord)
            gameDone = True
        if gameDone ==True:
            restartGame()




    

def drawGallows():
    global noseX, nooseY
    #base
    t1.color('black')
    t1.penup()
    t1.setheading(0)
    t1.goto(-int(sw/4), -int(sh/4) )
    t1.pendown()
    t1.forward(int(sw*0.3))# draw main pole
    t1.penup()
    t1.backward(int(sw*0.10))
    t1.pendown()
    t1.left(90)
    t1.forward(int(sh*0.60))#draw top
    t1.left(90)
    t1.forward(int(sw*0.25))#draw hanger
    t1.left(90)
    t1.forward(int(sh*0.10))
    nooseX = t1.xcor()
    nooseY = t1.ycor()

def drawHead():
    global headR
    hR = int(sw*0.08)
    headR = hR
    t1.penup()
    t1.goto(t1.xcor()-hR, t1.ycor()-hR)
    t1.pendown()
    t1.circle(hR)
    t1.penup()
    t1.goto(t1.xcor()+hR, t1.ycor()-hR)
    t1.setheading(-90)


def drawArm(whichA):
    #assumes that turtle is at -90 position
    #assumes that turtle is at bottom of torso
    tx = t1.xcor()  # remember x and y coords for later
    ty = t1.ycor()
    t1.setheading(-90)
    t1.backward(int(sh*0.10))
    if(whichA == RIGHT):
        t1.left(aAngle)
    else:
        t1.right(aAngle)
    t1.pendown()
    t1.forward(int(sw*0.1))
    t1.penup()
    t1.goto(tx, ty)
    t1.setheading(-90)

def drawTorso():
    t1.pendown()
    t1.forward(int(sh*0.15))
    t1.hideturtle()
    
def drawLeg(whichL):
    #save turtle position
    tx = t1.xcor()
    ty = t1.ycor()
    t1.setheading(-90)
    if(whichL == RIGHT):
        t1.left(lAngle)
    else:
        t1.right(lAngle)
    t1.pendown()
    t1.forward(int(sh*0.15))
    t1.penup()
    t1.goto(tx, ty)
    t1.setheading(-90)

    
# good to go
drawGallows()
drawHead()
drawTorso()
drawArm(RIGHT)
drawArm(LEFT)

drawLeg(RIGHT)
drawLeg(LEFT)


time.sleep(1)
t1.clear()
drawGallows()
pickSecretWord()
displayText("Pick a letter...")
displayBadLetters("Not in word: [" + lettersWrong + "]")
time.sleep(1)
makeWordString()
displayText(displayWord)
playGame()

    
