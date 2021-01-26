from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=600, height=400)
user_bet = screen.textinput('Make your bet', 'Which turtle will win the race? ')
colors = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
all_turtles = []

height = -100

for turtle_index in range(6):
    new_turtle = Turtle('turtle')
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.setpos(-270, height)
    height += 35
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
    for turtle in all_turtles:
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
