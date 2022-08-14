import turtle as turtle_module
import random
turtle_module.colormode(255)
tim = turtle_module.Turtle()
tim.speed("fastest")
tim.penup()
tim.hideturtle()
color_list = [(254, 253, 250), (247, 252, 250), (251, 243, 247), (234, 245, 250), (196, 9, 68), (244, 230, 74), (212, 155, 90), (19, 117, 174), (168, 169, 27), (107, 180, 209), (218, 131, 166), (163, 74, 30), (238, 72, 34), (5, 35, 87), (26, 139, 72), (124, 181, 142), (219, 76, 122), (240, 222, 3), (82, 17, 80), (175, 47, 90), (9, 59, 35), (12, 166, 213), (239, 160, 190), (126, 33, 21), (9, 44, 130), (52, 164, 114), (4, 104, 63), (4, 88, 99), (142, 209, 220), (100, 31, 13)]
tim.setheading(255)
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for dot_count in range(1, number_of_dots +1):
    tim.dot(20, random.choice(color_list))
    tim.forward(50)

    if dot_count % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)

screen = turtle_module.Screen()
screen.exitonclick()
