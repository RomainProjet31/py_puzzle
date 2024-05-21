import pygame
from src.entities.entity import Entity
from src.entities.player import Player


class Goal(Entity):

    W_GOAL = 32
    H_GOAL = 32

    def __init__(self, x: int, y: int) -> None:
        self.reached = False
        super().__init__(
            pygame.rect.Rect(x, y, self.W_GOAL, self.H_GOAL), (255, 0, 0), 0
        )

    def update(self, player: Player) -> None:
        if self.rect.colliderect(player.rect):
            self.reached = True
            self.color = (0, 255, 0)
