from brain_games.engine import run
from brain_games.games.calc import calculation

DESCRIPTION = 'What is the result of the expression?'


def main():
    run(DESCRIPTION, calculation)


if __name__ == '__main__':
    main()