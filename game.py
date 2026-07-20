import pygame

from board import Board
from button import Button
from ai.ai_player import AIPlayer

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

        # Player 1 = Human (Black)
        # Player 2 = AI (White)
        self.current_player = 1
        self.ai_player = 2

        self.game_over = False
        self.winner = None

        # AI delay
        self.ai_move_time = 0

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
        self.ai_move_time = 0

    def handle_events(self):

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                self.running = False

            elif event.type == pygame.MOUSEBUTTONDOWN:

                # Restart button
                if self.restart_button.is_clicked(event):
                    self.restart_game()
                    continue

                # Exit button
                if self.exit_button.is_clicked(event):
                    self.running = False
                    continue

                # Ignore board clicks if game ended
                if self.game_over:
                    continue

                # Ignore clicks during AI turn
                if self.current_player == self.ai_player:
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

                        # Switch to AI
                        self.current_player = self.ai_player

                        # AI thinks for 0.5 second
                        self.ai_move_time = pygame.time.get_ticks() + 500

    def update(self):

        if (
            not self.game_over
            and self.current_player == self.ai_player
            and pygame.time.get_ticks() >= self.ai_move_time
        ):

            move = AIPlayer.get_best_move(
                self.board,
                self.ai_player,
                depth=3
            )

            if move:

                row, col = move

                self.board.place_stone(
                    row,
                    col,
                    self.ai_player
                )

                if self.board.check_winner(self.ai_player):

                    self.game_over = True
                    self.winner = self.ai_player

                else:

                    self.current_player = 1

    def draw(self):

        self.screen.fill(BACKGROUND_COLOR)

        # -------------------------
        # Title
        # -------------------------
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

        # -------------------------
        # Turn Indicator
        # -------------------------
        info_font = pygame.font.SysFont(
            "Arial",
            24,
            bold=True,
        )

        if not self.game_over:

            if self.current_player == 1:
                text = "Your Turn (Black)"
            else:
                text = "AI Thinking..."

            info = info_font.render(
                text,
                True,
                (60, 60, 60),
            )

            self.screen.blit(info, (40, 60))

        # -------------------------
        # Board
        # -------------------------
        self.board.draw(self.screen)

        # -------------------------
        # Winner
        # -------------------------
        if self.game_over:

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

        # -------------------------
        # Buttons
        # -------------------------
        self.restart_button.draw(self.screen)
        self.exit_button.draw(self.screen)

        pygame.display.flip()

    def run(self):

        while self.running:

            self.handle_events()

            self.update()

            self.draw()

            self.clock.tick(FPS)
