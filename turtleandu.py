# import turtle

# canvas = turtle.Turtle()

# while True:

#     canvas.right(75)
#     canvas.forward(100)


import turtle

screenColor = turtle.Screen()
screenColor.bgcolor("light blue")
screenColor.title("Asi Turtle Project")

canvas = turtle.Turtle()

# while True:

canvas.right(75)
canvas.forward(100)

for i in range(4):
    canvas.right(144)
    canvas.forward(100)


turtle.done()