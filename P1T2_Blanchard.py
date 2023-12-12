"""
This is the Template Repl for Python with Turtle.

Python with Turtle lets you make graphics easily in Python.

Check out the official docs here: https://docs.python.org/3/library/turtle.html
"""

import turtle

t = turtle.Turtle()
# comment block
"""
for c in ['red', 'green', 'blue', 'purple']:
    t.color(c)
    t.forward(75)
    t.left(90)
    
"""
# 
"""
t.color("blue")
t.pensize(5)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.right(130)
t.forward(75)
t.right(95)
t.forward(75)
"""

# start of the I

t.color("red")
t.pensize(4)
t.forward(100)
t.backward(50)
t.right(90)
t.forward(100)
t.right(90)
t.forward(50)
t.backward(100)
t.penup()
t.right(180)
t.forward(15)
t.pendown()

# start of the B
t.color("blue")
t.left(90)
t.forward(100)
t.right(90)
t.forward(60)
t.right(90)
t.forward(50)
t.right(90)
t.forward(30)
t.backward(40)
t.left(90)
t.forward(50)
t.right(90)
t.forward(70)

# Counting with loops
size = 12
sides = 12

t.color("purple")
for count in range(sides):
  t.penup()  
  t.forward(size)
t.pendown()
t.right(sides)
t.circle(35)
t.right(25)
t.forward(100)
t.circle(35)
t.forward(100)
t.circle(35)
t.right(90)
t.forward(50)
t.circle(35)
t.forward(100)
t.circle(35)
t.right(90)
t.forward(50)
t.circle(35)
t.forward(100)
t.circle(35)
t.right(90)
t.forward(100)
t.circle(35)
t.forward(50)