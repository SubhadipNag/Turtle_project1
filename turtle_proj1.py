#1 Rainbow design turtle python project
import turtle

t = turtle.Pen()
s = turtle.Screen()
colors = ['red', 'purple', 'blue', 'green', 'orange', 'white', 'yellow']
s.bgcolor('black')
t.speed('fastest')
turtle.bgcolor('black')
for x in range(360):
    t.pencolor(colors[x%6])
    t.width(x/100 + 1)
    t.forward(x)
    t.left(59)
    t.speed(15)


