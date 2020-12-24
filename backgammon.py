# Side Project - Backgammon
# Started Nov 4, 2020
# Esther Brandle

import random
import turtle
import drawingClasses

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
    # draw t board
    #drawing.drawBoard(t,wn,board)

    return t,wn,board

def main():
    t,wn,board = setUpBoard()
    drawingClasses.drawBoard(t,wn,board)
    #print(board)
    white = 'tan'
    brown = 'saddlebrown'
    #drawingClasses.drawToken(t,wn,quad,triangle,player,ringColor,board)
    drawingClasses.drawToken(t,wn,0,1,white,brown,board)
    drawingClasses.drawToken(t,wn,1,1,white,brown,board)

main()
