from brain_games.engine import run
from brain_games.games.progression import get_round

DESCRIPTION = 'What number is missing in the progression?'


def main():
    run(DESCRIPTION, get_round)


if __name__ == '__main__':
    main()