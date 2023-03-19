from turtle import Turtle, Screen
import random


screen = Screen()
screen.setup(750, 750)

location = 0
is_on = False
colors = ["red", "blue", "purple", "green"]
all_turtles = []

user_bet = screen.textinput(title="Make your bet", prompt="Wich turtle will win the race? Enter a color")


for _ in range(0, 4):
    obj = Turtle(shape="turtle")
    obj.dot(15, "black")
    obj.penup()
    obj.color(colors[_])

    if location == 0:
        obj.goto(-330, 0)
    elif location == 1:
        obj.goto(0, -330)
        obj.left(90)
    elif location == 2:
        obj.goto(330, 0)
        obj.right(180)
    else:
        obj.goto(0, 330)
        obj.right(90)
        is_on = True
    location += 1
    all_turtles.append(obj)


    def is_finish(symbol):
        global is_on
        if turtle == all_turtles[0]:
            if turtle.xcor() > 0:
                is_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    turtle.write(f"You've won! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    turtle.write(f"You've lost! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've lost! The {winning_color} turtle is the winner")
        elif turtle == all_turtles[1]:
            if turtle.ycor() > 0:
                is_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    turtle.write(f"You've won! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    turtle.write(f"You've lost! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've lost! The {winning_color} turtle is the winner")
        elif turtle == all_turtles[2]:
            if turtle.xcor() < 0:
                is_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    turtle.write(f"You've won! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    turtle.write(f"You've lost! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've lost! The {winning_color} turtle is the winner")
        else:
            if turtle.ycor() < 0:
                is_on = False
                winning_color = turtle.pencolor()
                if user_bet == winning_color:
                    turtle.write(f"You've won! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've won! The {winning_color} turtle is the winner")
                else:
                    turtle.write(f"You've lost! The {winning_color} turtle is the winner", align="center", font=("Verdana", 20, "normal"))
                    print(f"You've lost! The {winning_color} turtle is the winner")


    if is_on:
        while is_on:
            for turtle in all_turtles:
                is_finish(turtle)
                distance = random.randint(0, 10)
                turtle.forward(distance)

obj.pendown()
screen.exitonclick()


