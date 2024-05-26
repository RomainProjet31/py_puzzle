class LevelConfiguration:
    def __init__(self, max_steps: int) -> None:
        self.max_steps = max_steps


CONFIGURATIONS = [
    LevelConfiguration(1),
    LevelConfiguration(4),
    LevelConfiguration(2),
    LevelConfiguration(9),
]
