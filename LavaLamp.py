from turtle import *
import random
import math
import time
bgcolor('black')
setup(width = 1.0, height = 1.0, startx = None, starty = None)
setworldcoordinates(0,0,1000,1000)
delay(0)
colormode(255)

def findY(x,a,b,c):
    #(500+(-0.008)((x-500)^2))*(sin(((2*\pi)/\left(500+a\right)+b)(x+500+c)))
    quad = (250+(-0.004)*((x-500)**2))
    sin = (math.sin(((2*math.pi)/(500+a)+b)*(x+500+c)))
    return math.fabs(quad * sin) - 20

def drawWave(turtle,a,b,c):
    turtle.pu()
    turtle.goto(250,-50)
    turtle.fill(True)
    count = 250
    while count < 750:
        turtle.goto(count, findY(count,a,b,c))
        count = count + 1
    turtle.goto(750,-50)
    turtle.fill(False)

def waveFrame():
    global a,b,c,reverse
    if reverse == 1:
        a = a + 1
        b = b + .000001
        c = c + 1
        if a >= 300:
            reverse = reverse * -1
    if reverse == -1:
        a = a + -1
        b = b + -.000001
        c = c + -1
        if a <= -300:
            reverse = reverse * -1
    for i in range(len(objs)):
        drawWave(objs[i],a,b,c)
        objs[i-1].clear()

def travelUp(turtle1, turtle2, circleSize):
    global x1,y1,circleSize1
    if turtle1.ycor() > 1000+2*circleSize:
        turtle1.goto(random.randint(250,750),-2*circleSize)
        turtle1.dot(circleSize)
        x1 = turtle1.xcor()
        y1 = turtle1.ycor()
        circleSize1 = random.randint(50,150)
    #time.sleep(.005)
    turtle1.goto(x1,y1)
    turtle1.dot(circleSize)
    turtle2.clear()
    y1 = y1 + 1
    x1 = x1 + .5 * random.randint(-1,1)
    turtle2.goto(x1, y1)
    turtle2.dot(circleSize)
    turtle1.clear()

def travelUp1(turtle1, turtle2, circleSize):
    global x11,y11,circleSize11
    if turtle1.ycor() > 1000+2*circleSize:
        turtle1.goto(random.randint(250,750),-2*circleSize)
        turtle1.dot(circleSize)
        x11 = turtle1.xcor()
        y11 = turtle1.ycor()
        circleSize11 = random.randint(50,150) 
    #time.sleep(.005)
    turtle1.goto(x11,y11)
    turtle1.dot(circleSize)
    turtle2.clear()
    y11 = y11 + 1
    x11 = x11 + .5 * random.randint(-1,1)
    turtle2.goto(x11, y11)
    turtle2.dot(circleSize)
    turtle1.clear()

def travelUp2(turtle1, turtle2, circleSize):
    global x111,y111,circleSize111
    if turtle1.ycor() > 1000+2*circleSize:
        turtle1.goto(random.randint(250,750),-2*circleSize)
        turtle1.dot(circleSize)
        x111 = turtle1.xcor()
        y111 = turtle1.ycor()
        circleSize111 = random.randint(50,150)
    #time.sleep(.005)
    turtle1.goto(x111,y111)
    turtle1.dot(circleSize)
    turtle2.clear()
    y111 = y111 + 1
    x111 = x111 + .5 * random.randint(-1,1)
    turtle2.goto(x111, y111)
    turtle2.dot(circleSize)
    turtle1.clear()

def travelUp3(turtle1, turtle2, circleSize):
    global x1111,y1111,circleSize1111
    if turtle1.ycor() > 1000+2*circleSize:
        turtle1.goto(random.randint(250,750),-2*circleSize)
        x1111 = turtle1.xcor()
        y1111 = turtle1.ycor()
        circleSize1111 = random.randint(50,150)
        turtle1.dot(circleSize1111)
    #time.sleep(.005)
    turtle1.goto(x1111,y1111)
    turtle1.dot(circleSize)
    turtle2.clear()
    y1111 = y1111 + 1
    x1111 = x1111 + .5 * random.randint(-1,1)
    turtle2.goto(x1111, y1111)
    turtle2.dot(circleSize)
    turtle1.clear()

