import random


def get_round():
    number_1 = random.randint(1, 30)
    number_2 = random.randint(1, 30)
    operator = random.choice(('+', '-', '*'))
    question = f'{number_1} {operator} {number_2}'
    if operator == '+':
        correct_answer = str(number_1 + number_2)
    elif operator == '-':
        correct_answer = str(number_1 - number_2)
    else:
        correct_answer = str(number_1 * number_2)
    return question, correct_answer