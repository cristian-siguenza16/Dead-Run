import pygame

from builder import Builder
from obstacle import Obstacle

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class ObstacleBuilder(Builder):
    def __init__(self):
        self.__obstacle = Obstacle()

    def build_image(self, height: int, width: int, speed: float):
        self.__obstacle.height = height
        self.__obstacle.widht = width
        self.__obstacle.speed = speed

    def build_animation_image(self, name: list[str]):
        self.__obstacle.animation = True
        self.__obstacle.animation_list = []
        self.__obstacle.index = 0
        self.__obstacle.move_counter = 0
        for path in name:
            self.__obstacle.image = pygame.image.load(path).convert_alpha()
            self.__obstacle.image = pygame.transform.scale(self.__obstacle.image,
                                                           (self.__obstacle.widht, self.__obstacle.height))
            self.__obstacle.animation_list.append(self.__obstacle.image)
        self.__obstacle.image = self.__obstacle.animation_list[self.__obstacle.index]
        self.__obstacle.mask = pygame.mask.from_surface(self.__obstacle.image)

    def build_position(self, x: int, y: int):
        self.__obstacle.pos = pygame.math.Vector2(x, SCREEN_HEIGHT - y)
        self.__obstacle.rect = self.__obstacle.image.get_rect(topleft=(x, self.__obstacle.pos.y))

    def build_unique_image(self, name: str):
        self.__obstacle.animation = False
        self.__obstacle.image = pygame.image.load(name).convert_alpha()
        self.__obstacle.image = pygame.transform.scale(self.__obstacle.image,
                                                       (self.__obstacle.widht, self.__obstacle.height))
        self.__obstacle.mask = pygame.mask.from_surface(self.__obstacle.image)

    def build_movable_x(self, move_range: int, move_direction: int):
        self.__obstacle.move_range = move_range
        self.__obstacle.move_direction = move_direction
        self.__obstacle.move_x = True

    def build_movable_y(self, move_range: int, move_direction: int):
        self.__obstacle.move_range = move_range
        self.__obstacle.move_direction = move_direction
        self.__obstacle.move_y = True

    def get_result(self) -> Obstacle:
        return self.__obstacle

    def reset(self):
        self.__obstacle = Obstacle()
