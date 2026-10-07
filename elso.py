import turtle
import random

def fel():
    y = tihi.ycor()
    tihi.sety(y+5)

def le():
    y = tihi.ycor()
    tihi.sety(y-5)

def jobb():
    x = tihi.xcor()
    tihi.setx(x+5)

def bal():
    x = tihi.xcor()
    tihi.setx(x-5)

def penup():
    tihi.penup()

def pendown():
    tihi.pendown()

def tav():
    dx = tihi.xcor() - viktor.xcor()
    dy = tihi.ycor() - viktor.ycor()
    tavolsag = (dx ** 2 + dy ** 2) ** 0.5

    turtle.write(int(tavolsag))


def tor():
    turtle.clear()



def vfel():
    y = viktor.ycor()
    viktor.sety(y+5)

def vle():
    y = viktor.ycor()
    viktor.sety(y-5)

def vjobb():
    x = viktor.xcor()
    viktor.setx(x+5)

def vbal():
    x = viktor.xcor()
    viktor.setx(x-5)



ablak = turtle.Screen()
ablak.setup(600, 600)
ablak.bgcolor("lightgreen")

viktor = turtle.Turtle()
viktor.shape("turtle")
viktor.color("blue")
viktor.shapesize(2)
viktor.speed(5)

tihi = turtle.Turtle()
tihi.shape("turtle")
tihi.color("red")
tihi.shapesize(2)
tihi.speed(2)

ablak.listen()
ablak.onkeypress(fel, "Up")
ablak.onkeypress(le, "Down")
ablak.onkeypress(bal, "Left")
ablak.onkeypress(jobb, "Right")
ablak.onkeypress(penup,"l")
ablak.onkeypress(pendown, "k")
ablak.onkeypress(tav, "e")
ablak.onkeypress(tor, "r")

ablak.onkeypress(vfel, "w")
ablak.onkeypress(vle, "s")
ablak.onkeypress(vbal, "a")
ablak.onkeypress(vjobb, "d")



ablak.mainloop()












