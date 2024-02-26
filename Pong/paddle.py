from turtle import Turtle
class Paddle(Turtle):
    def __init__(self,position) -> None:
        super().__init__("square")
        self.color("white")
        self.penup()
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.goto(position)
    
    def goup(self):
        new_y=self.ycor()+20
        self.goto(self.xcor(),new_y)

    def godown(self):
        new_y=self.ycor()-20
        self.goto(self.xcor(),new_y)

