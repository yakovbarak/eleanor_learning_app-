from __future__ import annotations

from pathlib import Path

import pygame


class SoundPlayer:
    def __init__(self) -> None:
        self._audio_available = False
        try:
            if not pygame.mixer.get_init():
                pygame.mixer.init()
            self._audio_available = True
        except pygame.error:
            self._audio_available = False

    def play_number(self, sound_folder: Path, number: int) -> None:
        if not self._audio_available:
            return

        sound_path = sound_folder / f"{number}.wav"
        if not sound_path.exists():
            return

        try:
            pygame.mixer.Sound(str(sound_path)).play()
        except pygame.error:
            return
