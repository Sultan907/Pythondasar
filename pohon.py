import turtle

def fibonacci_tree(t, branch_len, angle, level):
    if level > 0:
        t.forward(branch_len)
        t.right(angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.left(2 * angle)
        fibonacci_tree(t, branch_len - 15, angle, level - 1)
        t.right(angle)
        t.backward(branch_len)

t = turtle.Turtle()
t.speed(0)

t.penup()
t.goto(0, -200)
t.pendown()
t.setheading(90) 

fibonacci_tree(t, 100, 30, 7)

turtle.done()