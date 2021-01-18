# Side Project - Backgammon
# Started Nov 4, 2020
# Esther Brandle

import random
import turtle
import bg_drawing
import bg_dice

def oldGame():
    pass

def newGame():
    for pos in ['A4']:
        triangleD[pos].changeTknColor(brown)
        for x in range(7):
            triangleD[pos].addToken()
        triangleD[pos].drawTokensOnTri(t,wn,board)

def makeTriangles():
    # init values for making triangles
    triangles = {}
    color = -1
    x = -1
    y = -1
    # normal board locations
    for letter in ['A','B','C','D']:
        for num in [1,2,3,4,5,6]:
            # triangle name
            name = letter+str(num)
            # triangle color
            if (letter in ['A','B'] and num in [1,3,5]) or \
               (letter in ['C','D'] and num in [2,4,6]):
                color = 'tan'
            else:
                color = 'saddlebrown'
            # triangle x
            if letter in ['A','D']:
                x = 12-num
            else:
                x = 6-num
            # triangle y
            if letter in ['A','B']:
                y = 0
            else:
                y = 6
            triangles[name] = bg_drawing.Triangle(name,color,x,y)
    # white
    triangles['whiteBar'] = bg_drawing.Triangle('E0wbar','beige',0.5,10)
    triangles['whiteOut'] = bg_drawing.Triangle('E0wout','beige',2.75,10)
    # brown
    triangles['brownBar'] = bg_drawing.Triangle('E0bbar','beige',8,10)
    triangles['brownOut'] = bg_drawing.Triangle('E0bout','beige',10.25,10)
    return triangles

def setUpBoard():
    # turtle init stuff
    wn=turtle.Screen()
    wn.setworldcoordinates(-1,13,13,-1)
    t=turtle.Turtle()
    t.hideturtle()
    wn.tracer(False)
    # make logical board
    quad = ['']*6
    board = [quad[:],quad[:],quad[:],quad[:],['','','','']]
    triangleD = makeTriangles()
    # make dice
    #(numberOfDice,color,size,firstX,Y,xInterval)
    whiteDice=bg_dice.groupOfDice(2,"tan",0.85,5,8,1)
    brownDice=bg_dice.groupOfDice(2,"saddlebrown",0.85,6.5,8,1)
    return t,wn,board,triangleD

def main():
    t,wn,board,triangleD = setUpBoard()
    bg_drawing.drawBoard(t,wn,board,triangleD)

    white = 'tan'
    brown = 'saddlebrown'

    triangleD['brownOut'].changeTknColor(white)
    for x in range(5):
        triangleD['brownOut'].addToken()
    triangleD['brownOut'].drawTokensOnTri(t,wn,board)

    #triangleD['A5'].removeToken()
    #triangleD['A5'].redrawTriangle(t,wn,board)

main()
