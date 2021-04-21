from turtle import Turtle, Screen
from scoreboard import Scoreboard
import pandas
from map import Map

screen = Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
Turtle(image)
scoreboard = Scoreboard()
map = Map()

#TODO open cvs file
states = pandas.read_csv("50_states.csv")
list_states = states.state.to_list()
while len(scoreboard.guessed_states) < 50:

        
    answer_state = screen.textinput(title=f"{scoreboard.score}/{scoreboard.total_states} States Correct", prompt="What's another state's name?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = [state for state in list_states if state not in scoreboard.guessed_states]
        # for state in list_states:
        #     if state not in scoreboard.guessed_states:
        #         missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break
    #TODO check if state is on csv file
    result = states[states.state == answer_state]

    #TODO display the state name on the map according to x, y coordinates on the csv file
    if not result.empty:
        map.get_position(result.x.item(), result.y.item(), result.state.item())
        if answer_state not in scoreboard.guessed_states:
            scoreboard.update_score(result)
   



    #TODO save score when the answer is correct and display on the title screen


    #Getting coordinates
    # def get_mouse_click_coor(x, y):
    #     print(x, y)

    # screen.onscreenclick(get_mouse_click_coor)

    # screen.mainloop()

#screen.exitonclick()
