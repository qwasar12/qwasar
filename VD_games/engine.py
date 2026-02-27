import sys

def run_game(description, get_round_data):
    print("Добро пожаловать в VD-games!")
    name = input('Как тебя зовут? ')
    print(f"Привет, {name}!")
    print(description)

    for _ in range(3):
        question, correct_answer = get_round_data()
        print(f"Вопрос: {question}")
        user_answer = input("Твой ответ: ")

        if user_answer == str(correct_answer):
            print("Правильно!")
        else:
            print(f"'{user_answer}' — неправильный ответ. Правильный ответ: '{correct_answer}'.")
            print(f"Попробуй еще раз, {name}!")
            return

    print(f"Поздравляем, {name}!")
