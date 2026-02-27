import prompt

def welcome_user():
    print("Welcome to the VD-games!")
    name = prompt.string('как тебя зовут? ')
    print(f"привет, {name}!")
