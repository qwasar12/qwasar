from VD_games.engine import run_game
from VD_games.games import calc

def main():
    run_game(calc.DESCRIPTION, calc.generate_round)

if __name__ == '__main__':
    main()
