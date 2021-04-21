from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.total_states = 50
        self.hideturtle()
        self.penup()
        self.guessed_states = []

    def update_score(self, result):
        self.guessed_states.append(result.state.item())
        print(self.guessed_states)
        self.score += 1
        print(self.score)
