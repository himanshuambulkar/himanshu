
import turtle
import random
import time
bodies=[]
delay=0.1
sc=0
hs=0

# creating a screen
s=turtle.Screen()
s.title("Snake Game")
s.bgcolor("pink");# background color fill karne ke liye bgcolor fun hota hai.
s.setup(width=800,height=600)# size of screen

# creating a head
head=turtle.Turtle()
head.speed(0)
head.shape("circle")
head.color("red")
head.fillcolor("blue")
head.penup()
head.goto(0,0)
head.direction="stop"


# creating a food
food=turtle.Turtle()
food.speed(0)
food.shape("square")
food.color("blue")
food.fillcolor("green")
food.penup()
food.ht()# for hiding turtle ke liye
food.goto(200,200)
food.st()# for showing turtle

# creating a score board
sb=turtle.Turtle()
sb.penup()
sb.ht()
sb.goto(-400,370)
sb.write("Created by Himanshu Ambulkar")
sb.goto(-400,350)
sb.write("score:0      |     Highest Score:0")# to print a score on the screen for the first time

# creating a function for moving in all direction
def MoveUp():
    if head.direction!="down":
        head.direction="up"
def MoveDown():
    if head.direction!="up":
        head.direction="down"
def MoveLeft():
    if head.direction!="right":
        head.direction="left"
def MoveRight():
    if head.direction!="left":
        head.direction="right"
def MoveStop():
    head.direction="stop"

def Move():
    if head.direction=="up":
       y=head.ycor()
       head.sety(y+20)
    if head.direction=="down":
       y=head.ycor()
       head.sety(y-20)
    if head.direction=="left":
       x=head.xcor()
       head.setx(x-20)
    if head.direction=="right":
       x=head.xcor()
       head.setx(x+20)

# event handling
s.listen()
s.onkey(MoveUp,"Up")
s.onkey(MoveDown,"Down")
s.onkey(MoveLeft,"Left")
s.onkey(MoveRight,"Right")
s.onkey(MoveStop,"space")

#main loop
while True:
    s.update()# to update the screen
    #check collision with border
    if head.xcor()>390:
        head.setx(-390)
    if head.xcor()<-390:
        head.setx(390)
    if head.ycor()>290:
        head.sety(-290)
    if head.ycor()<-290:
        head.sety(290)
    # check collision with food
    if head.distance(food)<20:
       x=random.randint(-390,390)
       y=random.randint(-290,290)
       food.goto(x,y)
       #increase the body of snake
       body=turtle.Turtle()
       body.speed(0)
       body.penup()
       body.shape("square")
       body.color("red")
       bodies.append(body) #append fun new body in the list
       sc=sc+10000 #increase the score
       delay=delay-0.001 #increase a speed
       if sc>hs:
           hs=sc #update score
       sb.clear()
       sb.write("score:{}  |  highest score:{}".format(sc,hs))
     #move snake bodies
    for i in range(len(bodies)-1,0,-1):
        x=bodies[i-1].xcor()
        y=bodies[i-1].ycor()
        bodies[i].goto(x,y)
    if len(bodies)>0:
        x=head.xcor()
        y=head.ycor()
        bodies[0].goto(x,y)
    Move()

    #check collision
    for body in bodies:
        if body.distance(head)<20:
            time.sleep(1)
            head.goto(0,0)
            head.direction="stop"
            #hide bodies
            for body in bodies:
                body.ht()
            bodies.clear()
            sc=0
            delay=0.1
            sb.clear()
            sb.write("score:{}  |   highest score:{}".format(sc,hs))
        
    time.sleep(delay)
s.mainloop()















    



























