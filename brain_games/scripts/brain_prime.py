from brain_games.engine import run
from brain_games.games.prime import get_round

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    run(DESCRIPTION, get_round)


if __name__ == '__main__':
    main()