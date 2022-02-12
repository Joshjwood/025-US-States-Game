from turtle import Turtle

class StateManager:

    def __init__(self):
        self.all_states = []

    def spawn_car(self, state, x, y):
        new_state = Turtle("square")
        new_state.penup()
        new_state.color("black")
        new_state.hideturtle()
        new_state.goto(x, y)
        new_state.write(f"{state}", False, align="Center", font=("Arial", 14, "normal"))
        self.all_states.append(new_state)



