from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(width=500, height=400)
user_guess = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Enter a color: ")
colours = ["red", "green", "yellow", "yellow", "pink", "cyan"]

y_positions = [-70, -40, -10, 20, 50]
is_race_on = False
all_turtle=[]
for turtle_index in range(0, 5):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colours[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y_positions[turtle_index])
    new_turtle.penup()
    all_turtle.append(new_turtle)

if user_guess:
    is_race_on = True

while is_race_on:
    for turtle in all_turtle:
        if turtle.xcor()>230:
            is_race_on = False
            winning_color = turtle.pencolor()
            if winning_color == user_guess:
                print(f"You have won!. The {winning_color} is winner.")
            else:
                print(f"You have lose!. The {winning_color} is winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()


# def move_forwards():
#     tim.forward(10)
#
# def move_backward():
#     tim.backward(10)
#
# def move_left():
#     new_heading = tim.heading()+10
#     tim.setheading(new_heading)
#
# def move_right():
#     new_heading = tim.heading() - 10
#     tim.setheading(new_heading)
#
# def clear():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
#
# screen.listen()
# screen.onkey(move_forwards, "w")
# screen.onkey(move_backward, "s")
# screen.onkey(move_left, "a")
# screen.onkey(move_right, "d")
# screen.onkey(clear, "c")
