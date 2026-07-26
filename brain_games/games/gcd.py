import random


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def get_round():
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'{number_1} {number_2}'
    correct_answer = str(gcd(number_1, number_2))
    return question, correct_answer
