from turtle import Turtle
SPEED = 20
DIRECTIONS = [0, 90, 180, 270]


class Snake:
    def __init__(self):
        self.snake_body = []
        self.x_axis = 0

    def start_positioning(self):
        """
        first, this function creates and appends objects in the shape
        of squares to the list created in the init.
        secondly, after setting up the color, place the first cell
        of the list, afterwards places the next cell right next to it by only changing
        the x axis coordinate of the next cell and so on.
        """
        self.x_axis = 0
        for i in range(3):
            self.snake_body.append(Turtle(shape="square"))
        for cell in range(len(self.snake_body)):
            self.snake_body[cell].penup()
            self.snake_body[cell].color("white")
            self.snake_body[cell].setposition(x=self.x_axis, y=self.snake_body[cell].ycor())
            self.x_axis -= 20
        self.head = self.snake_body[0]

    def moving(self):
        """
        moves each of the snake blocks one by one by making the blocks
        follow the first block(the snake head) and only move it.
        """
        for cube in range(len(self.snake_body) - 1, 0, -1):
            self.snake_body[cube].color("white")
            n_x_axis = self.snake_body[cube - 1].xcor()
            n_y_axis = self.snake_body[cube - 1].ycor()
            self.snake_body[cube].goto(n_x_axis, n_y_axis)
        self.head.forward(SPEED)

# matching functions to the key mappings on 'main file' = controllers
    def up(self):
        if self.head.heading() != 270:
            self.head.setheading(90)

    def down(self):
        if self.head.heading() != 90:
            self.head.setheading(270)

    def left(self):
        if self.head.heading() != 0:
            self.head.setheading(180)

    def right(self):
        if self.head.heading() != 180:
            self.head.setheading(0)

    def eating(self):
        """
        extending the snake by one block for each
        pill it eats
        """
        self.snake_body.append(Turtle(shape="square"))
        self.snake_body[-1].penup()

    def reset_game(self):
        """
        when the game resets sends the snake off the screen and then
        erase it, only afterwards sends it back to its starting position(0,0)
        """
        for _ in self.snake_body:
            _.goto(1000, 1000)
        self.snake_body.clear()
        self.start_positioning()
