import pygame
from src.maps.map import Map
from src.entities.player import Player


class ATH:
    ATH_HEIGHT = 80
    _game_over_msg = "GAME OVER"
    _game_won_msg = "GAME WON"

    def __init__(self, map: Map, w_surface: int, h_surface: int) -> None:
        self.map = map
        self.surface_size = (w_surface, h_surface)
        self.font = pygame.font.SysFont(None, 48)
        self.bg = pygame.rect.Rect(0, 0, w_surface, self.ATH_HEIGHT)

        self.screen_bg = pygame.rect.Rect(0, 0, w_surface, h_surface)
        self.game_over_img = self.font.render(
            self._game_over_msg, True, (255, 255, 255)
        )
        self.game_over_pos = self._get_txt_pos(self._game_over_msg)

        self.game_won_img = self.font.render(self._game_won_msg, True, (255, 255, 255))
        self.game_won_pos = self._get_txt_pos(self._game_won_msg)

        self.flg_game_over = False
        self.flg_game_won = False
        self.rect_steps = []

    def update(self) -> None:
        self._compute_steps()

    def render(self, surface: pygame.Surface) -> None:
        if self.flg_game_over or self.flg_game_won:
            pygame.draw.rect(surface, (0, 0, 0), self.screen_bg)
            if self.flg_game_over:
                surface.blit(self.game_over_img, self.game_over_pos)
            elif self.flg_game_won:
                surface.blit(self.game_won_img, self.game_won_pos)
        else:
            pygame.draw.rect(surface, (146, 146, 146), self.bg)
            for rect in self.rect_steps:
                pygame.draw.rect(surface, (0, 0, 0), rect)

    def _get_txt_pos(self, txt: str) -> tuple:
        w_goi, h_goi = self.font.size(txt)
        return (
            self.surface_size[0] / 2 - w_goi / 2,
            self.surface_size[1] / 2 - h_goi / 2,
        )

    def _compute_steps(self) -> None:
        x = 10
        self.rect_steps = []
        steps_left = self.map.player.max_step - self.map.player.steps
        for _ in range(0, steps_left):
            rect = pygame.rect.Rect(x, 10, 16, 32)
            self.rect_steps.append(rect)
            x += rect.w + 5
