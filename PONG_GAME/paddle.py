# Import the Turtle module
from turtle import Turtle

# Create a Paddle class that inherits from Turtle
class Paddle(Turtle):
    # Initialize the paddle with a specified position
    def __init__(self, position):
        # Call the constructor of the superclass (Turtle)
        super().__init__()

        # Move the paddle to the specified position
        self.goto(position)

        # Set up the paddle appearance
        self.shape("square")
        self.color("white")
        self.penup()

        # Set the orientation of the paddle to face upwards
        self.setheading(90)

        # Stretch the paddle size to make it look like a rectangle
        self.turtlesize(stretch_wid=1, stretch_len=5)

    # Method to move the paddle upward
    def move_up(self):
        # Move the paddle forward by 20 units
        self.forward(20)

    # Method to move the paddle downward
    def move_down(self):
        # Move the paddle backward by 20 units
        self.backward(20)

