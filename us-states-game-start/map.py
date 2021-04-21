from turtle import Turtle

class Map(Turtle):
    def __init__(self):
        super().__init__()
        self.position_x = 0
        self.position_y = 0
        self.hideturtle()
        self.penup()



    def get_position(self, position_x, position_y, state):
        self.hideturtle()
        self.penup()
        self.goto(position_x, position_y)
        self.write(f"{state}", align="center", font=("Arial", 8, "normal"))
