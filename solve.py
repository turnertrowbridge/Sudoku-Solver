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