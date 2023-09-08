import turtle

t = turtle.Turtle()
t.speed(10)
t.penup()
t.goto(-100, 0)
t.pendown()
for i in range(3):
    t.forward(100)
    t.left(120) 

t.penup()
t.goto(50, 0) 
t.pendown()
for i in range(2):
    t.forward(100) 
    t.left(90) 
    t.forward(50)
    t.left(90) 

t.penup()
t.goto(-350, 0)
t.pendown()
for i in range(1):
    t.pendown()
    t.forward(200)
    t.left(120)
    t.forward(100)
    t.left(60)
    t.forward(100)
    t.left(60)
    t.forward(100)

    
t.penup()
t.goto(330, 85) 
t.pendown()
for i in range(2):
    t.forward(100)
    t.right(60)
    t.forward(100)
    t.right(120)

t.penup()
t.goto(0, -200) 
t.pendown() 
for i in range(6):
   t.forward(100)
   t.right(60)

t.penup()
t.goto(200, -150) 
t.pendown() 
for i in range(1):
    t.forward(100)
    t.right(45)
    t.forward(100)
    t.right(135)
    t.forward(100)
    t.right(45)
    t.forward(100)

turtle.done()
