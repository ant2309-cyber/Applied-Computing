import turtle
wn = turtle.Screen()
tom = turtle.Turtle()

def triangle(length):
    for a in range (3):
        tom.forward(length)
        tom.right(120)
    wn.exitonclick()
triangle(80)
