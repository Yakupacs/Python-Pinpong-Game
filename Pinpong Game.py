import turtle

pencere = turtle.Screen()
pencere.title("PinPong")
pencere.bgcolor("lightgray")
pencere.setup(width=800, height=600)
pencere.tracer(0)

raket_a = turtle.Turtle()
raket_a.speed(0)
raket_a.shape('square')
raket_a.color('red')
raket_a.penup()
raket_a.goto(-350, 0)
raket_a.shapesize(5, 1)

raket_b = turtle.Turtle()
raket_b.speed(0)
raket_b.shape('square')
raket_b.color('blue')
raket_b.penup()
raket_b.goto(350, 0)
raket_b.shapesize(5, 1)

ball = turtle.Turtle()
ball.speed(0)
ball.shape('circle')
ball.color('black')
ball.penup()
ball.dx = 0.15
ball.dy = 0.15

yazi = turtle.Turtle()
yazi.speed(0)
yazi.color('black')
yazi.penup()
yazi.goto(0, 250)
yazi.write("OyuncuA:0   OyuncuB:0", align='center', font=('Courier', 24, "bold"))
yazi.hideturtle()
puan_a = 0
puan_b = 0

def raket_a_up():
    y = raket_a.ycor()
    y = y + 25
    raket_a.sety(y)

def raket_a_down():
    y = raket_a.ycor()
    y = y - 25
    raket_a.sety(y)

def raket_b_up():
    y = raket_b.ycor()
    y = y + 25
    raket_b.sety(y)

def raket_b_down():
    y = raket_b.ycor()
    y = y - 25
    raket_b.sety(y)

pencere.listen()
pencere.onkeypress(raket_a_up, 'w')
pencere.onkeypress(raket_a_down, 's')
pencere.onkeypress(raket_b_up, 'Up')
pencere.onkeypress(raket_b_down, 'Down')

while True:
    pencere.update()
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    if ball.ycor() > 290 or ball.ycor()< -290:
        ball.dy = ball.dy * -1

    if ball.xcor() > 390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puan_a = puan_a + 1
        yazi.clear()
        yazi.write("OyuncuA:{}  OyuncuB:{}".format(puan_a, puan_b), align='center', font=('Courier', 24, "bold"))

    if ball.xcor() < -390:
        ball.goto(0, 0)
        ball.dx = ball.dx * -1
        puan_b = puan_b + 1
        yazi.clear()
        yazi.write("OyuncuA:{}  OyuncuB:{}".format(puan_a, puan_b), align='center', font=('Courier', 24, "bold"))

    if (ball.xcor() > 340 and ball.xcor() > 350) and (ball.ycor() < raket_b.ycor() + 60 and ball.ycor() > raket_b.ycor() - 60):
        ball.setx(340)
        ball.dx = ball.dx * -1

    if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < raket_a.ycor() + 60 and ball.ycor() > raket_a.ycor() - 60):
        ball.setx(-340)
        ball.dx = ball.dx * -1