objs = list()
for i in range(2):
    objs.append(Turtle())
    objs[i].radians()
    objs[i].speed(0)
    objs[i].pencolor(255,255,255)
    objs[i].fillcolor(255,255,255)
    objs[i].pu()
    objs[i].ht()

objs1 = list()
for i in range(2):
    objs1.append(Turtle())
    objs1[i].radians()
    objs1[i].speed(0)
    objs1[i].pencolor(255,255,255)
    objs1[i].fillcolor(255,255,255)
    objs1[i].pu()
    objs1[i].ht()
    
objs2 = list()
for i in range(2):
    objs2.append(Turtle())
    objs2[i].radians()
    objs2[i].speed(0)
    objs2[i].pencolor(255,255,255)
    objs2[i].fillcolor(255,255,255)
    objs2[i].pu()
    objs2[i].ht()
    
objs3 = list()
for i in range(2):
    objs3.append(Turtle())
    objs3[i].radians()
    objs3[i].speed(0)
    objs3[i].pencolor(255,255,255)
    objs3[i].fillcolor(255,255,255)
    objs3[i].pu()
    objs3[i].ht()

objs4 = list()
for i in range(2):
    objs4.append(Turtle())
    objs4[i].radians()
    objs4[i].speed(0)
    objs4[i].pencolor(255,255,255)
    objs4[i].fillcolor(255,255,255)
    objs4[i].pu()
    objs4[i].ht()

objs1[0].goto(random.randint(250,750),-50)
objs1[0].dot(50)
x1 = objs1[0].xcor()
y1 = objs1[0].ycor()
circleSize1 = random.randint(50,150)

objs2[0].goto(random.randint(250,750),-50)
objs2[0].dot(50)
x11 = objs2[0].xcor()
y11 = objs2[0].ycor()
circleSize11 = random.randint(50,150)

objs3[0].goto(random.randint(250,750),-50)
objs3[0].dot(50)
x111 = objs3[0].xcor()
y111 = objs3[0].ycor()
circleSize111 = random.randint(50,150)

objs4[0].goto(random.randint(250,750),-50)
objs4[0].dot(50)
x1111 = objs4[0].xcor()
y1111 = objs4[0].ycor()
circleSize1111 = random.randint(50,150)

a = 0
b = 0
c = 0
reverse = -1

##r = objs[0].fillcolor()[0]
##g = objs[0].fillcolor()[1]
##b = objs[0].fillcolor()[2]
colorR = random.randint(0,255)
colorG = random.randint(0,255)
colorB = random.randint(0,255)

def changeColor(turtleList):
    global reverse, colorR, colorG, colorB
    r = turtleList[0].fillcolor()[0]
    g = turtleList[0].fillcolor()[1]
    b = turtleList[0].fillcolor()[2]
    for i in range(2):
        if colorR > turtleList[i].fillcolor()[0]:
            r = r + 1
        if colorR < turtleList[i].fillcolor()[0]:
            r = r - 1
        if colorG > turtleList[i].fillcolor()[1]:
            g = g + 1
        if colorG < turtleList[i].fillcolor()[1]:
            g = g - 1
        if colorB > turtleList[i].fillcolor()[2]:
            b = b + 1
        if colorB < turtleList[i].fillcolor()[2]:
            b = b - 1
        turtleList[i].color((r,g,b),(r,g,b))
    if turtleList[0].fillcolor()[0] == colorR and turtleList[0].fillcolor()[1] == colorG and turtleList[0].fillcolor()[2] == colorB:
        colorR = random.randint(0,255)
        colorG = random.randint(0,255)
        colorB = random.randint(0,255)
    

while True:
    for i in range(4000):
        waveFrame()
        travelUp(objs1[0],objs1[1], circleSize1)
        if i % 2:
            travelUp1(objs2[0],objs2[1], circleSize11)
        if i % 3:
            travelUp2(objs3[0],objs3[1], circleSize111)
        if i % 4:
            travelUp3(objs4[0],objs4[1], circleSize1111)
        if i % 5:
            changeColor(objs4)
            changeColor(objs3)
            changeColor(objs2)
            changeColor(objs1)
            changeColor(objs)
