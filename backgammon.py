# Side Project - Backgammon
# Started Nov 4, 2020
# Esther Brandle

import random
import turtle
import bg-drawing
import bg-dice

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
            triangles[name] = drawingClasses.Triangle(name,color,x,y)
    # on the bar
    triangles['whiteBar'] = drawingClasses.Triangle('w0bar','beige',1.5,10)
    triangles['brownBar'] = drawingClasses.Triangle('b0bar','beige',7.5,10)
    # off the board
    triangles['whiteOut'] = drawingClasses.Triangle('w0out','beige',3.5,10)
    triangles['brownOut'] = drawingClasses.Triangle('b0out','beige',9.5,10)
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
    board = [quad[:],quad[:],quad[:],quad[:]]
    triangleD = makeTriangles()
    return t,wn,board,triangleD

def main():
    t,wn,board,triangleD = setUpBoard()
    drawingClasses.drawBoard(t,wn,board,triangleD)

    white = 'tan'
    brown = 'saddlebrown'

    triangleD['A2'].changeTknColor(brown)
    for x in range(12):
        triangleD['A2'].addToken()
    triangleD['A2'].drawTokensOnTri(t,wn,board)

    #triangleD['A4'].removeToken()
    #triangleD['A4'].redrawTriangle(t,wn,board)

main()
