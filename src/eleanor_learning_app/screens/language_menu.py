from __future__ import annotations

import pygame

from eleanor_learning_app.config import Language


class LanguageMenuScreen:
    def __init__(self, app: object, languages: list[Language]) -> None:
        self.app = app
        self.languages = languages
        self.button_rects: list[tuple[pygame.Rect, Language]] = []

    def draw(self, surface: pygame.Surface) -> None:
        width, height = surface.get_size()
        surface.fill((255, 245, 168))
        self.button_rects = []

        title_font = pygame.font.Font(None, 78)
        button_font = pygame.font.Font(None, 64)
        title = title_font.render("Choose Language", True, (47, 76, 107))
        surface.blit(title, title.get_rect(center=(width // 2, int(height * 0.22))))

        button_width = min(420, width - 120)
        button_height = 110
        gap = 36
        total_height = len(self.languages) * button_height + max(0, len(self.languages) - 1) * gap
        top = int(height * 0.52 - total_height / 2)

        colors = [(108, 210, 180), (255, 153, 102), (168, 145, 255)]
        for index, language in enumerate(self.languages):
            rect = pygame.Rect(0, top + index * (button_height + gap), button_width, button_height)
            rect.centerx = width // 2
            self.button_rects.append((rect, language))

            pygame.draw.rect(surface, colors[index % len(colors)], rect, border_radius=24)
            pygame.draw.rect(surface, (48, 61, 88), rect, width=4, border_radius=24)
            label = button_font.render(language.display_name, True, (28, 38, 58))
            surface.blit(label, label.get_rect(center=rect.center))

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            for rect, language in self.button_rects:
                if rect.collidepoint(event.pos):
                    self.app.start_number_game(language)
                    return
