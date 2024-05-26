import pygame
from src.events.keys import KEY_PRESSED
from src.maps.map import Map
from src.ui.help import Help
from src.ui.text_manager import TEXT_MANAGER


class ATH:
    ATH_HEIGHT = 80
    _game_over_msg = "GAME OVER"
    _game_won_msg = "GAME WON"
    _help_msg = "Press [h] for help"
    _restart_msg = "Press [r] to restart"

    def __init__(self, map: Map, w_surface: int, h_surface: int) -> None:
        self.help = Help((w_surface, h_surface))
        self.map = map
        self.screen_rect = pygame.rect.Rect(0, 0, w_surface, h_surface)
        self.bg = pygame.rect.Rect(0, 0, w_surface, self.ATH_HEIGHT)
        self.help_pos = pygame.Vector2(
            w_surface - TEXT_MANAGER.size(self._help_msg)[0], 10
        )
        self.flg_game_over = False
        self.flg_game_won = False
        self.rect_steps = []

    def update(self) -> None:
        if KEY_PRESSED.key_pressed == pygame.K_h:
            self.help.display = not self.help.display

        if not self.help.display:
            x = 10
            self.rect_steps = []
            steps_left = self.map.player.max_step - self.map.player.steps
            for _ in range(0, steps_left):
                rect = pygame.rect.Rect(x, 10, 16, 32)
                self.rect_steps.append(rect)
                x += rect.w + 5

    def render(self, surface: pygame.Surface) -> None:
        if self.help.display:
            self.help.render(surface)
        else:
            self._render_self(surface)

    def _render_self(self, surface: pygame.Surface) -> None:
        if self.flg_game_over or self.flg_game_won:
            pygame.draw.rect(surface, (0, 0, 0), self.screen_rect)
            self._render_end_lvl(surface)
        else:
            pygame.draw.rect(surface, (146, 146, 146), self.bg)
            # Render the steps
            for rect in self.rect_steps:
                pygame.draw.rect(surface, (0, 0, 0), rect)
            # Render the help message
            TEXT_MANAGER.render(surface, self._help_msg, self.help_pos)

    def _render_end_lvl(self, surface: pygame.Surface) -> None:
        msg = self._game_over_msg if self.flg_game_over else self._game_won_msg
        pos_go = TEXT_MANAGER.render_at_center(msg, surface)
        if self.flg_game_over:
            y = pos_go[1] + TEXT_MANAGER.size(msg)[1] + 5
            TEXT_MANAGER.render_at_center_x(self._restart_msg, surface, y)
