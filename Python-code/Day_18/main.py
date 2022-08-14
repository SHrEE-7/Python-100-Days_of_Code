import random
from turtle import Turtle, Screen

# 1.
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
#   for _ in range(4):
#     timmy.speed(1)
#     timmy.forward(100)
#     timmy.right(90)

# 2.
# timmy = Turtle()
# timmy.shape("turtle")
# timmy.color("green")
# for _ in range(15):
#     timmy.speed(1)
#     timmy.forward(10)
#     timmy.penup()
#     timmy.speed(1)
#     timmy.forward(10)
#     timmy.pendown()

# 3.
# import random
# timmy = Turtle()
# colors = ["green yellow","red","ghost white","olive drab","light sky blue","gold"]

# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.speed(1)
#         timmy.forward(100)
#         timmy.left(angle)

# for shape_side_n in range(3,10):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side_n)

# 4 random movement of turtle
# timmy = Turtle()
# colors = ["CornFlowerBlue","DarkOrchid","IndianRed","DeepSkyBlue","LightSeaGreen","wheat","SlateGray","SeaGreen"]
# directions = [0,90,180,270]
# timmy.pensize(15)
# timmy.speed(10)
# for _ in range(200):
#     timmy.color(random.choice(colors))
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))

# 5. random color with random direction of timmy
# import turtle as t
# timmy = t.Turtle()
# t.colormode(255)

# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     return (r,g,b)

# directions = [0,90,180,270]
# timmy.speed(10)
# timmy.pensize(15)
# for _ in range(200):
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# making a spirograph
import turtle as t
timmy = t.Turtle()
t.colormode(255)

def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    return (r,g,b)

timmy.speed(0)
def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + size_of_gap)

draw_spirograph(1)



screen = Screen()
screen.exitonclick()