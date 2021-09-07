## ARCHIVE
# Old drawing.py file

# Backgammon drawing module
# token, board, triangle
# Esther Brandle

import turtle
#error = "HELP! IT'S AN ERROR!"


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
def drawTriangle(t,pos,color,height):
    t.color('black',color)
    t.begin_fill()
    if height == 0:
        t.goto(pos+.5,2.8)
    else:
        t.goto(pos+.5,3.2)
    t.goto(pos,height)
    t.end_fill()

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

def drawTriRow(t,color1,color2,height):
    t.goto(12,height)
    t.down()
    pos = 11
    for x in range(6):
        for color in [color1,color2]:
            drawTriangle(t,pos,color,height)
            pos -= 1
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
    # draw row 1 (quad 0 & 1)
    drawTriRow(t,'tan','saddlebrown',0)
    # draw row 2 (quad 2 & 3)
    drawTriRow(t,'saddlebrown','tan',6)
    # redraw board edge, not filled
    drawBoardEdge(t,'black',False)
    labelPlaces(t,wn)
    wn.tracer(True)
