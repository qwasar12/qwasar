import random

DESCRIPTION = 'Отвечай "да", если число простое, иначе "нет".'

def generate_round():
    number = random.randint(1, 50)
    question = str(number)
    
    if number < 2:
        correct_answer = "нет"
    else:
        correct_answer = "да"
        for i in range(2, number):
            if number % i == 0:
                correct_answer = "нет"
                break
                
    return question, correct_answer
