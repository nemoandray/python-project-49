import prompt

from brain_games.cli import welcome_user


def run(description, get_round):
    print("Welcome to the Brain Games!")
    name = welcome_user()
    print(description)
    count = 0

    while count < 3:
        question, correct_answer = get_round()
        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')
        if correct_answer == answer:
            count += 1
            print('Correct!')
        else:
            print(
                f"'{answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'."
                )
            print(f"Let's try again, {name}!")
            return
    print(f'Congratulations, {name}!')
