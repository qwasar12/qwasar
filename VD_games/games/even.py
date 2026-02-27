import random

DESCRIPTION = 'Отвечай "да", если число четное, иначе "нет".'

def generate_round():
    number = random.randint(1, 100)
    correct_answer = "да" if number % 2 == 0 else "нет"
    return str(number), correct_answer
