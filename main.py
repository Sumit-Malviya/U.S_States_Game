import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)


data = pandas.read_csv("50_states.csv")
all__states = data.state.to_list()
guessed_states = []

while len(guessed_states) <= 50:
    answer_state = screen.textinput(title= f"{len(guessed_states)}/50 States Correct",
                                    prompt="What's another state names?:").title()
    if answer_state == "Exit":
        missing_states = [state for state in all__states if state not in guessed_states]
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    if answer_state in all__states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(answer_state)

# is_guess_true = True
# filling_list = []
# score = 0
# while is_guess_true:
#     if answer_state in list_of_states and answer_state not in filling_list:
#         single_state_info = data[data.state == f"{answer_state}"]
#         x_cor = single_state_info.x
#         y_cor = single_state_info.y
#         turtle.goto(x_cor, y_cor)
#         filling_list.append(answer_state)
#
#     elif len(filling_list) == 50:
#         print("Congrats! you have correctly guessed all the states.")
#         is_guess_true = False

screen.exitonclick()