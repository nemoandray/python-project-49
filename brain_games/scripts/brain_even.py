from brain_games.engine import run
from brain_games.games.even import get_round

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    run(DESCRIPTION, get_round)


if __name__ == '__main__':
    main()
    
    