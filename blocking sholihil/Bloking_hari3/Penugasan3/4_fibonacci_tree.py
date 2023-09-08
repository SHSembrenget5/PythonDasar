import turtle

t = turtle.Turtle()
t.speed(0)

def fibonacci_tree(branch_len, angle):
    if branch_len < 2:
        t.forward(branch_len)
        t.backward(branch_len)
    else:
        t.forward(branch_len)
        t.right(angle)
        fibonacci_tree(branch_len - 15, angle)
        t.left(2 * angle)
        fibonacci_tree(branch_len - 15, angle)
        t.right(angle)
        t.backward(branch_len)

t.left(90)
starting_length = 80
angle = 30

fibonacci_tree(starting_length, angle)

turtle.done()
