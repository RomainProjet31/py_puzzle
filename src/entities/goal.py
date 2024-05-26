from pathlib import Path
import pygame
from src.sounds.sound_manager import SOUND_MANAGER
from src.entities.sprites.sprite import Sprite
from src.entities.entity import Entity
from src.entities.player import Player


class Goal(Entity, Sprite):
    W_GOAL = 48
    H_GOAL = 48
    _reached_sound = "coin-collect-retro-8-bit-sound-effect-145251.mp3"

    def __init__(self, x: int, y: int) -> None:
        self._reached = False
        self.ended = False
        super().__init__(
            pygame.rect.Rect(x, y, self.W_GOAL, self.H_GOAL), (255, 0, 0), 0
        )
        Sprite.__init__(
            self,
            Path(__file__).parent.parent.parent
            / f"assets/mystic_wood/sprites/objects/chest_01.png",
            pygame.Vector2(64, 16),
            pygame.Vector2(16, 16),
            limits={0: 4},
            scale=3,
        )

    def update(self, dt: float, player: Player) -> None:
        if not self._reached and self.rect.colliderect(player.rect):
            self._reached = True
            SOUND_MANAGER.play(self._reached_sound)
            self.cursor_col = 0

        Entity.update(self, 0)

        if self._reached is True:
            self.clock += dt
            if (
                self.cursor_col < self.limits[self.cursor_line] - 1
                and self.clock >= 100
            ):
                self.clock = 0
                self.cursor_col += 1
            elif self.cursor_col >= self.limits[self.cursor_line] - 1:
                self.ended = True

    def render(self, surface: pygame.Surface) -> None:
        Sprite.render(self, surface, self.rect)
