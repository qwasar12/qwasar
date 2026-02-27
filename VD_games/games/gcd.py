import random
import math

DESCRIPTION = "Найдите наибольший общий делитель чисел."

def generate_round():
    num1, num2 = random.randint(1, 100), random.randint(1, 100)
    return f"{num1} {num2}", math.gcd(num1, num2)
