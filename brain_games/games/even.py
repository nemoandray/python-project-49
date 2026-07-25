import random


def is_even(number: int) -> bool:
    return number % 2 == 0


def get_round():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_even(question) else 'no'
    return question, correct_answer