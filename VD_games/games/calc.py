import random

DESCRIPTION = "Вычислите результат выражения."

def generate_round():
    a, b = random.randint(1, 20), random.randint(1, 20)
    op = random.choice(['+', '-', '*'])
    if op == '+': ans = a + b
    elif op == '-': ans = a - b
    else: ans = a * b
    return f"{a} {op} {b}", ans
