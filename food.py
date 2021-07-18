from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("indigo")
        self.speed("fastest")
        self.disappear()

    def disappear(self):
        """
        once the snake make contact with food it appear
        on a different part of the screen
        """
        x_cor = random.randint(-270, 270)
        y_cor = random.randint(-270, 270)
        self.goto(x_cor, y_cor)
