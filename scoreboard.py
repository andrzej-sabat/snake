from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.score = 0
        with open("data.txt", mode="r") as file:
            self.highscore = int(file.read())
        self.update_scoreboard()

    def reset(self):
        if self.score > self.highscore:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))
            self.highscore = self.score
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """Update scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def add_point_to_score(self):
        """Add point to score count"""
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #   """Display GAME OVER"""
    #   self.goto(0,0)
    #   self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))
