import turtle

turtle.bgcolor("black")
turtle.speed(3) 

def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

draw_circle(300, "red")

turtle.penup()
turtle.goto(0, -260)
turtle.pendown()
draw_circle(260, "white")

turtle.penup()
turtle.goto(0, -220)
turtle.pendown()
draw_circle(220, "red")

turtle.penup()
turtle.goto(0, -180)
turtle.pendown()
draw_circle(180, "blue")

turtle.penup()
turtle.goto(-170, 65)
turtle.setheading(0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()

for i in range(5):
    turtle.forward(340)
    turtle.right(144)

turtle.end_fill()

turtle.hideturtle()

turtle.done()