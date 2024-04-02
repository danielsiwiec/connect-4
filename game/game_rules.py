import dataclasses
import os
from typing import Union

BOARD_DIMENSIONS = 6
WINNING_STREAK = 4


@dataclasses.dataclass
class Board:
    columns: list[list[str]]

    def __init__(self):
        self.columns = [[] for _ in range(6)]

    def drop_in_column(self, selected_column: int, player: str):
        if selected_column >= BOARD_DIMENSIONS:
            raise Exception("You can't do that")
        self.columns[selected_column].append(player)
        self.print_board()

    def print_board(self):
        print("--- Current board ---\n")
        for horizontal_position in range(BOARD_DIMENSIONS - 1, -1, -1):
            for column in self.columns:
                player = column[horizontal_position] if len(column) > horizontal_position else ' '
                print(f'[{player}]', end=' ')
            print('\n')


def horizontal_win(board: Board, selected_column: int) -> bool:
    selected_stack = board.columns[selected_column]
    player = selected_stack[-1]
    horizontal_position = len(selected_stack) - 1
    streak = 0

    # start with full range of columns
    for column in range(selected_column - 3, selected_column + 3):
        # for columns outside of starting range - skip
        if column < 0:
            continue
        # for columns outside of ending range - we've reached the end - no win
        if column > BOARD_DIMENSIONS - 1:
            return False
        # if column has enough pieces for horizontal win...
        if len(board.columns[column]) > horizontal_position:
            # if the piece matches the current player
            if board.columns[column][horizontal_position] == player:
                # if the streak was already 3 - win
                if streak == 3:
                    return True
                # if not - increment streak by 1
                else:
                    streak += 1
            else:
                streak = 0


def diagonal_win_bottom_up(board: Board, selected_column: int) -> bool:
    selected_stack = board.columns[selected_column]
    player = selected_stack[-1]
    # starting position is 3 below current piece
    horizontal_position = len(selected_stack) - 1 - 3
    streak = 0

    # start with full range of columns
    for column in range(selected_column - 3, selected_column + 3):
        # for columns outside of starting range (left of bottom) - skip and increment offset
        if column < 0 or horizontal_position < 0:
            horizontal_position += 1
            continue
        # for columns outside of ending range - we've reached the end - no win
        if column > BOARD_DIMENSIONS - 1:
            return False
        # if column has enough pieces for diagonal win...
        if len(board.columns[column]) > horizontal_position:
            # if the piece matches the current player
            if board.columns[column][horizontal_position] == player:
                # if the streak was already 3 - win
                if streak == 3:
                    return True
                # if not - increment streak by 1
                else:
                    streak += 1
                    horizontal_position += 1
            else:
                streak = 0
                horizontal_position += 1


def diagonal_win_top_down(board: Board, selected_column: int) -> bool:
    selected_stack = board.columns[selected_column]
    player = selected_stack[-1]
    # starting position is 3 below current piece
    horizontal_position = len(selected_stack) - 1 + 3
    streak = 0

    # start with full range of columns
    for column in range(selected_column - 3, selected_column + 3):
        # for columns outside of starting range (left of bottom) - skip and increment offset
        if column < 0 or horizontal_position < 0:
            horizontal_position -= 1
            continue
        # for columns outside of ending range - we've reached the end - no win
        if column > BOARD_DIMENSIONS - 1:
            return False
        # if column has enough pieces for diagonal win...
        if len(board.columns[column]) > horizontal_position:
            # if the piece matches the current player
            if board.columns[column][horizontal_position] == player:
                # if the streak was already 3 - win
                if streak == 3:
                    return True
                # if not - increment streak by 1
                else:
                    streak += 1
                    horizontal_position -= 1
            else:
                streak = 0
                horizontal_position -= 1


def vertical_win(board: Board, selected_column: int) -> bool:
    selected_column = board.columns[selected_column]
    current_player = selected_column[-1]
    return len(selected_column) >= 4 and all(elem == current_player for elem in selected_column[-4:])


def is_game_over(board: Board, selected_column: int) -> bool:
    win_conditions = [horizontal_win, vertical_win, diagonal_win_bottom_up]
    for win_condition in win_conditions:
        if win_condition(board, selected_column):
            return True

    return False


def play_game(moves_generator) -> Union[str, None]:
    current_player = 'A'
    board = Board()
    for selected_column in moves_generator:
        board.drop_in_column(selected_column, current_player)
        if is_game_over(board, selected_column):
            return current_player
        current_player = 'A' if current_player == 'B' else 'B'