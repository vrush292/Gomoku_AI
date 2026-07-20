from ai.alpha_beta import AlphaBeta


class AIPlayer:

    @staticmethod
    def get_best_move(board, player, depth=3):

        _, move = AlphaBeta.search(
            board,
            depth,
            float("-inf"),
            float("inf"),
            True,
            player,
        )

        return move