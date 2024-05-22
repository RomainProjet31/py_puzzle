from pathlib import Path
import pygame
from src.entities.sprites.sprite import Sprite
from src.events.keys import KeyPressed
from src.entities.entity import Entity


class Player(Entity, Sprite):
    H_PLAYER = 32
    W_PLAYER = 16

    _speed = 10
    _color = (0, 0, 255)

    def __init__(self, x: int, y: int, max_step: int = 10) -> None:
        self.max_step = max_step
        self.steps = 0
        Entity.__init__(
            self,
            pygame.rect.Rect(x, y, self.W_PLAYER, self.H_PLAYER),
            self._color,
            self._speed,
        )
        Sprite.__init__(
            self,
            Path(__file__).parent.parent.parent
            / f"assets/mystic_wood/sprites/characters/player.png",
            pygame.Vector2(288, 480),
            pygame.Vector2(48, 48),
        )

    def update(self, dt: float) -> None:
        if self.velocity.x == 0 and self.velocity.y == 0:
            if self.cursor_line != 0:
                self.cursor_col = self.cursor_line = 0
            if self._handle_key_evt():
                self.steps += 1
                self.cursor_line = 3
                self.cursor_col = 0
        Entity.update(self, dt)
        Sprite.update(self, dt)

    def render(self, surface: pygame.Surface) -> None:
        Sprite.render(self, surface, self.rect)

    def _handle_key_evt(self) -> bool:
        """
        return: True if a valid key has been pressed
        """
        valid_key = False
        if KeyPressed.instance().key_pressed == pygame.K_RIGHT:
            self.velocity.x = 1
            valid_key = True
        elif KeyPressed.instance().key_pressed == pygame.K_DOWN:
            self.velocity.y = 1
            valid_key = True
        elif KeyPressed.instance().key_pressed == pygame.K_LEFT:
            self.velocity.x = -1
            valid_key = True
        elif KeyPressed.instance().key_pressed == pygame.K_UP:
            self.velocity.y = -1
            valid_key = True

        return valid_key

    def lost(self) -> bool:
        return self.steps > self.max_step
