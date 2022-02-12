import turtle
import pandas
from state_icon import StateManager

screen = turtle.Screen()
statemanager = StateManager()

screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

results = []

data = pandas.read_csv("50_states.csv")
data_dict = data.to_dict()

#data = data[data["Primary Fur Color"] == "Black"]

# monday = data[data.day == "Monday"]
# print((monday.temp) * 1.8 + 32)
all_states = data.state.to_list()

while len(results) < 50:
    score = len(results)
    answer_state = screen.textinput(title=f"Guess the state: {score}/50", prompt="What's another states name?")
    if answer_state.lower() == "exit":
        missing_states = [i for i in all_states if i not in results]
        data2 = pandas.DataFrame(missing_states)
        data2.to_csv("Here's what you missed")
        break
    for i in data_dict["state"]:
        #print(data_dict["state"][i])

        if answer_state.title() == data_dict["state"][i]:
            if answer_state.title() not in results:
                results.append(answer_state.title())

                state = data[data["state"] == answer_state.title()]
                xpos = int(state.x)
                ypos = int(state.y)
                #print(xpos)
                #print(ypos)

                statemanager.spawn_car(state=answer_state.title(), x=xpos, y=ypos)






turtle.mainloop()