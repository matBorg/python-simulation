import turtle
from random import randint
import random
b1 = turtle.Screen()
b1.bgcolor("black")
b1.title("Bouncing things")
b1.tracer(0)
balls = []
colors = ["green", "white", "purple", "yellow", "red", "blue", "orange"]
shapes = ["circle", "triangle", "square"]
for _ in range(randint(0, 1000)):
	balls.append(turtle.Turtle())
for ball in balls:
	ball.shape(random.choice(shapes))
	ball.color(random.choice(colors))
	ball.penup()
	ball.speed(0)
	x = randint(-290, 290)
	y = randint(200, 400)
	ball.goto(x, y)
	ball.dy = 0
	ball.dx = randint(-3, 3)
	ball.da = randint(-3, 3)
g = 0.98
while True:
	b1.update()
	for ball in balls:
		ball.rt(ball.da )
		ball.dy-=g
		ball.sety(ball.ycor()+ball.dy)
		ball.setx(ball.xcor()+ball.dx)
		if ball.ycor() < -300:
			ball.dy *= -1
		if ball.xcor() > 300 or ball.xcor()< -300:
			ball.dx *= -1

b1.mainloop()