import turtle
wn = turtle.Screen()
tom = turtle.Turtle()

def Octagon(length):
    for a in range (12):
        tom.forward(length)
        tom.right(30)
    wn.exitonclick()
Octagon(80)