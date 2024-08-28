import turtle
import random

# Set up the screen
win = turtle.Screen()
win.title("Advanced Pong")
win.setup(width=800, height=600)
win.tracer(0)  # Stops the window from updating automatically

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.color("white")
paddle_a.shapesize(stretch_wid=6, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.color("white")
paddle_b.shapesize(stretch_wid=6, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.speed(1)
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.175  # Ball movement speed along x
ball.dy = -0.175  # Ball movement speed along y

# Score
score_a = 0
score_b = 0

# Obstacles
obstacles = []

# Paddle movement flags
paddle_a_up_flag = False
paddle_a_down_flag = False
paddle_b_up_flag = False
paddle_b_down_flag = False


def create_obstacles():
    for _ in range(3):  # Add three obstacles each round
        obstacle_type = random.choice(["red_square", "fog_patch", "mirror_line", "extra_ball"])
        obstacle = turtle.Turtle()
        obstacle.speed(0)
        obstacle.penup()

        if obstacle_type == "red_square":
            obstacle.shape("square")
            obstacle.color("red")
            obstacle.shapesize(stretch_wid=2, stretch_len=2)
            x = random.randint(-200, 200)
            y = random.randint(-150, 150)
            obstacle.goto(x, y)

        elif obstacle_type == "fog_patch":
            obstacle.shape("circle")
            obstacle.color("gray")
            obstacle.shapesize(stretch_wid=4, stretch_len=4)
            obstacle.color((0.5, 0.5, 0.5))  # Semi-transparent
            x = random.randint(-200, 200)
            y = random.randint(-150, 150)
            obstacle.goto(x, y)

        elif obstacle_type == "mirror_line":
            obstacle.shape("square")
            obstacle.color("blue")
            obstacle.shapesize(stretch_wid=0.5, stretch_len=15)
            x = 0
            y = random.randint(-200, 200)
            obstacle.goto(x, y)

        elif obstacle_type == "extra_ball":
            obstacle.shape("circle")
            obstacle.color("yellow")
            obstacle.shapesize(stretch_wid=1.5, stretch_len=1.5)
            x = random.randint(-200, 200)
            y = random.randint(-150, 150)
            obstacle.goto(x, y)
            obstacle.dx = random.choice([-0.15, 0.15])
            obstacle.dy = random.choice([-0.15, 0.15])
            obstacles.append(obstacle)
            continue

        obstacles.append(obstacle)


def clear_obstacles():
    for obstacle in obstacles:
        obstacle.hideturtle()
    obstacles.clear()


# Scoreboard
score_display = turtle.Turtle()
score_display.speed(0)
score_display.color("white")
score_display.penup()
score_display.hideturtle()
score_display.goto(0, 260)
score_display.write("Player A: 0  Player B: 0", align="center", font=("Courier", 24, "normal"))


# Function to update the scoreboard
def update_score():
    score_display.clear()
    score_display.write("Player A: {}  Player B: {}".format(score_a, score_b), align="center",
                        font=("Courier", 24, "normal"))


# Paddle movement functions
def paddle_a_up():
    global paddle_a_up_flag
    paddle_a_up_flag = True


def paddle_a_down():
    global paddle_a_down_flag
    paddle_a_down_flag = True


def paddle_a_up_release():
    global paddle_a_up_flag
    paddle_a_up_flag = False


def paddle_a_down_release():
    global paddle_a_down_flag
    paddle_a_down_flag = False


def paddle_b_up():
    global paddle_b_up_flag
    paddle_b_up_flag = True


def paddle_b_down():
    global paddle_b_down_flag
    paddle_b_down_flag = True


def paddle_b_up_release():
    global paddle_b_up_flag
    paddle_b_up_flag = False


def paddle_b_down_release():
    global paddle_b_down_flag
    paddle_b_down_flag = False


def increase_ball_speed():
    ball.dx *= 1.2
    ball.dy *= 1.2


def decrease_ball_speed():
    ball.dx *= 0.8
    ball.dy *= 0.8


# Function to reset the ball and start a new round
def reset_ball():
    ball.goto(0, 0)
    ball.dx = 0.175 if random.choice([True, False]) else -0.175
    ball.dy = 0.175 if random.choice([True, False]) else -0.175
    clear_obstacles()
    create_obstacles()
    change_background()


def change_background():
    colors = ["black", "darkblue", "darkred", "darkgreen", "purple", "darkorange"]
    win.bgcolor(random.choice(colors))


# Keyboard bindings
win.listen()
win.onkeypress(paddle_a_up, "w")
win.onkeyrelease(paddle_a_up_release, "w")
win.onkeypress(paddle_a_down, "s")
win.onkeyrelease(paddle_a_down_release, "s")
win.onkeypress(paddle_b_up, "Up")
win.onkeyrelease(paddle_b_up_release, "Up")
win.onkeypress(paddle_b_down, "Down")
win.onkeyrelease(paddle_b_down_release, "Down")
win.onkeypress(increase_ball_speed, "p")
win.onkeypress(decrease_ball_speed, "l")

# Main game loop
while True:
    win.update()

    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move the paddles
    if paddle_a_up_flag and paddle_a.ycor() < 250:
        paddle_a.sety(paddle_a.ycor() + 3)  # Slower movement speed
    if paddle_a_down_flag and paddle_a.ycor() > -240:
        paddle_a.sety(paddle_a.ycor() - 3)  # Slower movement speed
    if paddle_b_up_flag and paddle_b.ycor() < 250:
        paddle_b.sety(paddle_b.ycor() + 3)  # Slower movement speed
    if paddle_b_down_flag and paddle_b.ycor() > -240:
        paddle_b.sety(paddle_b.ycor() - 3)  # Slower movement speed

    # Move obstacles (if they are extra balls)
    for obstacle in obstacles:
        if hasattr(obstacle, 'dx'):
            obstacle.setx(obstacle.xcor() + obstacle.dx)
            obstacle.sety(obstacle.ycor() + obstacle.dy)
            if obstacle.ycor() > 290 or obstacle.ycor() < -290:
                obstacle.dy *= -1
            if obstacle.xcor() > 390 or obstacle.xcor() < -390:
                obstacle.dx *= -1

    # Border collision checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1

    if ball.xcor() > 390:
        score_a += 1
        update_score()
        reset_ball()

    if ball.xcor() < -390:
        score_b += 1
        update_score()
        reset_ball()

    # Paddle collision checking
    if (ball.dx > 0) and (350 > ball.xcor() > 340) and (paddle_b.ycor() + 50 > ball.ycor() > paddle_b.ycor() - 50):
        ball.setx(340)
        ball.dx *= -1

    if (ball.dx < 0) and (-350 < ball.xcor() < -340) and (paddle_a.ycor() + 50 > ball.ycor() > paddle_a.ycor() - 50):
        ball.setx(-340)
        ball.dx *= -1

    # Obstacle collision checking
    for obstacle in obstacles:
        if (obstacle.xcor() - 20 < ball.xcor() < obstacle.xcor() + 20) and (
                obstacle.ycor() - 20 < ball.ycor() < obstacle.ycor() + 20):
            ball.dx *= -1
            ball.dy *= -1
        if hasattr(obstacle, 'dx'):
            if (obstacle.xcor() - 20 < ball.xcor() < obstacle.xcor() + 20) and (
                    obstacle.ycor() - 20 < ball.ycor() < obstacle.ycor() + 20):
                ball.dx *= -1
                ball.dy *= -1
