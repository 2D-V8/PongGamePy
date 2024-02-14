# Import the Turtle module
from turtle import Turtle

# Create a Ball class that inherits from Turtle
class Ball(Turtle):
    # Initialize the ball object
    def __init__(self):
        # Call the constructor of the superclass (Turtle)
        super().__init__()

        # Set up the ball appearance
        self.shape("circle")
        self.penup()
        self.color("white")

        # Place the ball at the home position
        self.home()

        # Set the initial heading of the ball
        self.setheading(60)

        # Set the initial movement values for x and y directions
        self.x_move = 10
        self.y_move = 10

        # Set the initial movement speed of the ball
        self.move_speed = 0.1

    # Method to move the ball
    def move(self):
        # Calculate the new position of the ball
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        # Move the ball to the new position
        self.goto(new_x, new_y)

    # Method to bounce the ball in the y direction
    def bounce_y(self):
        # Reverse the y direction of the ball
        self.y_move *= -1
        # Adjust the movement speed to make the game progressively faster
        self.move_speed *= 0.9

    # Method to bounce the ball in the x direction
    def bounce_x(self):
        # Reverse the x direction of the ball
        self.x_move *= -1
        # Adjust the movement speed to make the game progressively faster
        self.move_speed *= 0.9

    # Method to reset the ball to the home position
    def reset(self):
        self.home()




