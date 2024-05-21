import pygame


class Entity:
    """
    Not really like an entity component system
    """

    TILE_SIZE = 64

    def __init__(self, rect: pygame.Rect, color, speed: int) -> None:
        self.velocity = pygame.Vector2()
        self.speed = speed
        self.color = color
        self.rect = rect

    def update(self, dt: float) -> None:
        self.rect.x += self.velocity.x * self.speed
        self.rect.y += self.velocity.y * self.speed

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, self.color, self.rect)
