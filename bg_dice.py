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
        # die turtle & color
        self.t=turtle.Turtle()
        self.t.color('black',self.color)
        # default draw die
        self.drawDie()

    def drawDie(self):
        # prepare
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
        self.t.goto(self.X+(0.65/2.25),self.Y-(0.65/1.3))
        # write number
        if self.value != 0:
            self.t.write(str(self.value),font=('Arial','14','normal'))

    def rollDie(self):
        self.value = random.randint(1,6)
        self.drawDie()

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
            self.group.append(Dice(wn,name,color,X,self.startY))
            self.startY += (0.65 + self.yInterval)
        
    def rollGroup(self):
        for die in self.group:
            Dice.rollDie(die)

#########################
# Example dice creation #
#########################
'''
#Two dice, one white, one red, no group of dice
die1=Dice("tan",30,100,100)
die2=Dice("saddlebrown",30,200,200)
for i in range(2):
    die1.rollDie()
    die2.rollDie()
    input('All dice have been rolled. Press enter to roll again: ')


#2 groups of dice
whiteDice=groupOfDice(2,"tan",30,5,7,1)
brownDice=groupOfDice(2,"saddlebrown",30,6.5,7,1)
x = input('Press enter to start rolling: ')
while x == '':
    whiteDice.rollGroup()
    brownDice.rollGroup()
    x = input('All groups of dice have been rolled. Press enter to roll again: ')
'''
