from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = -1
        self.level_update()
    def game_over(self):
        self.goto(0,0)
        self.write(arg="Game Over", move=False, align='center', font=FONT)

    def level_update(self):
        self.level += 1
        self.penup()
        self.goto(-250, 250)
        self.clear()
        self.write(arg=f"Level: {self.level}", move=False, align='left', font=FONT)



