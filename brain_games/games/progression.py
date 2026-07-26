import random


def generate_progression():
    start = random.randint(-50, 100)
    step = random.randint(1, 10)
    length = 10
    result = []
    for index in range(length):
        current_element = start + index * step
        result.append(current_element)
    hidden_index = random.randint(0, length - 1)
    return result, hidden_index


def get_round():
    result, hidden_index = generate_progression()
    correct_answer = str(result[hidden_index])
    result[hidden_index] = '..'
    question = ' '.join(str(item) for item in result)
    return question, correct_answer
