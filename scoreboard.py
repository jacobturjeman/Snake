from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.clear()
        self.hideturtle()
        self.goto(-100, 270)
        self.color("white")
        self.current = 0
        self.read()
        self.update()

    def update(self):
        """
        reads the file to get the highscore and clears the screen,
        displays the current score and the highscore
        """
        self.read()
        self.clear()
        self.write(f"Score : {self.current}, highscore : {self.highscore}", font=("Arial", 18, "normal"))

    def write_score(self):
        """
        write the score to the data.txt file, rewrite highscore
        """
        with open("data.txt", mode="w") as text:
            text.write(self.current.__str__())

    def read(self):
        """
        reads the highscore from the data.txt file
        """
        with open("data.txt", mode="r") as text:
            self.highscore = int(text.read())

    def reset_game(self):
        """
        whenever the snake collides either with the edge of
        the screen or with itself sets the score back to 0
        and if the score was higher than the high score,
        rewrite the highscore file
        """
        if self.current > self.highscore:
            self.write_score()
        self.current = 0
        self.update()

    def raise_score(self):
        """
        when the snake collide with 'food'
        gains a point
        """
        self.current += 1
        if self.current > self.highscore:
            self.write_score()
        self.update()


