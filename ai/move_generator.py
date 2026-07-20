from settings import BOARD_SIZE


class MoveGenerator:

    @staticmethod
    def get_candidate_moves(board):

        candidates = set()

        has_stones = False

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if board.grid[row][col] != 0:

                    has_stones = True

                    for dr in range(-2, 3):
                        for dc in range(-2, 3):

                            r = row + dr
                            c = col + dc

                            if (
                                0 <= r < BOARD_SIZE
                                and 0 <= c < BOARD_SIZE
                                and board.grid[r][c] == 0
                            ):
                                candidates.add((r, c))

        # First move of the game
        if not has_stones:
            center = BOARD_SIZE // 2
            return [(center, center)]

        return list(candidates)