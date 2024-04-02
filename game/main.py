import re

from game.game_rules import BOARD_DIMENSIONS, play_game


def input_feeder():
    pattern = re.compile(f"^[0-{BOARD_DIMENSIONS - 1}]$")
    while True:
        print(f'Give input [0-{BOARD_DIMENSIONS - 1}]')
        txt = input()
        if pattern.match(txt):
            yield int(txt)
        else:
            print(f'Must be a number between 0 and {BOARD_DIMENSIONS - 1}')


if __name__ == "__main__":
    winner = play_game(input_feeder())
    if winner:
        print(f'Game over. Player {winner} won!')
    else:
        print('No one won :(')
