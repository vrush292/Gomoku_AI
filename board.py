import pygame

from settings import (
    BOARD_SIZE,
    CELL_SIZE,
    MARGIN,
    GRID_COLOR,
    BLACK_STONE,
    WHITE_STONE,
    STONE_RADIUS,
)


class Board:
    def __init__(self):
        # 0 = Empty
        # 1 = Black
        # 2 = White
        self.grid = [
            [0 for _ in range(BOARD_SIZE)]
            for _ in range(BOARD_SIZE)
        ]

    def draw(self, screen):
        """Draw board and stones."""

        # Draw horizontal grid lines
        for row in range(BOARD_SIZE):

            start_x = MARGIN
            start_y = MARGIN + row * CELL_SIZE

            end_x = MARGIN + (BOARD_SIZE - 1) * CELL_SIZE
            end_y = start_y

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (start_x, start_y),
                (end_x, end_y),
                2,
            )

        # Draw vertical grid lines
        for col in range(BOARD_SIZE):

            start_x = MARGIN + col * CELL_SIZE
            start_y = MARGIN

            end_x = start_x
            end_y = MARGIN + (BOARD_SIZE - 1) * CELL_SIZE

            pygame.draw.line(
                screen,
                GRID_COLOR,
                (start_x, start_y),
                (end_x, end_y),
                2,
            )

        # Draw stones
        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                value = self.grid[row][col]

                if value == 0:
                    continue

                x = MARGIN + col * CELL_SIZE
                y = MARGIN + row * CELL_SIZE

                color = BLACK_STONE if value == 1 else WHITE_STONE

                pygame.draw.circle(
                    screen,
                    color,
                    (x, y),
                    STONE_RADIUS,
                )

    def get_cell(self, mouse_pos):

        mouse_x, mouse_y = mouse_pos

        col = round((mouse_x - MARGIN) / CELL_SIZE)
        row = round((mouse_y - MARGIN) / CELL_SIZE)

        if 0 <= row < BOARD_SIZE and 0 <= col < BOARD_SIZE:
            return row, col

        return None, None

    def is_empty(self, row, col):
        return self.grid[row][col] == 0

    def place_stone(self, row, col, player):
        self.grid[row][col] = player

    def check_winner(self, player):

        directions = [
            (0, 1),   # Horizontal
            (1, 0),   # Vertical
            (1, 1),   # Diagonal \
            (1, -1),  # Diagonal /
        ]

        for row in range(BOARD_SIZE):
            for col in range(BOARD_SIZE):

                if self.grid[row][col] != player:
                    continue

                for dr, dc in directions:

                    count = 1

                    r = row + dr
                    c = col + dc

                    while (
                        0 <= r < BOARD_SIZE
                        and 0 <= c < BOARD_SIZE
                        and self.grid[r][c] == player
                    ):

                        count += 1

                        if count == 5:
                            return True

                        r += dr
                        c += dc

        return False