from item import Item
from player_component import PlayerComponent


class Diamond(Item):
    def __init__(self, player: PlayerComponent | None, tiles_path: dict[str, any], height: int,
                 widht: int, x: int, y: int, speed: float, value: int):
        self.value = value
        super().__init__(player, tiles_path, height, widht, x, y, speed)

    def get_reaction(self) -> dict:
        return {'Diamond': self.value}

    def get_diamonds(self) -> int:
        return self.player.get_diamonds() + self.value
