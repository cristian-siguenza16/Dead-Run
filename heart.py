from item import Item
from player_component import PlayerComponent


class Heart(Item):
    def __init__(self, player: PlayerComponent | None, tiles_path: dict[str, any], height: int,
                 widht: int, x: int, y: int, speed: float):
        super().__init__(player, tiles_path, height, widht, x, y, speed)

    def get_reaction(self) -> dict:
        return {'Heart': 1}

    def get_lives(self) -> int:
        if self.player.get_lives() < 3:
            return self.player.get_lives() + 1
        else:
            return self.player.get_lives()
