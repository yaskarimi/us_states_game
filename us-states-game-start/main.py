import turtle
import pandas

screen = turtle.Screen()
count = 0
screen.title("U.S. states game")
screen.addshape("blank_states_img.gif")
turtle.shape("blank_states_img.gif")
correct_guess = []

while len(correct_guess) < 50:
    user_guess = screen.textinput(title=f"{count}/50 correct states", prompt="What's another state?").title()
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


    if user_guess.casefold() == "exit".casefold():

        all_states = data.state.to_list()
        learn = []
        for state in all_states:
            if state not in correct_guess:
                learn.append(state)
        dataframe = pandas.DataFrame(learn)
        dataframe.to_csv("states_to_learn.csv")

        break
turtle.mainloop()
screen.exitonclick()
