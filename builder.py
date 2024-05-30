from abc import ABCMeta

from playground import Playground


class Builder(metaclass=ABCMeta):
    def build_image(self, height: int, width: int, speed: float):
        raise NotImplementedError

    def build_animation_image(self, name: list[str]):
        raise NotImplementedError

    def build_position(self, x: int, y: int):
        raise NotImplementedError

    def build_unique_image(self, name: str):
        raise NotImplementedError

    def build_floating_platform(self, name: list[str]):
        raise NotImplementedError

    def build_wall_platform(self, name: list[str]):
        raise NotImplementedError

    def build_platform_blocks(self, blocks: int):
        raise NotImplementedError

    def build_movable_x(self, move_range: int, move_direction: int):
        raise NotImplementedError

    def build_movable_y(self, move_range: int, move_direction: int):
        raise NotImplementedError

    def build_assets(self, names: list[str], quantity: int, height: int, playground: Playground):
        raise NotImplementedError

    def build_setup_assets(self, y_offset: int, playground: Playground):
        raise NotImplementedError

    def build_background_assets(self, names: list[str], playground: Playground):
        raise NotImplementedError

    def build_setup_background_assets(self, playground: Playground):
        raise NotImplementedError

    def build_background(self, speed: float, file_names: list[str]):
        raise NotImplementedError

    def reset(self):
        raise NotImplementedError
