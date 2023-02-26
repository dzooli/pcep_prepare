# Copyright (c) 2023 Zoltan Fabian
#
# This software is released under the MIT License.
# https://opensource.org/licenses/MIT

"""Simple Tic-Tac-Toe for the final project of the course Part1"""

from random import choice


class GameOver(Exception):
    pass


class GameTie(Exception):
    pass


game_board = [
    ["0", "1", "2"],
    ["3", "4", "5"],
    ["6", "7", "8"],
]


def make_list_of_free_fields(board):
    """Generates the list of unoccupied fields of the board."""
    idx = -1
    free = []
    for row in range(0, 3):
        for col in range(0, 3):
            try:
                int(board[row][col])
            except ValueError:
                continue
            finally:
                idx += 1
            free.append(idx)
    return free


def victory_for(sign: str, board) -> bool:
    """Check if the winner is the given sign."""
    if sign.upper() not in ["X", "O"]:
        raise ValueError("Invalid player sign!")
    col1 = (board[0][0], board[1][0], board[2][0])
    col2 = (board[0][1], board[1][1], board[2][1])
    col3 = (board[0][2], board[1][2], board[2][2])
    diag1 = (board[0][0], board[1][1], board[2][2])
    diag2 = (board[0][2], board[1][1], board[2][0])
    check_input = [board[0], board[1], board[2], col1, col2, col3, diag1, diag2]
    for check in check_input:
        if check.count(sign) == 3:
            return True
    return False


def draw_spacer(cap: str = "+", filler: str = "-"):
    """Draws one spacer line of the board."""
    print(3 * (cap + filler * 7) + cap)


def draw_row(row: list):
    """Draws one board row with the corresponding values."""
    if not isinstance(row, list):
        raise TypeError("Call it with a list!")
    for i in range(0, 3):
        print("|" + 3 * " " + str(row[i]) + 3 * " ", end="")
    print("|")


def draw_board(board):
    """Draws the board using spacers and board values."""
    for row in range(0, 3):
        draw_spacer()
        draw_spacer(cap="|", filler=" ")
        draw_row(board[row])
        draw_spacer(cap="|", filler=" ")
    draw_spacer()


def make_move(sign, board, user_move: int = -1):
    """Updates the board with the given sign"""
    for row in range(0, 3):
        for col in range(0, 3):
            try:
                value = int(board[row][col])
            except ValueError:
                continue
            if value == user_move:
                board[row][col] = sign
                return


if __name__ == "__main__":

    while True:
        try:
            draw_board(game_board)
            free_list = make_list_of_free_fields(game_board)
            if len(free_list) == 0:
                raise GameTie()

            player_move = input(f"Enter your move {free_list}: ")
            try:
                player_move = int(player_move)
            except ValueError:
                print("Please enter a number!")
                continue

            make_move("O", game_board, player_move)
            if victory_for("O", game_board):
                raise GameOver("Player wins!")

            free_list = make_list_of_free_fields(game_board)
            try:
                computer_move = choice(free_list)
            except IndexError as exc:
                raise GameTie() from exc
            make_move("X", game_board, computer_move)
            if victory_for("X", game_board):
                raise GameOver("Computer wins!")
        except KeyboardInterrupt:
            break
        except GameOver as exc:
            draw_board(game_board)
            print(f"\n{str(exc)}")
            break
        except GameTie:
            print("\nNo more fields! No winner!")
            break
