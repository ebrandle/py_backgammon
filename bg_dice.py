import turtle
import random
#import time

##############
# Single die #
##############
class Dice:
    
    def __init__(self,wn,name,color,lowerLeftX,lowerLeftY):
        # die information
        self.name=name
        self.color=color
        self.X=lowerLeftX
        self.Y=lowerLeftY
        self.value=0
        # die turtle & status
        self.t=turtle.Turtle()
        self.t.color('black',self.color)
        self.t.hideturtle()
        # default draw die
        #self.drawDie(wn)

    def drawDie(self,wn):
        # prepare
        wn.tracer(False)
        self.t.up()
        self.t.goto(self.X,self.Y)
        self.t.down()
        self.t.begin_fill()
        # draw square
        for x in range(4):
            self.t.fd(.65)
            self.t.right(90)
        # prepare
        self.t.end_fill()
        self.t.up()
        self.t.goto(self.X+(0.65/2.25),self.Y-0.15)
        wn.tracer(True)
        # write number
        if self.value != 0:
            self.t.write(str(self.value),font=('Arial','14','normal'))

    def rollDie(self,wn):
        self.value = random.randint(1,6)
        self.drawDie(wn)

#################
# Group of dice #
#################
class groupOfDice(Dice):
    def __init__(self,wn,number,color,X,firstY,yInterval):
        self.group=[]
        self.yInterval=yInterval
        self.startY=firstY
        self.X=X
        for i in range(1,number+1):
            self.group.append(Dice(wn,color+str(i),color,X,self.startY))
            self.startY += (0.65 + self.yInterval)
        
    def rollGroup(self,wn):
        for die in self.group:
            Dice.rollDie(die,wn)

#########################
# Example dice creation #
#########################
'''
# 2 groups of dice
whiteDice=groupOfDice(wn,2,"tan",5,7,1)
x = input('Press enter to start rolling: ')
while x == '':
    whiteDice.rollGroup(wn)
    x = input('All groups of dice have been rolled. Press enter to roll again: ')
'''
