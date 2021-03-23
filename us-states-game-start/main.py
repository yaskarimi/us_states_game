import turtle
import pandas

screen = turtle.Screen()
count = 0
game_is_on = True
screen.title("U.S. states game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
correct_guess = []

while game_is_on:
    user_guess = screen.textinput(title=f"{count}/50 correct states", prompt="What's another state?")
    data = pandas.read_csv("50_states.csv")
    if user_guess in data.values:
        correct_guess.append(user_guess)
        df = data[data["state"] == user_guess]
        x = int(df["x"].values)
        y = int(df["y"].values)
        count += 1
        new_turtle = turtle.Turtle()
        new_turtle.penup()
        new_turtle.hideturtle()
        new_turtle.goto(x, y)
        new_turtle.write(user_guess)

        print(x,y)
    if count == 50 :
        game_is_on = False
turtle.mainloop()
screen.exitonclick()