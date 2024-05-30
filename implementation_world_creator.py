import abc
import pygame
from player import Player

ASSET_HEIGHT = 500


class ImplementationWorldCreator(metaclass=abc.ABCMeta):

    @abc.abstractmethod
    def solid_background(self, file_name: list[str]):
        raise NotImplementedError

    @abc.abstractmethod
    def load_assets(self, names: list[str], quantity: int, a_height: int = ASSET_HEIGHT):
        raise NotImplementedError

    @abc.abstractmethod
    def setup_assets(self, y_offset: int):
        raise NotImplementedError

    @abc.abstractmethod
    def update(self, delta_time: int):
        raise NotImplementedError

    @abc.abstractmethod
    def render(self, dest):
        raise NotImplementedError

    @abc.abstractmethod
    def add_killable_platfrom(self, tiles_path: dict[str, str], height_platform: int, blocks: int, x: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_platform(self, tiles_path: dict[str, str], y: int, blocks: int, x: int,
                     height: int = 64, ud: bool = False):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movable_platform(self, tiles_path: dict[str, str], height_platform: int, blocks: int,
                             x: int, move_range: int, direction: int, height: int = 64, ud: bool = False):
        raise NotImplementedError

    @abc.abstractmethod
    def render_platform(self, screen):
        raise NotImplementedError

    @abc.abstractmethod
    def update_platform(self, delta_time: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_obstacle(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_portal_ud(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_movable_obstacle(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int,
                             move_range: int, move_direction: int, move_x: bool, move_y: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def render_obstacle(self, screen):
        raise NotImplementedError

    @abc.abstractmethod
    def update_obstacle(self, delta_time: int):
        raise NotImplementedError

    @abc.abstractmethod
    def load_background_assets(self, names: list[str]):
        raise NotImplementedError

    @abc.abstractmethod
    def setup_background_assets(self):
        raise NotImplementedError

    @abc.abstractmethod
    def update_background(self, delta_time: float):
        raise NotImplementedError

    @abc.abstractmethod
    def get_first_and_last_position(self):
        raise NotImplementedError

    @abc.abstractmethod
    def add_diamond(self, diamond_path: dict[str, any], height: int, widht: int, x: int, y: int,
                    diamond_value: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_heart(self, heart_path: dict[str, any], height: int, widht: int, x: int, y: int):
        raise NotImplementedError

    @abc.abstractmethod
    def add_misterybox(self, misterybox_path: dict[str, any], height: int, widht: int, x: int, y: int):
        raise NotImplementedError

    @abc.abstractmethod
    def render_item(self, screen):
        raise NotImplementedError

    @abc.abstractmethod
    def update_item(self, delta_time: int):
        raise NotImplementedError

    @abc.abstractmethod
    def get_platform_group(self) -> pygame.sprite.Group:
        raise NotImplementedError

    @abc.abstractmethod
    def get_obstacle_group(self) -> pygame.sprite.Group:
        raise NotImplementedError

    @abc.abstractmethod
    def get_portal_group(self) -> pygame.sprite.Group:
        raise NotImplementedError

    @abc.abstractmethod
    def get_items_group(self) -> pygame.sprite.Group:
        raise NotImplementedError

    @abc.abstractmethod
    def add_final_portal(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        raise NotImplementedError

    @abc.abstractmethod
    def final(self):
        raise NotImplementedError

    @abc.abstractmethod
    def set_final(self, final: bool):
        raise NotImplementedError

    @abc.abstractmethod
    def final_portal(self):
        raise NotImplementedError

    @abc.abstractmethod
    def killable_plaforms(self):
        raise NotImplementedError

    @abc.abstractmethod
    def speed(self):
        raise NotImplementedError

    # animaciones para el rayo
    @abc.abstractmethod
    def add_effect_animation(self, nplayer: int, player: Player, effect_type: int):
        raise NotImplementedError

    @abc.abstractmethod
    def render_effect(self, screen):
        raise NotImplementedError

    @abc.abstractmethod
    def render_effect_shield(self, screen, nplayer: int):
        raise NotImplementedError

    @abc.abstractmethod
    def update_effect(self, nplayer: int, shield: bool = False):
        raise NotImplementedError

    @abc.abstractmethod
    def get_winner_value(self):
        raise NotImplementedError
