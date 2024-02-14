# Import necessary modules

from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from score_board import Score_board
import time

# Set up the screen for the Pong game
screen= Screen()
screen.bgcolor("black")
screen.title("PONG")
screen.setup(width=800, height= 600)


# Create the ball object
ball = Ball()

# Turn off automatic screen updates
screen.tracer(0)


# Create left and right paddles
l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))

# Listen for keyboard inputs to control the paddles
screen.listen()
screen.onkey(key="w", fun=l_paddle.move_up)
screen.onkey(key="s",fun=l_paddle.move_down)
screen.onkey(key="Up", fun=r_paddle.move_up)
screen.onkey(key="Down",fun=r_paddle.move_down)

# Create the score board
score_board = Score_board()

# Set the initial game state to True
game_is_on =True
# Main game loop
while game_is_on:
    # Pause for a short time to control the speed of the ball
    time.sleep(ball.move_speed)
    # Move the ball
    ball.move()

    # Check for collisions with the left and right paddles, and bounce the ball
    if (ball.distance(l_paddle) < 50 and l_paddle.xcor() - 20 < ball.xcor() < l_paddle.xcor() + 20) or \
            (ball.distance(r_paddle) < 50 and r_paddle.xcor() - 20 < ball.xcor() < r_paddle.xcor() + 20):
        ball.bounce_x()

    # Check for collisions with the top and bottom walls, and bounce the ball
    if  ball.ycor() > 295 or ball.ycor() < -295:
            ball.bounce_y()

    # Check if the ball passed the left paddle, reset and update the score for the right player
    if ball.xcor() < -380:
        ball.reset()
        ball.bounce_x()
        score_board.r_point()

    # Check if the ball passed the right paddle, reset and update the score for the left player
    if  ball.xcor() > 380 :
        ball.reset()
        ball.bounce_x()
        score_board.l_point()




    screen.update()






screen.exitonclick()
