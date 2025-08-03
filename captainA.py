import turtle

# Set up the screen
turtle.bgcolor("black")
turtle.speed(0) # Set speed to fastest

# Function to draw a filled circle
def draw_circle(radius, color):
    turtle.color(color)
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()

# Move to starting position for the first circle
turtle.penup()
turtle.goto(0, -300)
turtle.pendown()

# Draw the concentric circles
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

# Draw the star
turtle.penup()
turtle.goto(-170, 65) # Position the turtle to start the star
turtle.setheading(0)
turtle.pendown()
turtle.color("white")
turtle.begin_fill()

# Loop to draw the 5 points of the star
for i in range(5):
    turtle.forward(340)
    turtle.right(144)

turtle.end_fill()

# Hide the turtle cursor
turtle.hideturtle()

# Keep the window open
turtle.done()