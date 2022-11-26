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
""" CREATE BOARD """
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
    triangles['E1'] = bg_drawing.Triangle('E1','beige',.75,10)
    triangles['E2'] = bg_drawing.Triangle('E2','beige',2.85,10)
    triangles['E1'].changeTknColor('tan')
    triangles['E2'].changeTknColor('tan')
    # brown
    triangles['E3'] = bg_drawing.Triangle('E3','beige',8.25,10)
    triangles['E4'] = bg_drawing.Triangle('E4','beige',10.5,10)
    triangles['E3'].changeTknColor('saddlebrown')
    triangles['E4'].changeTknColor('saddlebrown')
    return triangles

def createBoard():
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
def tokenValid(old,new,triangleD,yes,no):
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
    return yes

def moveValid(old,new,distance,diceList,player,triangleD,yes,no):
    # if not valid dice roll
    if abs(distance) not in diceList:
        return no
    # if attempting to move other player's piece
    if triangleD[old].tknCol != player:
        return no
    # attempting to move backwards
    if distance > 0 and player == "tan":
        return no
    elif distance < 0 and player == "saddlebrown":
        return no

    ''' TESTING TAKE OFF BOARD '''
    # new = e, still pieces on board outside end quad
    if triangleD[new].name == "E1" and player == "tan":
        print(triangleD[new])
        if not allPiecesInEnd(player,triangleD):
            return no
        
    if triangleD[new].name == "E4" and player == "saddlebrown":
        print(triangleD[new])
        if not allPiecesInEnd(player,triangleD):
            return no    
    
    ''' TESTING PIECES ON BAR '''
    # if white and have pieces on bar
    if player == "tan" and triangleD['E2'].numTokens > 0 and \
       triangleD[old].name != "E2":
        print("Alert triggered. Attempting to move while there are pieces on E2.")
        return no
    elif player == "saddlebrown" and triangleD['E3'].numTokens > 0 and \
       triangleD[old].name != "E3":
        print("Alert triggered. Attempting to move while there are pieces on E3.")
        return no
    
    return yes

''' TESTING TAKE OFF BOARD '''
def allPiecesInEnd(player,triangleD):
    # all pieces have to be in (a or d) and (e3 or e2)
    for tri in triangleD:
        if player == "tan":
            if triangleD[tri].numTokens > 0 and triangleD[tri].tknCol == player and \
               (triangleD[tri].quad == "A" or triangleD[tri].quad == "B" or \
                triangleD[tri].quad == "C" or triangleD[tri].name == "E2"):
                return False
        else:
            if triangleD[tri].numTokens > 0 and triangleD[tri].tknCol == player and \
               (triangleD[tri].quad == "B" or triangleD[tri].quad == "C" or \
                triangleD[tri].quad == "D" or triangleD[tri].name == "E3"):
                return False
    return True

def validateMove(old,new,distance,diceList,player,triangleD):
    # some setup
    no = "Invalid"
    yes = "Valid"

    ### Basic token validation ###
    if tokenValid(old,new,triangleD,yes,no) == no:
        return no
    
    ### Move validation ###
    if moveValid(old,new,distance,diceList,player,triangleD,yes,no) == no:
        return no
    
    return yes

def distanceOfMove(old,new):
    boardLs = ["A1","A2","A3","A4","A5","A6",\
               "B1","B2","B3","B4","B5","B6",\
               "C6","C5","C4","C3","C2","C1",\
               "D6","D5","D4","D3","D2","D1"]
    posOld = -1
    posNew = -1
    # calculate distance for token move
    for i in range(len(boardLs)):
        if boardLs[i] == old:
            posOld = i
        if boardLs[i] == new:
            posNew = i
    distance = posOld-posNew

    # if moving from bar
    if old[0] == "E":
        if new[0] == "A":
            distance = int(new[1])
        elif new[0] == "D":
            distance = abs(int(new[1])-6)+1

    # if moving to bar
    #elif new[0] == "E":
    #    distance = int(old[1])
    
    return distance

def availableDiceList(whiteDice,brownDice,player):
    # add dice values to list
    dice = whiteDice
    if player != "tan":
        dice = brownDice
    diceList = []
    for die in dice.group:
        diceList.append(die.value)
    # if doubles, add 2 more
    if diceList[0] == diceList[1]:
        diceList.append(diceList[0])
        diceList.append(diceList[0])
    return diceList

def makeValidMoveList(diceList,player,triangleD):
    # setup
    bouncedLs = []
    validMoveList = []
    boardLs = ["A1","A2","A3","A4","A5","A6",\
               "B1","B2","B3","B4","B5","B6",\
               "C6","C5","C4","C3","C2","C1",\
               "D6","D5","D4","D3","D2","D1",\
               "E1","E2","E3","E4"]

    # check bar
    if (player == "tan" and triangleD['E2'].numTokens > 0) or \
       (player == "saddlebrown" and triangleD['E3'].numTokens > 0):
        bouncedLs = validMoveListBar(diceList,player,triangleD,boardLs)
        if bouncedLs == []:
            return []
        print(bouncedLs)
        validMoveList.append(bouncedLs)
    # start loops
    for old in boardLs:
        for new in boardLs:
            distance = distanceOfMove(old,new)
            if distance > 6 or distance == 0:
                continue
            status = validateMove(old,new,distance,diceList,player,triangleD)
            if status == "Valid":
                validMoveList.append(old+":"+new)
    return validMoveList

