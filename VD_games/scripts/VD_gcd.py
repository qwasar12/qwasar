from VD_games.engine import run_game
from VD_games.games import gcd

def main():
    run_game(gcd.DESCRIPTION, gcd.generate_round)

if __name__ == '__main__':
    main()
