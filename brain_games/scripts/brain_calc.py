from brain_games.engine import run
from brain_games.games.calc import get_round

DESCRIPTION = 'What is the result of the expression?'


def main():
    run(DESCRIPTION, get_round)


if __name__ == '__main__':
    main()