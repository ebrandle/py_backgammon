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
    # draw t board
    #drawing.drawBoard(t,wn,board)

    return t,wn,board

def main():
    t,wn,board = setUpBoard()
    drawing.drawBoard(t,wn,board)
    #print(board)
    white = 'tan'
    brown = 'saddlebrown'
    # drawToken(t,wn,quad,triangle,player,ringColor,board)
    drawing.drawToken(t,wn,0,1,white,brown,board)
    drawing.drawToken(t,wn,1,1,white,brown,board)
    drawing.drawToken(t,wn,2,1,white,brown,board)
    drawing.drawToken(t,wn,3,3,white,brown,board)
    #drawing.drawToken(t,wn,quad,tri,brown,white,board)

main()
