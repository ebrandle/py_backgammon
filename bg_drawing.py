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
        #if self.tri == 0:
        #    return
        wn.tracer(False)
        t.up()
        t.goto(self.x+1,self.y)
        t.down()
        # cover rectangle where pieces might be
        t.color('beige')
        t.begin_fill()
        if self.y == 0:
            t.goto(self.x+1,2.99)
            t.goto(self.x,2.99)
        elif self.y == 6:
            t.goto(self.x+1,3.01)
            t.goto(self.x,3.01)
        else:
            #t.color('white')
            t.goto(self.x+1,7)
            t.goto(self.x,7)
        t.goto(self.x,self.y)
        t.goto(self.x+1,self.y)
        t.end_fill()
        # draw actual triangle
        t.color('black',self.clr)
        t.begin_fill()
        if self.y == 0:
            t.goto(self.x+.5,2.8)
            t.goto(self.x,self.y)
        elif self.y == 6:
            t.goto(self.x+.5,3.2)
            t.goto(self.x,self.y)
        t.goto(self.x,self.y)
        t.end_fill()
        t.up()
        wn.tracer(True)

    def drawTokensOnTri(self,t,wn,board):
        if self.numTokens <=5: #0-5
            tmpX = self.x+.5
        elif self.numTokens <=10: #6-10
            tmpX = self.x+.4
        elif self.numTokens >=5: #11-15
            tmpX = self.x+.3
        tmpY = self.y
        if self.y != 0:
            tmpY -= .5
        for tkn in range(self.numTokens):
            t.goto(tmpX,tmpY)
            if self.quad == 'E':
                #(t,wn,quad,tri,color,ringColor,board,x,y,numTokens)
                drawToken(t,wn,4,self.tri-1,self.tknCol,self.ringCol,board,tmpX,tmpY,str(self.numTokens))
            else:
                drawToken(t,wn,int(chr(ord(self.quad)-17)),self.tri-1,self.tknCol,self.ringCol,board,tmpX,tmpY,str(self.numTokens))
            # stack pieces up or down
            if self.y == 0:
                tmpY += .5
            else:
                tmpY -= .5
            # if more than 5 pieces, reset Y overlap X
            if tkn == 4:
                tmpX += .2
                tmpY = self.y
                if self.y != 0:
                    tmpY -= .5
            elif tkn == 9:
                tmpX += .2
                tmpY = self.y
                if self.y != 0:
                    tmpY -= .5
        return success
    
    def redrawTriangle(self,t,wn,board):
        wn.tracer(False)
        self.drawTriangle(t,wn)
        self.drawTokensOnTri(t,wn,board)
        drawBoardEdge(t,wn,'black',False)
        drawMidPoint(t,wn)
        wn.tracer(True)

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
def drawToken(t,wn,quad,tri,color,ringColor,board,x,y,tknNum):
    if color == 'tan':
        board[quad][tri] = 'w'+tknNum
    elif color == 'saddlebrown':
        board[quad][tri] = 'b'+tknNum
    else:
        return error
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
    wn.tracer(False)
    t.up()
    t.pensize(3)
    t.goto(6,0)
    t.down()
    t.goto(6,6)
    t.pensize(1)
    t.up()
    wn.tracer(True)


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

def labelTriangles(t,wn):
    wn.tracer(False)
    t.up()
    t.color("black","black")
    for row in [0,6]:
        for quad in [5.45,11.45]:
            labelQuad(t,row,quad)

    # label other stuff
    t.goto(2.5,11.5)
    t.write('White', font=("courier new",18,"bold"))
    t.goto(0.15,10.5)
    t.write('On the Bar',font=("courier new",14,"bold"))
    t.goto(2.25,10.5)
    t.write('Off the Board',font=("courier new",14,"bold"))
    t.goto(4.85,10.5)
    t.write('Dice',font=("courier new",14,"bold"))

    t.goto(8.5,11.5)
    t.write('Brown', font=("courier new",18,"bold"))
    t.goto(6.6,10.5)
    t.write('Dice',font=("courier new",14,"bold"))
    t.goto(7.75,10.5)
    t.write('Off the Board',font=("courier new",14,"bold"))
    t.goto(10.25,10.5)
    t.write('On the Bar',font=("courier new",14,"bold"))
    
    wn.tracer(True)

def drawDiceBG(t,wn,start):
    t.up()
    t.st()
    wn.tracer(False)
    t.goto(start,10)
    t.down()
    t.color('beige')
    t.begin_fill()
    t.goto(start,7)
    t.goto(start+1,7)
    t.goto(start+1,10)
    t.end_fill()
    t.ht()
    wn.tracer(True)
    t.up()

#######################
''' MAIN DRAW BOARD '''
#######################
def drawBoard(t,wn,board,triD):
    wn.tracer(False)
    t.up()
    # draw board, filled
    drawBoardEdge(t,wn,'black',True)
    # draw triangles
    for key in triD:
        triD[key].drawTriangle(t,wn)
    labelTriangles(t,wn)
    # redraw board edge, not filled
    drawMidPoint(t,wn)
    drawBoardEdge(t,wn,'black',False)

    # draw dice background
    for start in [4.7,6.4]:
        drawDiceBG(t,wn,start)
    
    wn.tracer(True)
