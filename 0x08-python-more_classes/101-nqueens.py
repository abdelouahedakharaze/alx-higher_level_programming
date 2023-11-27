#!/usr/bin/python3
# 101-nqueens.py
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N
non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    board (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]]
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def initialize_chessboard(size):
    """Initialize an `n`x`n` chessboard with 0's."""
    board = [[" "] * size for _ in range(size)]
    return board


def deepcopy_chessboard(board):
    """Return a deepcopy of a chessboard."""
    if isinstance(board, list):
        return [deepcopy_chessboard(row) for row in board]
    return board


def get_solution_positions(board):
    """Return the list of lists representation of a solved chessboard."""
    positions = []
    for r in range(len(board)):
        for c in range(len(board)):
            if board[r][c] == "Q":
                positions.append([r, c])
                break
    return positions


def mark_unavailable_spots(board, row, col):
    """Mark spots on a chessboard where non-attacking queens can no longer
    be placed."""
    for c in range(col + 1, len(board)):
        board[row][c] = "x"
    for c in range(col - 1, -1, -1):
        board[row][c] = "x"
    for r in range(row + 1, len(board)):
        board[r][col] = "x"
    for r in range(row - 1, -1, -1):
        board[r][col] = "x"
    c = col + 1
    for r in range(row + 1, len(board)):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(board):
            break
        board[r][c] = "x"
        c += 1
    c = col - 1
    for r in range(row + 1, len(board)):
        if c < 0:
            break
        board[r][c] = "x"
        c -= 1


def recursive_solve(board, row, queens, solutions):
    """Recursively solve an N-queens puzzle."""
    if queens == len(board):
        solutions.append(get_solution_positions(board))
        return solutions

    for c in range(len(board)):
        if board[row][c] == " ":
            tmp_B = deepcopy_chessboard(board)
            tmp_B[row][c] = "Q"
            mark_unavailable_spots(tmp_B, row, c)
            solutions = recursive_solve(tmp_B, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if not sys.argv[1].isdigit():
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = initialize_chessboard(int(sys.argv[1]))
    solutions = recursive_solve(board, 0, 0, [])
    for sol in solutions:
        print(sol)
