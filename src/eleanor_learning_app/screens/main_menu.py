from __future__ import annotations

import pygame


class MainMenuScreen:
    def __init__(self, app: object) -> None:
        self.app = app
        self.start_rect = pygame.Rect(0, 0, 320, 120)

    def draw(self, surface: pygame.Surface) -> None:
        width, height = surface.get_size()
        surface.fill((114, 214, 255))
        self.start_rect.center = (width // 2, int(height * 0.62))

        title_font = pygame.font.Font(None, 96)
        button_font = pygame.font.Font(None, 72)
        title = title_font.render("Numbers!", True, (32, 63, 122))
        title_rect = title.get_rect(center=(width // 2, int(height * 0.28)))
        surface.blit(title, title_rect)

        pygame.draw.circle(surface, (255, 234, 94), (int(width * 0.18), int(height * 0.22)), 70)
        pygame.draw.circle(surface, (255, 139, 148), (int(width * 0.82), int(height * 0.28)), 55)
        pygame.draw.circle(surface, (134, 231, 160), (int(width * 0.25), int(height * 0.78)), 45)

        pygame.draw.rect(surface, (255, 177, 66), self.start_rect, border_radius=28)
        pygame.draw.rect(surface, (144, 82, 32), self.start_rect, width=5, border_radius=28)
        label = button_font.render("Start", True, (72, 43, 22))
        surface.blit(label, label.get_rect(center=self.start_rect.center))

    def handle_event(self, event: pygame.event.Event) -> None:
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            if self.start_rect.collidepoint(event.pos):
                self.app.show_language_menu()
