from ai.move_generator import MoveGenerator
from ai.evaluation import Evaluation


class AlphaBeta:

    @staticmethod
    def search(board, depth, alpha, beta, maximizing, ai_player):

        opponent = 1 if ai_player == 2 else 2

        # -----------------------------
        # Terminal States
        # -----------------------------
        if board.check_winner(ai_player):
            return 1000000, None

        if board.check_winner(opponent):
            return -1000000, None

        if depth == 0:
            return Evaluation.evaluate(board, ai_player), None

        moves = MoveGenerator.get_candidate_moves(board)

        if not moves:
            return Evaluation.evaluate(board, ai_player), None

        # ==========================================================
        # ROOT NODE OPTIMIZATIONS
        # Only perform these once at the top of the search.
        # ==========================================================
        if maximizing and depth >= 3:

            # 1. Immediate Winning Move
            for row, col in moves:

                board.place_stone(row, col, ai_player)

                if board.check_winner(ai_player):
                    board.grid[row][col] = 0
                    return 1000000, (row, col)

                board.grid[row][col] = 0

            # 2. Immediate Block
            for row, col in moves:

                board.place_stone(row, col, opponent)

                if board.check_winner(opponent):
                    board.grid[row][col] = 0
                    return 900000, (row, col)

                board.grid[row][col] = 0

        # ==========================================================
        # Move Ordering
        # Evaluate candidate moves first so Alpha-Beta prunes earlier.
        # ==========================================================
        ordered_moves = []

        for row, col in moves:

            player = ai_player if maximizing else opponent

            board.place_stone(row, col, player)

            score = Evaluation.evaluate(board, ai_player)

            board.grid[row][col] = 0

            ordered_moves.append((score, row, col))

        ordered_moves.sort(reverse=maximizing)

        # ==========================================================
        # Maximizing Player (AI)
        # ==========================================================
        if maximizing:

            best_score = float("-inf")
            best_move = None

            for _, row, col in ordered_moves:

                board.place_stone(row, col, ai_player)

                score, _ = AlphaBeta.search(
                    board,
                    depth - 1,
                    alpha,
                    beta,
                    False,
                    ai_player
                )

                board.grid[row][col] = 0

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

                alpha = max(alpha, best_score)

                if alpha >= beta:
                    break

            return best_score, best_move

        # ==========================================================
        # Minimizing Player (Opponent)
        # ==========================================================
        else:

            best_score = float("inf")
            best_move = None

            for _, row, col in ordered_moves:

                board.place_stone(row, col, opponent)

                score, _ = AlphaBeta.search(
                    board,
                    depth - 1,
                    alpha,
                    beta,
                    True,
                    ai_player
                )

                board.grid[row][col] = 0

                if score < best_score:
                    best_score = score
                    best_move = (row, col)

                beta = min(beta, best_score)

                if alpha >= beta:
                    break

            return best_score, best_move