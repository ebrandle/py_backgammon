# Backgammon drawing module
# token, board, triangle
# Esther Brandle

import turtle

def processLocation(quad,triangle,board):
    row = 0
    col = 0
    if quad in [0,1]:
        row = 0
        #if quad == 0:
            #col = (-triangle) + 
    else:
        row = 11
    
    return row,col

def drawToken(t,wn,quad,tri,color,ringColor,board):
    board[quad][tri] = color[0]
    print(board)
    row,col = processLocation(quad,tri,board)
    wn.tracer(False)
    
    t.color('black',color)
    t.begin_fill()
    t.up()
    t.goto(row+.5,col)
    t.down()
    t.circle(.24)
    t.end_fill()
    t.color(ringColor)
    for size in range(1,4):
        t.up()
        t.goto(row+.5,col+(.25-(size*.06)-.01))
        t.down()
        t.circle(size*.06)

    wn.tracer(True)
    return board

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

def labelPlaces(t):
    for row in [0,6]:
        for quad in [1,2]:
            pass
        t.up()
        t.color("black","black")
        if row == 0:
            t.goto(11.45,row-.2)
        else:
            t.goto(11.45,row+.5)
        t.write(chr(row+65)+'1', font=("courier new",10,"bold"))
    

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
    # redraw board edge
    drawBoardEdge(t,'black',False)
    wn.tracer(True)
