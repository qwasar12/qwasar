from VD_games.engine import run_game
from VD_games.games import prime

def main():
    run_game(prime.DESCRIPTION, prime.generate_round)

if __name__ == '__main__':
    main()
