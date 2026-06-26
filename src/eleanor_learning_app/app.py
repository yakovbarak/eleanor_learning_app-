from __future__ import annotations

import pygame

from eleanor_learning_app.assets import SoundPlayer
from eleanor_learning_app.config import Language, load_languages
from eleanor_learning_app.screens.language_menu import LanguageMenuScreen
from eleanor_learning_app.screens.main_menu import MainMenuScreen
from eleanor_learning_app.screens.number_game_screen import NumberGameScreen


class EleanorLearningApp:
    def __init__(self, size: tuple[int, int] = (1024, 768)) -> None:
        pygame.init()
        pygame.display.set_caption("Eleanor Learning App")
        self.screen = pygame.display.set_mode(size, pygame.RESIZABLE)
        self.clock = pygame.time.Clock()
        self.languages = load_languages()
        self.sound_player = SoundPlayer()
        self.current_screen: MainMenuScreen | LanguageMenuScreen | NumberGameScreen
        self.current_screen = MainMenuScreen(self)

    def show_language_menu(self) -> None:
        self.current_screen = LanguageMenuScreen(self, self.languages)

    def start_number_game(self, language: Language) -> None:
        self.current_screen = NumberGameScreen(language, self.sound_player)

    def run(self) -> None:
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                else:
                    self.current_screen.handle_event(event)

            if hasattr(self.current_screen, "update"):
                self.current_screen.update()

            self.current_screen.draw(self.screen)
            pygame.display.flip()
            self.clock.tick(60)

        pygame.quit()
