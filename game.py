import pygame

from board import Board
from button import Button

from settings import (
    WINDOW_WIDTH,
    WINDOW_HEIGHT,
    FPS,
    TITLE,
    BACKGROUND_COLOR,
)


class Game:

    def __init__(self):

        self.screen = pygame.display.set_mode(
            (WINDOW_WIDTH, WINDOW_HEIGHT)
        )

        pygame.display.set_caption(TITLE)

        self.clock = pygame.time.Clock()

        self.running = True

        self.board = Board()

        # 1 = Black, 2 = White
        self.current_player = 1

        self.game_over = False
        self.winner = None

        # Buttons
        self.restart_button = Button(
            170,
            920,
            160,
            40,
            "Restart",
        )

        self.exit_button = Button(
            570,
            920,
            160,
            40,
            "Exit",
        )

    def restart_game(self):

        self.board = Board()
        self.current_player = 1
        self.game_over = False
        self.winner = None

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Restart
                if self.restart_button.is_clicked(event):
                    self.restart_game()
                    continue

                # Exit
                if self.exit_button.is_clicked(event):
                    self.running = False
                    continue

                # Don't allow moves after game over
                if self.game_over:
                    continue

                row, col = self.board.get_cell(event.pos)

                if row is None:
                    continue

                if self.board.is_empty(row, col):

                    self.board.place_stone(
                        row,
                        col,
                        self.current_player,
                    )

                    if self.board.check_winner(self.current_player):

                        self.game_over = True
                        self.winner = self.current_player

                    else:

                        if self.current_player == 1:
                            self.current_player = 2
                        else:
                            self.current_player = 1

    def update(self):
        pass

    def draw(self):

        self.screen.fill(BACKGROUND_COLOR)

        # -----------------------------
        # Game Title
        # -----------------------------
        title_font = pygame.font.SysFont(
            "Arial",
            42,
            bold=True,
        )

        title = title_font.render(
            "GOMOKU AI",
            True,
            (40, 40, 40),
        )

        title_rect = title.get_rect(
            center=(WINDOW_WIDTH // 2, 35)
        )

        self.screen.blit(title, title_rect)

        # -----------------------------
        # Draw Board
        # -----------------------------
        self.board.draw(self.screen)

        # -----------------------------
        # Winner Screen
        # -----------------------------
        if self.game_over:

            # Dark transparent overlay
            overlay = pygame.Surface(
                (WINDOW_WIDTH, WINDOW_HEIGHT),
                pygame.SRCALPHA,
            )

            overlay.fill((0, 0, 0, 100))

            self.screen.blit(overlay, (0, 0))

            winner_font = pygame.font.SysFont(
                "Arial",
                70,
                bold=True,
            )

            if self.winner == 1:
                message = "BLACK WINS!"
            else:
                message = "WHITE WINS!"

            winner_text = winner_font.render(
                message,
                True,
                (255, 255, 255),
            )

            winner_rect = winner_text.get_rect(
                center=(
                    WINDOW_WIDTH // 2,
                    WINDOW_HEIGHT // 2,
                )
            )

            self.screen.blit(
                winner_text,
                winner_rect,
            )

        # -----------------------------
        # Buttons
        # -----------------------------
        self.restart_button.draw(self.screen)
        self.exit_button.draw(self.screen)

        pygame.display.flip()

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)