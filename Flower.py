import turtle

# Create a Turtle screen
screen = turtle.Screen()
screen.bgcolor("white")

# Create a Turtle object
flower = turtle.Turtle()
flower.shape("turtle")
flower.color("red")
flower.speed(1)

# Function to draw a petal
def draw_petal():
    flower.circle(100, 60)
    flower.left(120)
    flower.circle(100, 60)
    flower.left(120)

# Function to draw a flower
def draw_flower():
    for _ in range(6):
        draw_petal()
        flower.left(60)

# Move the pen to the starting position
flower.penup()
flower.goto(0, -100)
flower.pendown()

# Draw the flower
draw_flower()

# Close the drawing window when clicked
screen.exitonclick()
