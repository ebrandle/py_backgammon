# Backgammon drawing module
# token, board, triangle
# Esther Brandle

import turtle
error = "HELP! IT'S AN ERROR!"
alert = "AHHH IT'S A THING!"
success = "Yay it worked!"


######################
''' TRIANGLE CLASS '''
######################
class Triangle:
    '''class for triangles'''
    def __init__(self,triName,triColor,x,y):
        # triangle information - does not change
        self.name = triName
        self.clr = triColor
        self.quad = self.name[0]
        self.tri = int(self.name[1])
        self.x = x
        self.y = y

        # token info
        self.numTokens = 0
        self.tknCol = -1 #'tan'
        self.ringCol = -1 #'saddlebrown'

    def __str__(self):
        print(self.name+':',self.clr,self.x,self.y)
        print('Number of tokens:',self.numTokens)

    # Drawing triangle methods
    def drawTriangle(self,t,wn):
        wn.tracer(False)
        t.up()
        t.goto(self.x+1,self.y)
        t.down()
        t.color('black',self.clr)
        t.begin_fill()
        if self.y == 0:
            t.goto(self.x+.5,2.8)
        else:
            t.goto(self.x+.5,3.2)
        t.goto(self.x,self.y)
        t.end_fill()
        t.up()
        wn.tracer(True)
        return success

    def drawTokensOnTri(self,t,wn,board):
        tmpX = self.x+.5
        tmpY = self.y
        if self.y == 6:
            tmpY -= .5
        for tkn in range(self.numTokens):
            t.goto(tmpX,tmpY)
            #print('Quad:',chr(ord(self.quad)-17),'Tri:',self.tri-1)
            drawToken(t,wn,int(chr(ord(self.quad)-17)),self.tri-1,self.tknCol,self.ringCol,board,tmpX,tmpY)
            # stack pieces up or down
            if self.y == 0:
                tmpY += .5
            else:
                tmpY -= .5
            # if more than 5 pieces, reset Y overlap X
            if tkn == 5:
                print(self.name)
                print('X:',self.x,tmpX)
                print('Y:',self.y,tmpY)
                tmpX += .25
                tmpY = self.y
                if self.y == 6:
                    tmpY -= .5
        return success
    
    def redrawTriangle(self,t,wn,board):
        self.drawTriangle(t,wn)
        self.drawTokensOnTri(t,wn,board)
        drawBoardEdge(t,wn,'black',False)
        drawMidPoint(t,wn)

    # Change token info
    def addToken(self):
        self.numTokens += 1
    def removeToken(self):
        self.numTokens -= 1
        if self.numTokens == 0:
            self.tknCol = -1
    def changeTknColor(self,newColor):
        self.tknCol = newColor
        if self.tknCol == 'tan':
            self.ringCol = 'saddlebrown'
        else:
            self.ringCol = 'tan'


###########################
''' DRAW TOKEN ROUTINES '''
###########################
##def processLocation(quad,triangle):
##    # A1, B1, C1, D3
##    y = 0
##    x = 0
##    if quad in [0,1]:
##        y = 0
##        if quad == 0: #A
##            x = (6-triangle) + 6
##        else: #B
##            x = 6-triangle
##    elif quad in [2,3]:
##        y = 5
##        if quad == 2: #C
##            x = 6-triangle
##        else: #D
##            x = (6-triangle) + 6
##    return x,y

def drawToken(t,wn,quad,tri,color,ringColor,board,x,y):
    board[quad][tri] = color[0]
##    changeDirection = 1
##    if 6-y > y:
##        changeDirection = -1
    #x,y = processLocation(quad,tri)
    #print(board)
    wn.tracer(False)
    t.up()
    t.color('black',color)
    t.begin_fill()
    t.down()
    t.circle(.24)
    t.end_fill()
    t.color(ringColor)
    for size in range(1,4):
        t.up()
        t.goto(x,y+(.25-(size*.06)-.01))
        t.down()
        t.circle(size*.06)
    wn.tracer(True)
    t.up()
    return board


###############################
''' DRAW BOARD SUB-ROUTINES '''
###############################
def drawBoardEdge(t,wn,edgeColor,fill):
    wn.tracer(False)
    t.goto(0,0)
    t.pensize(3)
    t.down()
    if fill == True:
        t.color(edgeColor,'beige')
        t.begin_fill()
    else:
        t.color(edgeColor)
    t.goto(0,6)
    t.goto(12,6)
    t.goto(12,0)
    t.goto(0,0)
    if fill == True:
        t.end_fill()
    t.pensize(1)
    t.up()
    wn.tracer(True)

def drawMidPoint(t,wn):
    t.up()
    t.pensize(3)
    t.goto(6,0)
    t.down()
    t.goto(6,6)
    t.pensize(1)
    t.up()


############################
''' DRAW TRIANGLE LABELS '''
############################
def labelQuad(t,row,quad):
    # for each quad section, label
    for tri in range(1,7):
        # quad A
        if row == 0 and quad < 6:
            t.goto(quad,row-.2)
            t.write(chr(row+66)+str(tri), font=("courier new",12,"bold"))
        # quad B
        elif row == 0 and quad > 6:
            t.goto(quad,row-.2)
            t.write(chr(row+65)+str(tri), font=("courier new",12,"bold"))
        # quad C
        elif row == 6 and quad < 6:
            t.goto(quad,row+.5)
            t.write(chr(row+61)+str(tri), font=("courier new",12,"bold"))
        # quad D
        elif row == 6 and quad > 6:
            t.goto(quad,row+.5)
            t.write(chr(row+62)+str(tri), font=("courier new",12,"bold"))
        quad -= 1

def labelPlaces(t,wn):
    wn.tracer(False)
    t.up()
    t.color("black","black")
    for row in [0,6]:
        for quad in [5.45,11.45]:
            labelQuad(t,row,quad)
    wn.tracer(True)


#######################
''' MAIN DRAW BOARD '''
#######################
def drawBoard(t,wn,board,triD):
    wn.tracer(False)
    t.up()
    # draw board, filled
    drawBoardEdge(t,wn,'black',True)
    drawMidPoint(t,wn)
    # draw triangles
    for key in triD:
        triD[key].drawTriangle(t,wn)
    # label triangles
    labelPlaces(t,wn)
    # redraw board edge, not filled
    drawBoardEdge(t,wn,'black',False)
    #labelPlaces(t,wn)
    wn.tracer(True)
