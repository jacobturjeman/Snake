from turtle import Screen, Turtle
import time
from snake import Snake
import food
import scoreboard


def raise_level():
    """
    a function that checks the score of the player,
    the higher the score the faster the snake advances
    """
    screen.delay()
    if score.current <= 5:
        return 0.1
    elif 10 >= score.current > 5:
        return 0.05
    elif 20 >= score.current > 10:
        return 0.008


# setting up the screen and title
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake OG")
screen.delay(0)

# the first layout of the snake and food as well as
# creating the scoreboard
snake = Snake()
snake.start_positioning()
food = food.Food()
score = scoreboard.Scoreboard()
# key mapping for the game
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

end = False
while not end:
    screen.update()
    time.sleep(raise_level())
    snake.moving()
    # if the snake head comes in range of 15 pixels from the food,
    # scores a point, reappearance of the food and extension of the snake
    if snake.head.distance(food) < 15:
        food.disappear()
        score.raise_score()
        snake.eating()
    # if the snake head x,y coordinates reaches the edges of the screen
    # resets the current score and the snake proportion
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        score.reset_game()
        snake.reset_game()
    # detects if the snake collides with it self, if so reset score and snake proportion
    for cube in snake.snake_body[1:]:
        if snake.head.position() == cube.position():
            score.reset_game()
            snake.reset_game()
screen.exitonclick()
