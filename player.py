from turtle import Turtle


STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.left(90)
        self.goto(STARTING_POSITION)
        self.showturtle()

    def move(self):
        self.forward(MOVE_DISTANCE)

    def reset_pos(self):
        self.hideturtle()
        self.goto(STARTING_POSITION)
        self.showturtle()
