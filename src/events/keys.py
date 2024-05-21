from typing import Any, Self


class KeyPressed:
    _instance: Self = None

    @staticmethod
    def instance() -> Self:
        if not KeyPressed._instance:
            KeyPressed._instance = KeyPressed()
        return KeyPressed._instance

    def __init__(self) -> None:
        self.key_pressed = None
