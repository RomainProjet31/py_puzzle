import os
from pathlib import Path
import pygame


class SoundNotFound(Exception):
    pass


class _SoundManager:

    _asset_path = Path(__file__).parent.parent.parent / "assets/sounds"

    def __init__(self) -> None:
        """
        Here all the sound will end to be loaded then store here
        """
        self.sounds: dict[str, pygame.mixer.Sound] = {}
        # One channel per sound
        self.channels: dict[str, pygame.mixer.Channel] = {}
        pygame.mixer.init()

    def play(self, sound_name: str) -> None:
        """
        :param sound_name -> the name of the file with its extension
        """
        if sound_name not in self.sounds:
            self.sounds[sound_name] = self._load(sound_name)

        sound = self.sounds[sound_name]
        channel = self.channels[sound_name]
        if not channel.get_busy():
            channel.play(sound)

    def _load(self, sound_name: str) -> pygame.mixer.Sound:
        self.channels[sound_name] = pygame.mixer.Channel(len(self.sounds))

        sound_path = f"{self._asset_path}/{sound_name}"

        if not os.path.isfile(sound_path):
            raise SoundNotFound(f"The file at {sound_path} does not exist")

        return pygame.mixer.Sound(sound_path)


SOUND_MANAGER = _SoundManager()
