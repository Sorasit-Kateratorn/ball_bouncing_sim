import turtle
import ball_oop


class Run:
    def __init__(self):
        self.num_balls = int(input("Number of balls to simulate: "))
        turtle.speed(0)
        turtle.tracer(0)
        turtle.hideturtle()
        self.canvas_width = turtle.screensize()[0]
        self.canvas_height = turtle.screensize()[1]
        self.ball_radius = 0.05 * self.canvas_width
        turtle.colormode(255)
        self.ball = ball_oop.BallManager(
            self.canvas_width, self.canvas_height, self.ball_radius, self.num_balls)

    def main(self):
        while (True):
            turtle.clear()
            for i in range(self.num_balls):
                self.ball.draw_circle(i)
                self.ball.move_circle(i)
            turtle.update()
        turtle.done()


start = Run()
start.main()
