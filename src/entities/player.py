import pygame
from src.events.keys import KeyPressed
from src.entities.entity import Entity


class Player(Entity):
    H_PLAYER = 32
    W_PLAYER = 16

    _speed = 10
    _color = (0, 0, 255)

    def __init__(self, x: int, y: int, max_step: int = 10) -> None:
        self.max_step = max_step
        self.steps = 0
        super().__init__(
            pygame.rect.Rect(x, y, self.W_PLAYER, self.H_PLAYER),
            self._color,
            self._speed,
        )

    def update(self, dt: float) -> None:
        if self.velocity.x == 0 and self.velocity.y == 0:
            if self._handle_key_evt():
                self.steps += 1
        super().update(dt)

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
