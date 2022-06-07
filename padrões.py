import turtle

colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow','pink']

loadWindow = turtle.Screen()
turtle.speed(0)
turtle.pensize(2)

turtle.bgcolor('black')
turtle.color('white')

#turtle.goto(-50,-75)
for i in range(750):
    try:
        turtle.begin_fill()
        turtle.color(colors[i%5])
        turtle.fd(0+i)
        turtle.lt(70)
        turtle.end_fill()
    except:
        quit()

turtle.exitonclick()

