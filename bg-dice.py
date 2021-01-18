import turtle
import random
import time

##############
# Single die #
##############
class Dice:
    def __init__(self,color,size,ulx,uly):
        self.color=color
        self.size=size
        self.upperLeftX=ulx
        self.upperLeftY=uly
        self.wn=turtle.Screen()
        self.t=turtle.Turtle()
        self.t.color('black',color)
        self.t.hideturtle()
        self.t.up()
        self.t.goto(self.upperLeftX,self.upperLeftY)
        self.t.down()
        self.value=0
        self.drawDie()

    def drawDie(self):
        self.t.begin_fill()
        for x in range(4):
            self.t.fd(self.size)
            self.t.right(90)
        self.t.end_fill()
        self.t.up()
        self.t.goto(self.upperLeftX+self.size/2.25,self.upperLeftY-self.size/1.3)
        if self.value != 0:
            self.t.write(str(self.value),font=('Arial','14','normal'))        
    
    def rollDie(self):
        self.value = random.randint(1,6)
        self.t.up()
        self.t.goto(self.upperLeftX,self.upperLeftY)
        self.t.down()
        self.drawDie()

#################
# Group of dice #
#################
class groupOfDice(Dice):
    def __init__(self,number,color,size,firstX,Y,xInterval):
        self.group=[]
        self.xInterval=xInterval
        self.startLeft=firstX
        self.size=size
        x=firstX
        for i in range(1,number+1):
            self.group.append(Dice(color,size,self.startLeft,Y))
            self.startLeft += (size + self.xInterval)
        
    def rollGroup(self):
        for die in self.group:
            Dice.rollDie(die)

########
# Main #
########
def main():
    #Two dice, one white, one red, no group of dice
    die1=Dice("tan",30,100,100)
    die2=Dice("saddlebrown",30,200,200)
    for i in range(2):
        die1.rollDie()
        die2.rollDie()
        input('All dice have been rolled. Press enter to roll again: ')

    #2 groups of dice
    print("\n")
    attackDice=groupOfDice(3,"salmon",30,-60,280,10)
    defendDice=groupOfDice(3,"lightblue",30,-60,240,10)
    x = input('Press enter to start rolling: ')
    while x == '':
        attackDice.rollGroup()
        defendDice.rollGroup()
        x = input('All groups of dice have been rolled. Press enter to roll again: ')
        
main()
