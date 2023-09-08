import turtle

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-100, 0)
t.pendown()

t.fillcolor("yellow")
t.begin_fill()
for i in range(3):
    t.forward(100)
    t.left(120) 
t.end_fill()

t.penup()
t.goto(50, 0) 
t.pendown()
t.fillcolor("red")
t.begin_fill()
for i in range(2):
    t.forward(100) 
    t.left(90) 
    t.forward(50)
    t.left(90) 
t.end_fill()

t.penup()
t.goto(-350, 0)
t.pendown()
t.fillcolor("green")
t.begin_fill()
for i in range(1):
    t.pendown()
    t.forward(200)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)
t.end_fill()

    
t.penup()
t.goto(330, 85) 
t.pendown()
t.fillcolor("blue")
t.begin_fill()
for i in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)
t.end_fill()

t.penup()
t.goto(0, -200) 
t.pendown()
t.fillcolor("purple")
t.begin_fill()
for i in range(5):
    t.forward(100) 
    t.right(72)
t.end_fill()


turtle.done()
