from settings import BOARD_SIZE


class Evaluation:

    PATTERN_SCORES = {
        "FIVE": 1000000,
        "OPEN_FOUR": 50000,
        "CLOSED_FOUR": 10000,
        "OPEN_THREE": 3000,
        "CLOSED_THREE": 500,
        "OPEN_TWO": 200,
        "CLOSED_TWO": 50,
    }

    DIRECTIONS = [
        (0, 1),     # Horizontal
        (1, 0),     # Vertical
        (1, 1),     # Diagonal \
        (1, -1),    # Diagonal /
    ]

    @staticmethod
    def evaluate(board, ai_player):

        opponent = 1 if ai_player == 2 else 2

        ai_score = Evaluation.score_player(board, ai_player)
        opponent_score = Evaluation.score_player(board, opponent)

        return ai_score - opponent_score

    @staticmethod
    def score_player(board, player):

        score = 0

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if board.grid[row][col] != player:
                    continue

                for dr, dc in Evaluation.DIRECTIONS:

                    # Don't start counting from the middle of a sequence
                    prev_r = row - dr
                    prev_c = col - dc

                    if (
                        0 <= prev_r < BOARD_SIZE
                        and 0 <= prev_c < BOARD_SIZE
                        and board.grid[prev_r][prev_c] == player
                    ):
                        continue

                    # Count consecutive stones
                    count = 0
                    r = row
                    c = col

                    while (
                        0 <= r < BOARD_SIZE
                        and 0 <= c < BOARD_SIZE
                        and board.grid[r][c] == player
                    ):
                        count += 1
                        r += dr
                        c += dc

                    # Check left side
                    left_open = False

                    if (
                        0 <= prev_r < BOARD_SIZE
                        and 0 <= prev_c < BOARD_SIZE
                        and board.grid[prev_r][prev_c] == 0
                    ):
                        left_open = True

                    # Check right side
                    right_open = False

                    if (
                        0 <= r < BOARD_SIZE
                        and 0 <= c < BOARD_SIZE
                        and board.grid[r][c] == 0
                    ):
                        right_open = True

                    score += Evaluation.pattern_score(
                        count,
                        left_open,
                        right_open
                    )

        return score

    @staticmethod
    def pattern_score(count, left_open, right_open):

        if count >= 5:
            return Evaluation.PATTERN_SCORES["FIVE"]

        if count == 4:

            if left_open and right_open:
                return Evaluation.PATTERN_SCORES["OPEN_FOUR"]

            if left_open or right_open:
                return Evaluation.PATTERN_SCORES["CLOSED_FOUR"]

        elif count == 3:

            if left_open and right_open:
                return Evaluation.PATTERN_SCORES["OPEN_THREE"]

            if left_open or right_open:
                return Evaluation.PATTERN_SCORES["CLOSED_THREE"]

        elif count == 2:

            if left_open and right_open:
                return Evaluation.PATTERN_SCORES["OPEN_TWO"]

            if left_open or right_open:
                return Evaluation.PATTERN_SCORES["CLOSED_TWO"]

        return 0