def validMoveListBar(diceList,player,triangleD,boardLs):
    bouncedLs = []
    if player == "tan":
        if triangleD["E2"].numTokens not in diceList:
            return []
        old = "E2"
        for new in ["A1","A2","A3","A4","A5","A6"]:
            distance = int(new[1])
            status = validateMove(old,new,distance,diceList,player,triangleD)
            if status == "Valid":
                bouncedLs.append(old+":"+new)
    elif player == "saddlebrown":
        if triangleD["E3"].numTokens not in diceList:
            return []
        old = "E3"
        for new in ["D1","D2","D3","D4","D5","D6"]:
            distance = int(new[1])
            status = validateMove(old,new,distance,diceList,player,triangleD)
            if status == "Valid":
                bouncedLs.append(old+":"+new)
    return bouncedLs

def newPlayerTurn(player,white,brown,whiteDice,brownDice,wn):
    if player == white:
        player = brown
        brownDice.rollGroup(wn)
    elif player == brown:
        player = white
        whiteDice.rollGroup(wn)
    return player#,whiteDice,brownDice

def main():
    # create + draw board
    t,wn,board,triangleD,whiteDice,brownDice,white,brown = createBoard()
    bg_drawing.drawBoard(t,wn,board,triangleD)
    # set up pieces for new game
    newGame(t,wn,board,triangleD,white,brown)
    # roll dice
    whiteDice.rollGroup(wn)
    brownDice.rollGroup(wn)

    # choose starting player
    player = white
    firstPlayer = input("Player colour: ").lower()
    if firstPlayer == "brown" or firstPlayer == "black":
        player = brown

    # find available dice list
    diceList = availableDiceList(whiteDice,brownDice,player)

    # make validMoveList
    validMoveList = makeValidMoveList(diceList,player,triangleD)
    print(validMoveList)
    if player == white:
        print("White dice:",diceList)
    elif player == brown:
        print("Brown dice:",diceList)

    quitGame = False
    while quitGame == False:
        # make first move or "q" to quit game
        move = input("Move token from x to y (ex A1:A2): ").upper()
        while move != "Q":
            while len(diceList) != 0:
                if move[0] == "Q":
                    quitGame = True
                    break
                # if invalid, try again
                if move not in validMoveList:
                    print("Invalid move; please try again.")
                    if player == white:
                        move = input("White player's turn: ").upper()
                    else:
                        move = input("Brown player's turn: ").upper()
                    continue
                # else play move
                old = move[:2]
                new = move[3:]
                distance = distanceOfMove(old,new)

                # if bouncing opponent piece
                if triangleD[new].tknCol != player and\
                   triangleD[new].numTokens == 1:
                    if player == brown:
                        triangleD['E2'].addToken(t,wn,board)
                        print("White bar:",triangleD['E2'].numTokens)
                    else:
                        triangleD['E3'].addToken(t,wn,board)
                        print("Brown bar:",triangleD['E3'].numTokens)
                    triangleD[new].removeToken(t,wn,board)
                
                #print("Distance:",distance,"diceList:",diceList)
                triangleD[new].changeTknColor(player)
                triangleD[new].addToken(t,wn,board)
                triangleD[old].removeToken(t,wn,board)
                diceList.remove(abs(distance))
                if len(diceList) == 0:
                    player = newPlayerTurn(player,white,brown,whiteDice,brownDice,wn)
                    break
                #print("New diceList:",diceList)
                if player == white:
                    validMoveList = makeValidMoveList(diceList,player,triangleD)
                    print(validMoveList)
                    print("White dice:",diceList)
                    move = input("White player's turn: ").upper()
                    continue
                elif player == brown:
                    validMoveList = makeValidMoveList(diceList,player,triangleD)
                    print(validMoveList)
                    print("Brown dice:",diceList)
                    move = input("Brown player's turn: ").upper()
                    continue
                else:
                    print("Invalid player")
                    move == "Q"
                    quitGame = True
                    break
            
            # next turn
            #player = newPlayerTurn(player,white,brown,whiteDice,brownDice)
            if player == white:
                print("\nWhite player's turn!")
                whiteDice.rollGroup(wn)
                print("Dice rolled.")
                diceList = availableDiceList(whiteDice,brownDice,player)
                validMoveList = makeValidMoveList(diceList,player,triangleD)
                print(validMoveList)
                print("White dice:",diceList)
                move = input("White player's turn: ").upper()
            elif player == brown:
                print("\nBrown player's turn!")
                brownDice.rollGroup(wn)
                print("Dice rolled.")
                diceList = availableDiceList(whiteDice,brownDice,player)
                validMoveList = makeValidMoveList(diceList,player,triangleD)
                print(validMoveList)
                print("Brown dice:",diceList)
                move = input("Brown player's turn: ").upper()
            if move[0] == "Q":
                quitGame = True
                break
        if move[0] == "Q":
            quitGame = True
        if quitGame == True:
            break
    print("Game ended.")

main()
