# Side Project - Backgammon
# Started Nov 4, 2020
# Esther Brandle

import random
import turtle
import drawing

def oldGame():
    pass

def newGame():
    pass

def setUpBoard():
    # turtle init stuff
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,13,13,-1)
    t=turtle.Turtle()
    t.hideturtle()
    wn.tracer(False)
    # make logical board
    quad = ['']*6
    board = [quad[:],quad[:],quad[:],quad[:]]

    return t,wn,board

def main():
    t,wn,board = setUpBoard()
    drawing.drawBoard(t,wn,board)
    #print(board)
    white = 'tan'
    brown = 'saddlebrown'
    # drawToken(t,wn,quad,triangle,player,ringColor,board)
    drawing.drawToken(t,wn,2,5,white,brown,board)
    drawing.drawToken(t,wn,0,0,brown,white,board)

main()
