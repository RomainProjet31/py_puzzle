import pygame


class Sprite:

    def __init__(
        self,
        sprite_path: str,
        file_size: pygame.Vector2,
        sprite_size: pygame.Vector2,
        scale: int = 1,
        limits: dict = {},
    ) -> None:
        self.clock = 0
        self.scale = scale
        self.cursor_col = 0
        self.cursor_line = 0
        self.limits = limits
        self.file_size = file_size
        self.images: list[list] = []
        self.sprite_size = sprite_size

        self.load_sprite_sheet(sprite_path)

    def update(self, dt: float) -> None:
        self.clock += dt
        if self.clock >= 100:
            self.clock = 0
            self.cursor_col += 1
            limit_achieved = (
                self.cursor_line in self.limits
                and self.cursor_col == self.limits[self.cursor_line]
            )
            if self.cursor_col == len(self.images[self.cursor_line]) or limit_achieved:
                self.cursor_col = 0

    def render(self, screen: pygame.Surface, rect: pygame.Rect) -> None:
        screen.blit(self.images[self.cursor_line][self.cursor_col], (rect.x, rect.y))

    def load_sprite_sheet(self, sprite_path) -> None:
        self.sprite_sheet = pygame.image.load(sprite_path).convert_alpha()
        self._load_images()

    def _load_images(self) -> None:
        self.images = []
        max_y = int(self.file_size.y / self.sprite_size.y)
        max_x = int(self.file_size.x / self.sprite_size.x)

        for y in range(0, max_y):
            line = []
            for x in range(0, max_x):
                img = self._get_image(x, y, self.sprite_size.x, self.sprite_size.y)
                line.append(img)
            self.images.append(line)

    def _get_image(self, x, y, w, h, colour=(0, 0, 0)):
        image = pygame.Surface((w, h)).convert_alpha()
        image.blit(self.sprite_sheet, (0, 0), ((x * w), (y * h), w, h))
        image = pygame.transform.scale(image, (w * self.scale, h * self.scale))
        image.set_colorkey(colour)
        return image
