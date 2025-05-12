import turtle

# Set up the turtle screen
screen = turtle.Screen()
screen.bgcolor("white")  # You can change the background color

# Create a turtle object
pen = turtle.Turtle()

# Set the turtle's speed (optional)
pen.speed(2)

# Drawing a square
for _ in range(4):  # Repeat 4 times to create a square
    pen.forward(100)  # Move the turtle forward by 100 units
    pen.left(90)      # Turn the turtle left by 90 degrees

# Finish the drawing
turtle.done()
