import turtle
import pandas as pd


screen = turtle.Screen()
screen.title("U.S. States Game")
image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

# to get the coordinates of the image and how the 50_states.csv file was made 
# def get_mouse_click_coor(x, y):
#     print(x,y)
# turtle.onscreenclick(get_mouse_click_coor)
# turtle.mainloop()
FONT = ("Courier", 12, "normal")
states = pd.read_csv("50_states.csv")


score=0
all_states = states.state.to_list()
answer_state_list = []
while len(answer_state_list) < 50:
    answer_state = (screen.textinput(title=f"Score = {score} ", prompt="What's another state name?")).title()
    
    if answer_state == "Exit":
        break
    for index in range(len(states.state)):
        if answer_state == states.state[index]:
            x = states.x[index]
            y = states.y[index]
            turtle2 = turtle.Turtle()
            turtle2.hideturtle()
            turtle2.penup()
            turtle2.goto(x, y)
            turtle2.write(f"{answer_state}", align="center", font= FONT)
            score += 1
            answer_state_list.append(answer_state)

            
print(answer_state_list)

unguessed_states = []
for state in all_states:
    if state not in answer_state_list:
            unguessed_states.append(state)

print(unguessed_states)
new_data = pd.DataFrame(unguessed_states)
new_data.to_csv("states_to_learn.csv")

screen.exitonclick()