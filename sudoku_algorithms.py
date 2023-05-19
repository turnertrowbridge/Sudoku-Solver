from typing import List


def isValidSudoku(self, board: List[List[str]]) -> bool:
    board_length = len(board)

    # time: O(n^2) space: O(n^2)
    rows = [set() for _ in range(board_length)]
    cols = [set() for _ in range(board_length)]
    squares = [set() for _ in range(board_length)]

    for r in range(board_length):
        for c in range(board_length):

            space = board[r][c]

            # skip other checks if space is blank
            if space == ".":
                continue

            # compute the square that the space is in
            s = (r // 3) * 3 + (c // 3)

            if (
                    space in rows[r]
                    or space in cols[c]
                    or space in squares[s]
            ):
                return False

            else:
                rows[r].add(space)
                cols[c].add(space)
                squares[s].add(space)

    return True


def solveSudoku(self, board: List[List[str]]) -> None:
    """
    Do not return anything, modify board in-place instead.
    """
    board_length = len(board)

    def solve(r: int, c: int) -> bool:
        # base cases
        if r == board_length:  # row filled
            return True
        if c == board_length:  # column filled
            return solve(r + 1, 0)

        # search for solutions
        if board[r][c] == ".":
            for i in range(1, board_length + 1):
                if isValid(r, c, str(i)):
                    board[r][c] = str(i)

                    if solve(r, c + 1):  # recursively solve the modified board
                        return True

                    board[r][c] = "."  # undo the choice if it didn't lead to a valid solution

            return False  # if no valid number is found for the current cell, backtrack

        else:
            return solve(r, c + 1)  # recursively solve the modified board

    def isValid(r: int, c: int, n: str) -> bool:
        # Check if the number already exists in the same row, col, or square
        for i in range(board_length):
            if (
                    (board[r][i] == n)
                    or (board[i][c] == n)
                    or (board[3 * (r // 3) + i // 3][3 * (c // 3) + i % 3] == n)
            ):
                return False

        return True

    solve(0, 0)  # start the algorithm