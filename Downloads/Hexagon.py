import turtle
wn = turtle.Screen()
tom = turtle.Turtle()

def Hexagon(length):
    for a in range (6):
        tom.forward(length)
        tom.right(60)
    wn.exitonclick()
Hexagon(80)
