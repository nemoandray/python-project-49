import random


def is_prime(number: int) -> bool:
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
    return True


def get_round():
    question = random.randint(1, 100)
    correct_answer = 'yes' if is_prime(question) else 'no'
    return question, correct_answer