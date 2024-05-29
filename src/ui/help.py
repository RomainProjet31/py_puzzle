import pygame

from src.ui.text_manager import TEXT_MANAGER


class Help:
    """
    Class to help the player to know better about the game
    """

    _directional = "Use the directional keys to move"
    _move_lock = "Once you moved, only an obstacle can stop you"
    _goal = "The chests are the goals. Reach them all to end the level"
    _special_blocks = "Do not trust the walls ;)"
    _image_path = "./assets/help/tutorial.png"

    def __init__(self, screen_size: tuple) -> None:
        self.texts_to_render = [
            self._directional,
            self._move_lock,
            self._goal,
            self._special_blocks,
        ]
        self.display = False
        self.bg = pygame.rect.Rect(0, 0, screen_size[0], screen_size[1])
        self.font = pygame.font.SysFont(None, 48)
        self.tutorial_img = pygame.image.load(self._image_path).convert_alpha()
        self.scaled = False

    def render(self, surface: pygame.Surface) -> None:
        pygame.draw.rect(surface, (0, 0, 0), self.bg)
        curr_y = TEXT_MANAGER.render_texts(
            self.texts_to_render, surface, pygame.Vector2(10, 10), size=30
        )
        if not self.scaled:
            self.tutorial_img = pygame.transform.scale(
                self.tutorial_img,
                (surface.get_width() - 20, surface.get_height() - curr_y - 10),
            )
            self.scaled = True
        surface.blit(self.tutorial_img, (10, curr_y))
