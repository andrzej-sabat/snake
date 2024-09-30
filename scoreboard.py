from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as file:
            self.highscore = int(file.read())
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 275)
        self.update_scoreboard()



    def update_scoreboard(self):
        """Update scoreboard"""
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", align="center", font=("Arial", 15, "normal"))

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as file:
                file.write(f"{self.highscore}")
        self.score = 0
        self.update_scoreboard()

    def add_point_to_score(self):
        """Add point to score count"""
        self.score += 1
        self.update_scoreboard()

    # def game_over(self):
    #   """Display GAME OVER"""
    #   self.goto(0,0)
    #   self.write("GAME OVER", align="center", font=("Arial", 15, "normal"))
