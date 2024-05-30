import pygame

from builder import Builder
from playground import Playground

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class PlaygroundBuilder(Builder):
    def __init__(self):
        self.__playground = Playground()

    def build_background(self, speed: float, file_names: list[str]):
        self.__playground.add_background = True
        self.__playground.speed = speed
        for file in file_names:
            background_surf = pygame.image.load(file).convert_alpha()
            background_surf = pygame.transform.scale(background_surf,
                                                     (SCREEN_WIDTH, SCREEN_HEIGHT))
            self.__playground.background_surf_list.append(background_surf)
            background_rect = background_surf.get_rect()
            background_rect.y = SCREEN_HEIGHT - background_rect.height
            self.__playground.background_rect_list.append(background_rect)

    def get_result(self) -> Playground:
        return self.__playground
