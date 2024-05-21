import pygame
from src.entities.player import Player
from src.entities.entity import Entity


class Block(Entity):
    _collider_color = (0, 0, 0)
    _no_collider_color = (255, 255, 255)

    def __init__(self, x: int, y: int, collider: bool) -> None:
        self.collider = collider
        super().__init__(
            pygame.rect.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE),
            self._collider_color if collider else self._no_collider_color,
            0,
        )

    def update(self, player: Player) -> None:
        if self.collider and self.rect.colliderect(player.rect):
            if player.velocity.x > 0:
                player.rect.x = self.rect.left - player.rect.w
            elif player.velocity.x < 0:
                player.rect.x = self.rect.right

            if player.velocity.y > 0:
                player.rect.y = self.rect.top - player.rect.h
            elif player.velocity.y < 0:
                player.rect.y = self.rect.bottom
            player.velocity.x = player.velocity.y = 0
