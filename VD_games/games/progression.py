import random

DESCRIPTION = "Какое число пропущено в прогрессии?"

def generate_round():
    start = random.randint(1, 20)
    step = random.randint(2, 5)
    length = 10
    
    progression = []
    current_number = start
    
    for i in range(length):
        progression.append(str(current_number))
        current_number = current_number + step
    
    hidden_index = random.randint(0, length - 1)
    correct_answer = progression[hidden_index]
    progression[hidden_index] = ".."
    
    question = " ".join(progression)
    
    return question, correct_answer
