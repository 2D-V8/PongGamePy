# Import the Turtle module
from turtle import Turtle


# Create a Score_board class that inherits from Turtle
class Score_board(Turtle):
    # Initialize the score attributes and set up the Turtle object
    def __init__(self):
        # Initialize left and right scores to 0
        self.l_score = 0
        self.r_score = 0

        # Call the constructor of the superclass (Turtle)
        super().__init__()

        # Set up the Turtle appearance
        self.hideturtle()
        self.color("white")
        self.hideturtle()
        self.penup()

        # Update the score board on initialization
        self.update_score_board()

    # Method to update the score board display
    def update_score_board(self):
        # Clear the existing score display
        self.clear()

        # Move to the left position and display the left score
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Courier", 80, "normal"))

        # Move to the right position and display the right score
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Courier", 80, "normal"))

    # Method to update the right score and refresh the display
    def r_point(self):
        # Increment the right score
        self.r_score += 1
        # Update the score board
        self.update_score_board()

    # Method to update the left score and refresh the display
    def l_point(self):
        # Increment the left score
        self.l_score += 1
        # Update the score board
        self.update_score_board()

