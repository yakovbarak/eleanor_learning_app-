from __future__ import annotations

import pygame

from eleanor_learning_app.assets import SoundPlayer
from eleanor_learning_app.config import Language
from eleanor_learning_app.games.numbers import NumberGame, NumberRound


class NumberGameScreen:
    def __init__(self, language: Language, sound_player: SoundPlayer) -> None:
        self.language = language
        self.sound_player = sound_player
        self.game = NumberGame()
        self.round: NumberRound = self.game.new_round()
        self.feedback = ""
        self.feedback_color = (35, 130, 78)
        self.advance_at: int | None = None
        self.button_rects: list[tuple[pygame.Rect, int]] = []
        self.sound_player.play_number(self.language.number_sound_path, self.round.target)

    def draw(self, surface: pygame.Surface) -> None:
        width, height = surface.get_size()
        surface.fill((198, 237, 255))
        self.button_rects = []

        prompt_font = pygame.font.Font(None, 84)
        digit_font = pygame.font.Font(None, 112)
        feedback_font = pygame.font.Font(None, 60)

        prompt = prompt_font.render(f"Find: {self.round.target}", True, (40, 59, 95))
        surface.blit(prompt, prompt.get_rect(center=(width // 2, int(height * 0.18))))

        button_size = min(180, max(120, (width - 180) // 3))
        gap = min(55, max(24, (width - button_size * 3) // 5))
        row_width = button_size * 3 + gap * 2
        left = (width - row_width) // 2
        top = int(height * 0.42)

        colors = [(255, 128, 134), (101, 203, 146), (255, 211, 86)]
        for index, choice in enumerate(self.round.choices):
            rect = pygame.Rect(left + index * (button_size + gap), top, button_size, button_size)
            self.button_rects.append((rect, choice))
            pygame.draw.rect(surface, colors[index], rect, border_radius=24)
            pygame.draw.rect(surface, (48, 61, 88), rect, width=5, border_radius=24)
            digit = digit_font.render(str(choice), True, (25, 35, 58))
            surface.blit(digit, digit.get_rect(center=rect.center))

        if self.feedback:
            feedback = feedback_font.render(self.feedback, True, self.feedback_color)
            surface.blit(feedback, feedback.get_rect(center=(width // 2, int(height * 0.78))))

    def update(self) -> None:
        if self.advance_at is not None and pygame.time.get_ticks() >= self.advance_at:
            self._next_round()

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type != pygame.MOUSEBUTTONDOWN or event.button != 1:
            return

        if self.advance_at is not None:
            self._next_round()
            return

        for rect, choice in self.button_rects:
            if rect.collidepoint(event.pos):
                self._choose(choice)
                return

    def _choose(self, choice: int) -> None:
        if self.game.is_correct(choice, self.round.target):
            self.feedback = "Great!"
            self.feedback_color = (31, 143, 86)
            self.advance_at = pygame.time.get_ticks() + 900
        else:
            self.feedback = "Try again"
            self.feedback_color = (166, 80, 54)

    def _next_round(self) -> None:
        self.round = self.game.new_round()
        self.feedback = ""
        self.advance_at = None
        self.sound_player.play_number(self.language.number_sound_path, self.round.target)
