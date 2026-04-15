import time

def get_valid_input(prompt, valid_options):
    while True:
        try:
            choice = int(input(prompt))
            if choice in valid_options:
                return choice
            else:
                print(f"\n\n‼️- invalid option. choose from {valid_options}")
        except ValueError:
            print("\n\n⚠️- option must be an integer. try again.")


def uilook():
    ui_look = get_valid_input("""\nwhat kind of theme would you prefer?
    1. classic pomodoro
    2. soft and dreamy study
    3. focus + productive
    4. late night coder
    5. cozy desk energy
    6. monochrome / minimalistic
    
    your preference (1/2/3/4/5/6): """, [1,2,3,4,5,6])

    if ui_look == 1:
        classic_pomodoro()
    elif ui_look == 2:
        soft_pomodoro()
    elif ui_look == 3:
        focus_pomodoro()
    elif ui_look == 4:
        late_night_pomodoro()
    elif ui_look == 5:
        cozy_desk_pomodoro()
    elif ui_look == 6:
        monochrome_pomodoro()


def classic_pomodoro():
    print("\n\t[🍅] --> welcome to pomodoro timer!")

    timer = get_valid_input("""\n(⌛) choose your preferred timer:
    1. 25 minutes work, 5 minutes break
    2. 30 minutes work, 5 minutes break
    3. 50 minutes work, 10 minutes break
    4. custom
    
    choose (1/2/3/4): """, [1,2,3,4])

    if timer == 1:
        c_time_2510()
    elif timer == 2:
        c_time_3010()
    elif timer == 3:
        c_time_50_10()
    elif timer == 4:
        c_time_custom()


# placeholder functions (so your code runs without errors)
def soft_pomodoro():
    print("soft theme coming soon 🌸")

def focus_pomodoro():
    print("focus mode coming soon ⚡")

def late_night_pomodoro():
    print("late night mode coming soon 🌙")

def cozy_desk_pomodoro():
    print("cozy vibes coming soon ☕")

def monochrome_pomodoro():
    print("minimal mode coming soon ⚪⚫")
  
---

def c_time_2510():
    print("running 25/5 timer...")

def c_time_3010():
    print("running 30/5 timer...")

def c_time_50_10():
    print("running 50/10 timer...")

def c_time_custom():
    print("custom timer coming soon...")

# run program
uilook()
