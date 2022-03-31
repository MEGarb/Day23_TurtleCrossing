from turtle import Turtle


FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.goto(-250, 260)
        self.level = 1
        self.update_scoreboard()


        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Level:  {self.level}", font=FONT)

    def gameover(self):
        self.goto(0, 0)
        self.color("red")
        self.write(f"GAME OVER", align="center",font=FONT)

        print("turt squished")

    def level_up(self):
        self.level += 1
        self.update_scoreboard()
