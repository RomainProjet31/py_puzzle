import pygame


class Help:
    """
    Class to help the player to know better about the game
    """

    def __init__(self, screen_size: tuple) -> None:
        self.display = False
        self.bg = pygame.rect.Rect(0, 0, screen_size[0], screen_size[1])
        self.font = pygame.font.SysFont(None, 48)
        self.txt = self.font.render("TEST", True, (255, 255, 255))

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (0, 0, 0), self.bg)
        surface.blit(self.txt, (10, 10))
