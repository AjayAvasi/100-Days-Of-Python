import pandas
import turtle


def squirrel():
    data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")
    color_count = {"colors": list(data["Primary Fur Color"].unique()), "count": []}

    print(color_count["colors"])
    for color in color_count["colors"]:
        color_count["count"].append(len(data[data["Primary Fur Color"] == color]))
    final_data = pandas.DataFrame(color_count)
    final_data.to_csv("squirrel_count.csv")


screen = turtle.Screen()
screen.title("U.S. States Game")

image_path = "blank_states_img.gif"
screen.addshape(image_path)
turtle.shape(image_path)

writer = turtle.Turtle()
writer.pu()
writer.speed("fastest")
writer.hideturtle()

score = 0
already_guessed = set()
state_data = pandas.read_csv("50_states.csv")
game_on = True
while game_on:
    answer = screen.textinput(f"{score}/50 Correct", "What is a state on this map?")


    if answer.lower() == "exit":
        break
    answer = answer.title()
    if answer in list(state_data["state"]):
        if answer not in already_guessed:

            score += 1
            already_guessed.add(answer)
            correct_row = state_data[state_data["state"] == answer]
            x = int(correct_row["x"].iloc[0])
            y = int(correct_row["y"].iloc[0])
            writer.goto(x, y)
            writer.write(answer, False, "center")

missed = {"Missed States": [state for state in state_data.state.to_list() if state not in already_guessed]}

pandas.DataFrame(missed).to_csv("Missed_States.csv")

screen.exitonclick()
