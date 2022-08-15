from turtle import Turtle, Screen
import random
is_race_on=False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput(title="Make Your Bet",prompt="Which turtle will win the race? Enter color Name: ")
colors = ["red","orange","yellow","green","blue","purple","black"]
y_positions = [-120,-80,-40,0,40,80,120]
all_turtles = []
for turtle_index in range(0,7):
    tim = Turtle(shape="turtle")
    tim.color(colors[turtle_index])
    tim.penup()
    tim.goto(x=-280,y=y_positions[turtle_index])
    all_turtles.append(tim)

if user_bet:
    is_race_on = True
while is_race_on:
    for turtle in all_turtles:
        if turtle.xcor() > 270:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You've won ..! The winning color is {winning_color} is the winner.!")
            else:
                print(f"You've lost.!! The winning color is {winning_color} is the winner.! ")    
        
        random_distance = random.randint(0,10)
        turtle.forward(random_distance)

screen.exitonclick()