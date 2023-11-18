import turtle
import random


class BallManager:
    def __init__(self, canvas_width, canvas_height, ball_radius, num_balls) -> None:
        self.xpos = []
        self.ypos = []
        self.vx = []
        self.vy = []
        self.ball_color = []
        self.canvas_width = canvas_width
        self.canvas_height = canvas_height
        self.ball_radius = ball_radius
        self.num_balls = num_balls

        for _ in range(num_balls):
            self.xpos.append(random.randint(-1*canvas_width +
                             ball_radius, canvas_width - ball_radius))
            self.ypos.append(random.randint(-1*canvas_height +
                             ball_radius, canvas_height - ball_radius))
            self.vx.append(random.randint(1, int(0.01*canvas_width)))
            self.vy.append(random.randint(1, int(0.01*canvas_height)))
            self.ball_color.append(
                (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)))

    def move_circle(self, i):
        for i in range(self.num_balls):
            # update the x, y coordinates of ball i with velocity in the x (vx) and y (vy) components
            self.xpos[i] += self.vx[i]
            self.ypos[i] += self.vy[i]

            # if the ball hits the side walls, reverse the vx velocity
            if abs(self.xpos[i] + self.vx[i]) > (self.canvas_width - self.ball_radius):
                self.vx[i] = -self.vx[i]

            # if the ball hits the ceiling or the floor, reverse the vy velocity
            if abs(self.ypos[i] + self.vy[i]) > (self.canvas_height - self.ball_radius):
                self.vy[i] = -self.vy[i]

    def draw_circle(self, i):
        for i in range(self.num_balls):
            # draw a circle of radius equals to size at x, y coordinates and paint it with color
            turtle.penup()
            turtle.color(self.ball_color[i])
            turtle.fillcolor(self.ball_color[i])
            turtle.goto(self.xpos[i], self.ypos[i])
            turtle.pendown()
            turtle.begin_fill()
            turtle.circle(self.ball_radius)
            turtle.end_fill()


def main():
    canvas_width = 800
    canvas_height = 600
    ball_radius = 20
    num_balls = 3

    turtle.speed(0)
    turtle.hideturtle()
    turtle.bgcolor("white")
    turtle.title("Bouncing Balls")

    ball_manager = BallManager(
        canvas_width, canvas_height, ball_radius, num_balls)

    for _ in range(100):
        ball_manager.move()
        ball_manager.draw()

    turtle.done()


if __name__ == "__main__":
    main()
