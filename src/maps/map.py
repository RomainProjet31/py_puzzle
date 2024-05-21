import os
from pathlib import Path
from pygame import Surface
from src.entities.goal import Goal
from src.entities.block import Block
from src.entities.player import Player


class Map:

    _floor_idx = "0"
    _block_idx = "1"
    _player_idx = "2"
    _goal_idx = "3"
    _tile_size = 64

    def __init__(self) -> None:
        self.map_nb = 1
        self.player: Player = None
        self.blocks: list[Block] = None
        self.goals: list[Goal] = None

    def load_map(self, offset_y: int = 0) -> None:
        self.goals = []
        self.blocks = []
        path = Path(__file__).parent.parent.parent / f"assets/maps/{self.map_nb}"
        with path.open() as current_map_file:
            i = offset_y / 64
            for line in current_map_file.readlines():
                j = 0
                for chr in line.split(","):
                    chr_idx = chr.replace("\n", "")

                    x = j * self._tile_size
                    y = i * self._tile_size

                    block = Block(x, y, chr_idx == self._block_idx)
                    self.blocks.append(block)
                    if chr_idx == self._player_idx:
                        self.player = Player(
                            block.rect.centerx - Player.W_PLAYER / 2,
                            block.rect.centery - Player.H_PLAYER / 2,
                        )
                    elif chr_idx == self._goal_idx:
                        self.goals.append(
                            Goal(
                                block.rect.centerx - Goal.W_GOAL / 2,
                                block.rect.centery - Goal.H_GOAL / 2,
                            )
                        )

                    j += 1
                i += 1

    def next_map(self, offset_y: int = None) -> None:
        self.map_nb += 1
        self.load_map(offset_y)

    def has_next(self) -> bool:
        path = Path(__file__).parent.parent.parent / f"assets/maps/{self.map_nb}"
        return os.path.isfile(path)

    def update(self, dt: int) -> None:
        self.player.update(dt)

        for block in self.blocks:
            block.update(self.player)

        for goal in self.goals:
            if not goal.reached:
                goal.update(self.player)

    def render(self, surface: Surface) -> None:
        for block in self.blocks:
            block.render(surface)

        self.player.render(surface)

        for goal in self.goals:
            goal.render(surface)

    def game_result(self) -> bool | None:
        lost = (
            self.player.steps > self.player.max_step
            and self.player.velocity.x == self.player.velocity.y == 0
        )
        reached_goals = [goal for goal in self.goals if goal.reached == True]
        won = len(reached_goals) == len(self.goals)
        if won:
            return True
        else:
            return False if lost else None
