# Backgammon drawing module
# token, board, triangle
# Esther Brandle

import turtle
#error = "HELP! IT'S AN ERROR!"


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
        self.tri = self.name[1]
        self.x = x
        self.y = y

        # token info
        self.numTokens = 0
        self.tknCol = -1

    def __str__(self):
        print(self.name+':'+self.clr,self.x,self.y)

    # Drawing triangle methods
    def drawTriangle(self,t,wn):
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
        

    def drawTokensOnTri(self,t):
        for tkn in range(self.numTokens):
            continue
            t.goto()
            drawToken(t,wn,self.quad,self.tri,color,ringColor,board)
    

    # Change token info
    def addToken(self):
        self.numTokens += 1
    def removeToken(self):
        self.numTokens -= 1
        if self.numTokens == 0:
            self.tknCol = -1
    def changeTknColor(self,newColor):
        self.tknCol = newColor


###########################
''' DRAW TOKEN ROUTINES '''
###########################
def processLocation(quad,triangle):
    # A1, B1, C1, D3
    y = 0
    x = 0
    if quad in [0,1]:
        y = 0
        if quad == 0: #A
            x = (6-triangle) + 6
        else: #B
            x = 6-triangle
    elif quad in [2,3]:
        y = 5
        if quad == 2: #C
            x = 6-triangle
        else: #D
            x = (6-triangle) + 6
    return x,y

def drawToken(t,wn,quad,tri,color,ringColor,board):
    board[quad][tri] = color[0]
    #print(board)
    wn.tracer(False)
    x,y = processLocation(quad,tri)
    
    t.color('black',color)
    t.begin_fill()
    t.up()
    # check row
    if y == 0:
        t.goto(x+.5,y)
    elif y == 5:
        t.goto(x+.5,y)
    t.down()
    t.circle(.24)
    t.end_fill()
    t.color(ringColor)
    for size in range(1,4):
        t.up()
        t.goto(x+.5,y+(.25-(size*.06)-.01))
        t.down()
        t.circle(size*.06)

    wn.tracer(True)
    return board


###############################
''' DRAW BOARD SUB-ROUTINES '''
###############################
def drawBoardEdge(t,edgeColor,fill):
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

def makeTriangles():
    # init values for making triangles
    triangles = {}
    color = -1
    x = -1
    y = -1
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
            triangles[name] = Triangle(name,color,x,y)
    return triangles


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
def drawBoard(t,wn,board):
    wn.tracer(False)
    t.up()
    # draw board, filled
    drawBoardEdge(t,'black',True)
    # draw mid point
    t.down()
    t.pensize(3)
    t.goto(6,0)
    t.goto(6,6)
    t.pensize(1)
    t.up()
    
    # make triangles (and put in dictionary)
    triangleD = makeTriangles()
    for key in triangleD:
        triangleD[key].drawTriangle(t,wn)
    
    # redraw board edge, not filled
    drawBoardEdge(t,'black',False)
    #labelPlaces(t,wn)
    wn.tracer(True)
