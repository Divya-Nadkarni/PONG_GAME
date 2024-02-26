from turtle import Screen,Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

screen=Screen()
screen.setup(width=800,height=600)
screen.bgcolor("black")
screen.title("The pong game")
screen.tracer(0)

l_paddle=Paddle((-350,0))
r_paddle=Paddle((350,0))
ball=Ball()
scoreboard=Scoreboard()


screen.listen()
screen.onkey(r_paddle.goup,"Up")
screen.onkey(r_paddle.godown,"Down")
screen.onkey(l_paddle.goup,"w")
screen.onkey(l_paddle.godown,"s")

is_game_on=True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    #Detect collision with paddle
    if ball.distance(r_paddle)<50 and ball.xcor() > 320 or ball.distance(l_paddle)<50 and ball.xcor() < -320:
        ball.bounce_x()
 
    #detect ball misses
    elif ball.xcor()>370:
        ball.reset_position()
        scoreboard.l_point()

    elif ball.xcor()<-370:
        ball.reset_position()
        scoreboard.r_point()
    
screen.exitonclick()