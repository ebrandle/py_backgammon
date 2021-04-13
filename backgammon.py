# Side Project - Backgammon
# Started Nov 4, 2020
# Visual aspects complete Apr 13, 2021
# Esther Brandle

import random
import turtle
import bg_drawing
import bg_dice

#########################
""" CONTINUE OLD GAME """
#########################
def oldGame():
    return

######################
""" START NEW GAME """
######################
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

####################
""" SET UP BOARD """
####################
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

######################
""" GAMEPLAY LOGIC """
######################
def validateMove(old,new,player,whiteDice,brownDice,triangleD):
    no = "Invalid"
    yes = "Valid"
    boardLs = ["A1","A2","A3","A4","A5","A6",\
                "B1","B2","B3","B4","B5","B6",\
                "C6","C5","C4","C3","C2","C1",\
                "D6","D5","D4","D3","D2","D1"]

    ### Basic token validation ###
    # if old is empty or new is full
    if triangleD[old].numTokens == 0:
        return no
    if triangleD[new].numTokens == 15:
        return no
    # if old has invalid token color
    if triangleD[old].tknCol == -1:
        return no
    # if new is 2+ and new/old colors don't match
    if triangleD[new].numTokens > 1 and \
       triangleD[new].tknCol != triangleD[old].tknCol:
        return no

    ### Move validation ###
    # setup
    posOld = -1
    posNew = -1
    for i in range(len(boardLs)):
        if boardLs[i] == old:
            posOld = i
        if boardLs[i] == new:
            posNew = i
    distance = posOld-posNew
    dice = whiteDice
    if player != "tan":
        dice = brownDice
    dieVal = []
    for die in dice.group:
        dieVal.append(die.value)
    # if not valid dice roll
    if abs(distance) not in dieVal:
        return no
            
    return yes

def main():
    t,wn,board,triangleD,whiteDice,brownDice,white,brown = setUpBoard()
    bg_drawing.drawBoard(t,wn,board,triangleD)
    newGame(t,wn,board,triangleD,white,brown)
    
    whiteDice.rollGroup(wn)
    brownDice.rollGroup(wn)

    #print(board)
    color = white
    initColor = input("Team colour: ").lower()
    if initColor == "brown" or initColor == "black":
        color = brown
    move = input("Move token from x to y (ex A1:A2): ").upper()
    while move != "Q":
        old = move[:2]
        new = move[3:]
        status = validateMove(old,new,color,whiteDice,brownDice,triangleD)
        if status == "Invalid":
            print("Invalid move; please try again.")
            if color == white:
                move = input("Player White's turn: ").upper()
            else:
                move = input("Player Brown's turn: ").upper()
            continue
        triangleD[new].changeTknColor(color)
        triangleD[new].addToken(t,wn,board)
        triangleD[old].removeToken(t,wn,board)
        
        # next turn
        if color == white:
            color = brown
            brownDice.rollGroup(wn)
            move = input("Player Brown's turn: ").upper()
        elif color == brown:
            color = white
            whiteDice.rollGroup(wn)
            move = input("Player White's turn: ").upper()

main()
