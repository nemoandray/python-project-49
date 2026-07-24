import prompt
import random
from .cli import welcome_user


def is_even(number: int) -> bool:
    return number % 2 == 0


def brain_even(name: str) -> str:
    count = 0
    good_answer = (f"Congratulations, {name}!")  
    print('Answer "yes" if the number is even, otherwise answer "no".')

    while count < 3:
        question = random.randint(1, 100)
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_even(question) else 'no'
        if answer == correct_answer:
            print('Correct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.")
            return f"Let's try again, {name}!"
    return good_answer


def main():
    print('Welcome to the Brain Games!')
    name = welcome_user()
    print(brain_even(name))


if __name__ == '__main__':
    main()
    
    