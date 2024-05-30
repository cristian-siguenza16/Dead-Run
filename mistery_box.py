from item import Item
import random
from player_component import PlayerComponent


class MisteryBox(Item):
    def __init__(self, player: PlayerComponent | None, tiles_path: dict[str, any], height: int,
                 widht: int, x: int, y: int, speed: float):
        super().__init__(player, tiles_path, height, widht, x, y, speed)

    def get_reaction(self) -> dict:
        num = random.randint(1, 100)
        speed_value = random.randint(1, 7) * 0.01
        if num <= 50:
            num = random.randint(1, 100)
            if num <= 50:
                return {'Speed_up': speed_value, 'Player': 0}
            else:
                return {'Speed_down': -speed_value, 'Player': 0}
        else:
            return {'Lightning': 1, 'Player': 0}
