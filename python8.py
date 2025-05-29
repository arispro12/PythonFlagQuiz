import random
import turtle

scn = turtle.Screen()
t = turtle.Turtle()
turtle.title("Flags with t")
turtle.bgcolor("white")
t.shape("turtle")
t.speed("fast")


def estonia():
    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -60)
    t.pd()

    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()


def japan():
    t.fillcolor("black")
    t.begin_fill()

    for i in range(4):
        t.fd(200)
        t.rt(90)
        t.end_fill()

    t.pu()
    t.goto(100, -140)
    t.pd()
    t.fillcolor("red")
    t.begin_fill()
    t.circle(50)
    t.end_fill()  #@# @22
def germany():
    t.fillcolor("black")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -60)
    t.pd()

    t.fillcolor("yellow")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()
def russia():
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -60)
    t.pd()

    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()
def poland():
    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()
def armenia():
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -60)
    t.pd()

    t.fillcolor("orange")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()
def netherlands():
    t.fillcolor("red")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(50)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -30)
    t.pd()

    t.fillcolor("white")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.pu()
    t.goto(0, -60)
    t.pd()

    t.fillcolor("blue")
    t.begin_fill()
    for i in range(2):
        t.fd(150)
        t.rt(90)
        t.fd(30)
        t.rt(90)
    t.end_fill()

    t.hideturtle()


t.hideturtle()
#estonia()
#japan()
#germany()
#russia()
#poland()
#armenia()
#netherlands

flags = [estonia, japan, germany, russia, poland, armenia, netherlands]


life=3
points=0

while life > 0 and len(flags) > 0:
    t.reset()
    flagchoice=random.choice(flags)
    flagchoice()
    answer=input("What's the flag?")

    flags.remove(flagchoice)

    if answer == flagchoice.__name__:
        print("Bravo!")
        points = points+1
        print("Your points:", points)
        print("Your lives:", life)
    else:
        print("No!")
        life = life - 1
        print("Your points:", points)
        print("Your lives:", life)
    if life==0:
        turtle.bye()
        print("you lost!")
turtle.done()
