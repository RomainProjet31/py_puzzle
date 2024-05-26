from pathlib import Path
import pygame
from src.sounds.sound_manager import SOUND_MANAGER
from src.entities.sprites.sprite import Sprite
from src.entities.player import Player
from src.entities.entity import Entity


class Block(Entity, Sprite):
    _collider_color = (0, 0, 0)
    _no_collider_color = (255, 255, 255)
    _collider_sprite_path = "assets/mystic_wood/sprites/tilesets/floors/wooden.png"
    _floor_sprite_path = "assets/mystic_wood/sprites/tilesets/grass.png"

    def __init__(
        self, x: int, y: int, collider: bool, magic_block: bool = False
    ) -> None:
        self.magic_block = magic_block
        self.collider = True if magic_block else collider
        # TODO: Extend another class
        file_path = (
            self._collider_sprite_path if self.collider else self._floor_sprite_path
        )

        Entity.__init__(
            self,
            pygame.rect.Rect(x, y, self.TILE_SIZE, self.TILE_SIZE),
            self._collider_color if collider else self._no_collider_color,
            0,
        )
        Sprite.__init__(
            self,
            Path(__file__).parent.parent.parent / file_path,
            pygame.Vector2(16, 16),
            pygame.Vector2(16, 16),
            scale=4,
        )

    def update(self, player: Player) -> None:
        if self.collider and self.rect.colliderect(player.rect):
            self._reveal_if_magic()
            self._stop_player(player)

    def render(self, surface: pygame.Surface) -> None:
        Sprite.render(self, surface, self.rect)

    def _reveal_if_magic(self) -> None:
        if self.magic_block:
            self.collider = False
            self.load_sprite_sheet(self._floor_sprite_path)
            SOUND_MANAGER.play("8-bit-game-1-186975.mp3")

    def _stop_player(self, player: Player) -> None:
        if player.velocity.x > 0:
            player.rect.x = self.rect.left - player.rect.w
        elif player.velocity.x < 0:
            player.rect.x = self.rect.right

        if player.velocity.y > 0:
            player.rect.y = self.rect.top - player.rect.h
        elif player.velocity.y < 0:
            player.rect.y = self.rect.bottom
        player.velocity.x = player.velocity.y = 0
