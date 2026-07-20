from ai.move_generator import MoveGenerator
from ai.evaluation import Evaluation


class Minimax:

    @staticmethod
    def search(board, depth, maximizing, ai_player):

        # Base case
        if depth == 0:
            return Evaluation.evaluate(board, ai_player), None

        if maximizing:

            best_score = float("-inf")
            best_move = None

            moves = MoveGenerator.get_candidate_moves(board)

            for row, col in moves:

                # Make move
                board.grid[row][col] = ai_player

                score, _ = Minimax.search(
                    board,
                    depth - 1,
                    False,
                    ai_player,
                )

                # Undo move
                board.grid[row][col] = 0

                if score > best_score:
                    best_score = score
                    best_move = (row, col)

            return best_score, best_move

        else:

            opponent = 1 if ai_player == 2 else 2

            best_score = float("inf")
            best_move = None

            moves = MoveGenerator.get_candidate_moves(board)

            for row, col in moves:

                board.grid[row][col] = opponent

                score, _ = Minimax.search(
                    board,
                    depth - 1,
                    True,
                    ai_player,
                )

                board.grid[row][col] = 0

                if score < best_score:
                    best_score = score
                    best_move = (row, col)

            return best_score, best_move