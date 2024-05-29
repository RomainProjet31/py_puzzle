from pygame import Surface, Vector2
import pygame


class _TextManager:

    _white = (255, 255, 255)

    def __init__(self) -> None:
        self.font = pygame.font.SysFont(None, 48)

    def render(
        self, surface: Surface, text: str, pos: Vector2, color=_white, size: int = 48
    ) -> None:
        if size != 48 and size > 0:
            font = pygame.font.SysFont(None, size)
        else:
            font = self.font
        surface.blit(font.render(text, True, color), pos)

    def size(self, text: str) -> tuple:
        return self.font.size(text)

    def render_at_center(self, text: str, surface: Surface, color=_white) -> Vector2:
        surf_w = surface.get_width()
        surf_h = surface.get_height()
        w_goi, h_goi = self.font.size(text)
        x = surf_w / 2 - w_goi / 2
        y = surf_h / 2 - h_goi / 2
        pos_txt = Vector2(x, y)
        self.render(surface, text, pos_txt, color)
        return pos_txt

    def render_at_center_x(
        self, text: str, surface: Surface, y: int, color=_white
    ) -> None:
        surf_w = surface.get_width()
        w_goi = self.font.size(text)[0]
        x = surf_w / 2 - w_goi / 2
        pos_txt = Vector2(x, y)
        self.render(surface, text, pos_txt, color)
        return pos_txt

    def render_texts(
        self,
        lst_text: list[str],
        surface: Surface,
        base_pos: Vector2,
        color=_white,
        size: int = 48,
    ) -> int:
        """
        :return The current y coordinate
        """
        offset_y = 5
        current_pos = base_pos
        for txt in lst_text:
            self.render(surface, txt, current_pos, color, size)
            current_pos.y += self.size(txt)[1] + offset_y
        return current_pos.y


TEXT_MANAGER = _TextManager()
