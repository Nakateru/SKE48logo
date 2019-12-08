import turtle as t


def drawS(x, y):
    t.speed(5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(90)
    t.circle(58, 270)
    t.setheading(180)
    t.circle(75, -270)


def drawK(x, y):
    t.speed(2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-90)
    t.forward(253)
    t.penup()
    t.goto(x + 140, y)
    t.pendown()
    t.goto(x + 10, y - 130)
    t.goto(x + 140, y - 260)


def drawE(x, y):
    t.speed(2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-90)
    t.forward(260)
    t.penup()
    t.goto(x + 90, y)
    t.pendown()
    t.goto(x, y)
    t.penup()
    t.goto(x + 90, y - 120)
    t.pendown()
    t.goto(x, y - 120)
    t.penup()
    t.goto(x + 110, y - 260)
    t.pendown()
    t.goto(x, y - 260)


def draw4(x, y):
    t.speed(2)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.goto(x - 145, y - 200)
    t.goto(x + 20, y - 200)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(-90)
    t.forward(255)


def draw8(x, y):
    t.speed(5)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.setheading(0)
    t.circle(60)
    t.circle(-75)


if __name__ == '__main__':
    posx = -102
    posy = 285
    t.setup(500, 700)
    t.screensize(canvwidth=500, canvheight=700, bg="orange")
    t.hideturtle()
    t.pensize(10)
    t.pencolor("white")

    drawS(posx, posy)
    drawK(posx + 55, posy + 50)
    drawE(posx + 225, posy + 50)
    draw4(posx, posy - 220)
    draw8(posx + 117, posy - 335)
    t.exitonclick()
