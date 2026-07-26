from brain_games.engine import run
from brain_games.games.gcd import get_round

DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def main():
    run(DESCRIPTION, get_round)


if __name__ == '__main__':
    main()