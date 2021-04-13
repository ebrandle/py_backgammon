# Side Project - Backgammon
# Started Nov 4, 2020
# Esther Brandle

import random
import turtle
import bg_drawing
import bg_dice

def oldGame():
    pass

def newGame(t,wn,board,triangleD,white,brown):
    for pos in ['A1','B6','C2','D6']:
        triangleD[pos].changeTknColor(white)
        if pos == 'A1':triangleD[pos].numTokens = 2
        if pos == 'B6':triangleD[pos].numTokens = 5
        if pos == 'C2':triangleD[pos].numTokens = 3
        if pos == 'D6':triangleD[pos].numTokens = 5
        triangleD[pos].drawTokensOnTri(t,wn,board)
    for pos in ['A6','B2','C6','D1']:
        triangleD[pos].changeTknColor(brown)
        if pos == 'A6':triangleD[pos].numTokens = 5
        if pos == 'B2':triangleD[pos].numTokens = 3
        if pos == 'C6':triangleD[pos].numTokens = 5
        if pos == 'D1':triangleD[pos].numTokens = 2
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
    triangles['whiteOut'] = bg_drawing.Triangle('E0wOut','beige',.75,10)
    triangles['whiteBar'] = bg_drawing.Triangle('E0wBar','beige',2.85,10)
    # brown
    triangles['brownBar'] = bg_drawing.Triangle('E0bBar','beige',8.25,10)
    triangles['brownOut'] = bg_drawing.Triangle('E0bOut','beige',10.5,10)
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
    whiteDice=bg_dice.groupOfDice(wn,2,"tan",4.85,8.15,0.65)
    brownDice=bg_dice.groupOfDice(wn,2,"saddlebrown",6.55,8.15,0.65)
    # other stuff
    white = 'tan'
    brown = 'saddlebrown'
    return t,wn,board,triangleD,whiteDice,brownDice,white,brown

def main():
    t,wn,board,triangleD,whiteDice,brownDice,white,brown = setUpBoard()
    bg_drawing.drawBoard(t,wn,board,triangleD)
    newGame(t,wn,board,triangleD,white,brown)
    
    whiteDice.rollGroup(wn)
    brownDice.rollGroup(wn)

    #triangleD['brownOut'].changeTknColor(brown)
    #for x in range(5):
    #    triangleD['brownOut'].addToken()
    #triangleD['brownOut'].drawTokensOnTri(t,wn,board)

    #triangleD['A5'].removeToken()
    #triangleD['A5'].redrawTriangle(t,wn,board)

main()
