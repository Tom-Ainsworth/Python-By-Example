# import turtle
# import random

# scr = turtle.Screen()
# scr.bgcolor("yellow")
# turtle.shape("turtle")


# turtle.penup() lifts the pen if I need to start
# drawing from another position.
# turtle.pendown() drops the pen, and is set as the default.

# 060 Draw a square.
# for i in range(0, 4):
#     turtle.forward(100)
#     turtle.right(90)


# 061 Draw a triangle.
# for i in range(0,3):
#     turtle.right(120)
#     turtle.forward(100)


# 062 Draw a circle. Here's 2 ways of doing it.
# turtle.circle(50)
# for i in range(0,360):
#     turtle.forward(1)
#     turtle.right(1)


# 063 Draw three squares in a row with a gap between each.
# Fill them using three different colours.


# turtle.begin_fill()
# turtle.color("black", "red")
# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(60)
# turtle.pendown()

# turtle.begin_fill()
# turtle.color("black", "green")

# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(60)
# turtle.pendown()

# turtle.begin_fill()
# turtle.color("black", "blue")
# for i in range(0, 4):
#     turtle.forward(50)
#     turtle.right(90)
# turtle.end_fill()
# turtle.penup()
# turtle.forward(60)
# turtle.pendown()


# 064 Draw a five-pointed star.
# for i in range(0,5):
#     turtle.right(144)
#     turtle.forward(50)


# 065 Write the numbers as shown below,
# starting at the bottom of the number one.
# # One
# turtle.left(90)
# turtle.forward(100)
# turtle.right(90)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()

# # Two
# turtle.forward(75)
# turtle.right(90)
# turtle.forward(50)
# turtle.right(90)
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)
# turtle.penup()
# turtle.forward(50)
# turtle.pendown()

# # Three
# turtle.forward(75)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(40)
# turtle.left(180)
# turtle.forward(40)
# turtle.left(90)
# turtle.forward(50)
# turtle.left(90)
# turtle.forward(75)


# 066 Draw an octagon that uses a different colour
# (randomly selected from a list of six possible colors) for each line.
# for i in range(0,8):
#     turtle.color(random.choice(['green', 'blue', 'red', 'pink', 'white',
# 'black']))
#     turtle.forward(50)
#     turtle.right(45)


# 067 Create the following pattern: (See page 53 of the book)
# for i in range(0,11):
#     for i in range(0,8):
#         turtle.color(random.choice(['green','blue','red','pink','white','black']))
#         turtle.forward(50)
#         turtle.left(45)
#     turtle.left(32)


# 068 Draw a pattern that will change each time the program is run.
# lines = random.randint(5, 20)
# for i in range(0, lines):
#     turtle.forward(random.randint(50, 100))
#     turtle.left(random.randint(45, 90))


# Use the random function to pick the number of lines, the length
# of each line and the angle of each turn.

# scr.exitonclick()
