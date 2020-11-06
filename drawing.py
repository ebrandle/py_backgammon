# Backgammon drawing module
# token, board, triangle
# Esther Brandle

import turtle

def drawToken(t,wn,quad,tri,color,ringColor,board):
    board[quad][tri] = color[0]
    wn.tracer(False)
    
    t.color('black',color)
    t.begin_fill()
    t.up()
    t.goto(tri+.5,quad)
    t.down()
    t.circle(.24)
    t.end_fill()
    t.color(ringColor)
    for size in range(1,4):
        t.up()
        t.goto(tri+.5,quad+(.25-(size*.06)-.01))
        t.down()
        t.circle(size*.06)

    wn.tracer(True)
    return board

def drawTriangle(t,pos,color,level):
    t.color('black',color)
    t.begin_fill()
    if level == 0:
        t.goto(pos+.5,2.8)
    else:
        t.goto(pos+.5,3.2)
    t.goto(pos,level)
    t.end_fill()

def drawBoard(t,wn,board):
    wn.tracer(False)
    t.up()
    drawBoardEdge(t,'black',True)
    # draw mid point
    t.down()
    t.pensize(3)
    t.goto(6,0)
    t.goto(6,6)
    t.pensize(1)
    t.up()
    
    # draw row 1 (quad 0 & 1)
    t.goto(12,0)
    t.down()
    pos = 11
    for x in range(6):
        for color in ['tan','saddlebrown']:
            drawTriangle(t,pos,color,0)
            pos -= 1
    t.up()
    # draw row 2 (quad 2 & 3)
    t.goto(12,6)
    t.down()
    pos = 11
    for x in range(6):
        for color in ['saddlebrown','tan']:
            drawTriangle(t,pos,color,6)
            pos -= 1
    t.up()

    drawBoardEdge(t,'black',False)
    wn.tracer(True)

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
    
