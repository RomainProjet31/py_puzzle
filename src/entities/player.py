from pathlib import Path
import pygame
from src.sounds.sound_manager import SOUND_MANAGER
from src.entities.sprites.sprite import Sprite
from src.events.keys import KEY_PRESSED
from src.entities.entity import Entity


class Player(Entity, Sprite):
    H_PLAYER = 64
    W_PLAYER = 64
    _idle_line = 1
    _move_line = 3
    _max_cols = {_idle_line: 4, _move_line: 6}
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
            / f"assets/mystic_wood/sprites/characters/slime.png",
            pygame.Vector2(224, 416),
            pygame.Vector2(32, 32),
            limits=self._max_cols,
            scale=2,
        )
        self.dest_rect = self._align_collider_and_pos()
        self.cursor_line = self._idle_line

    def update(self, dt: float) -> None:
        if self.velocity.x == 0 and self.velocity.y == 0:
            if self.cursor_line != self._idle_line:
                self.cursor_line = self._idle_line
                self.cursor_col = 0

            if self._handle_key_evt():
                self.steps += 1
                self.cursor_line = self._move_line
                self.cursor_col = 0
        else:
            SOUND_MANAGER.play("snow-step-2-102324.mp3")
        Entity.update(self, dt)
        self.dest_rect = self._align_collider_and_pos()
        Sprite.update(self, dt)

    def render(self, surface: pygame.Surface) -> None:
        Sprite.render(self, surface, self.rect)

    def _align_collider_and_pos(self) -> pygame.rect.Rect:
        x = self.rect.x - self.rect.w / 3.0
        y = self.rect.y - self.rect.h / 3.0
        w = self.rect.w
        h = self.rect.h
        return pygame.rect.Rect(x, y, w, h)

    def _handle_key_evt(self) -> bool:
        """
        return: True if a valid key has been pressed
        """
        valid_key = False
        if KEY_PRESSED.key_pressed == pygame.K_RIGHT:
            self.velocity.x = 1
            valid_key = True
        elif KEY_PRESSED.key_pressed == pygame.K_DOWN:
            self.velocity.y = 1
            valid_key = True
        elif KEY_PRESSED.key_pressed == pygame.K_LEFT:
            self.velocity.x = -1
            valid_key = True
        elif KEY_PRESSED.key_pressed == pygame.K_UP:
            self.velocity.y = -1
            valid_key = True

        return valid_key

    def lost(self) -> bool:
        return self.steps > self.max_step
