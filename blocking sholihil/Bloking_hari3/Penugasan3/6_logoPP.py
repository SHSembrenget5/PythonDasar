import turtle

t = turtle.Turtle()
t.speed(20)

t.penup()
t.goto(0, -400)
t.pendown()

# Outer circle
r = 400
t.circle(r)

# Inner circle
t.penup()
t.goto(0, -355)
t.pendown()
t.fillcolor("blue")
t.begin_fill()
t.circle(350)
t.end_fill()

# Small circle
t.penup()
t.goto(-110, 180)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.circle(60)
t.end_fill()

# Small circle
t.penup()
t.goto(-110, 185)
t.pendown()
t.fillcolor("black")
t.color("black")
t.begin_fill()
t.circle(55)
t.end_fill()

# Rectangle inner
t.penup()
t.goto(-75, -205)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.forward(170)
t.right(90)
t.forward(100)
t.right(90)
t.forward(170)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(-70, -220)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.forward(160)
t.right(90)
t.forward(80)
t.right(90)
t.forward(160)
t.right(90)
t.forward(80)
t.right(90)
t.end_fill()

# Small circle inner
t.penup()
t.goto(10, -260)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.circle(160)
t.end_fill()

# Rectangle
t.penup()
t.goto(99, 204)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.setheading(270)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(165, 204)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.setheading(270)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(15, 204)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.setheading(270)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.end_fill()


# Rectangle
t.penup()
t.goto(-65, 265)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.setheading(270)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.forward(345)
t.right(90)
t.forward(85)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(-118, -172)
t.pendown()
t.fillcolor("white")
t.color("white")
t.begin_fill()
t.setheading(145)
t.forward(205)
t.right(90)
t.forward(110)
t.right(90)
t.forward(205)
t.right(90)
t.forward(110)
t.right(90)
t.end_fill()

# Small circle
t.penup()
t.goto(99, 26)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.circle(155)
t.end_fill()


# Rectangle
t.penup()
t.goto(-120, -165)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.setheading(145)
t.forward(195)
t.right(90)
t.forward(100)
t.right(90)
t.forward(195)
t.right(90)
t.forward(100)
t.right(90)
t.end_fill()


# Rectangle
t.penup()
t.goto(-70, 260)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.setheading(270)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(10, 198)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.setheading(270)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(93, 198)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.setheading(270)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.forward(340)
t.right(90)
t.forward(75)
t.right(90)
t.end_fill()

# Rectangle
t.penup()
t.goto(160, 198)
t.pendown()
t.fillcolor("red")
t.color("red")
t.begin_fill()
t.setheading(270)
t.forward(255)
t.right(90)
t.forward(60)
t.right(90)
t.forward(255)
t.right(90)
t.forward(60)
t.right(90)
t.end_fill()


turtle.done()
