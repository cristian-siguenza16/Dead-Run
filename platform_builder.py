import pygame

from builder import Builder
from platform import Platform

tile_width = 64
tile_height = 64
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class PlatformBuilder(Builder):
    def __init__(self):
        self.__platform = Platform()

    def build_image(self, height: int, width: int, speed: float):
        self.__platform.width = width
        self.__platform.height = height
        self.__platform.speed = speed

    def build_position(self, x: int, y: int, vheight: int = tile_height, killable: bool = False):
        self.__platform.pos = pygame.math.Vector2(x, SCREEN_HEIGHT - y)
        self.__platform.killable = killable
        if vheight != tile_height:
            self.__platform.rect = self.__platform.surf.get_rect(topleft=(x, self.__platform.pos.y), height=vheight)
        else:
            self.__platform.rect = self.__platform.surf.get_rect(topleft=(x, self.__platform.pos.y))
        self.__platform.surf = self.__platform.surf.convert_alpha()

    def build_unique_image(self, name: str, ud: bool = False):
        platform_image_surf_unique = pygame.image.load(name).convert_alpha()
        if ud:
            self.__platform.surf = pygame.Surface((self.__platform.width, tile_height/2), pygame.SRCALPHA)
            platform_image_surf_unique = pygame.transform.scale(platform_image_surf_unique, (tile_width, tile_height/2))
        else:
            self.__platform.surf = pygame.Surface((self.__platform.width, tile_height), pygame.SRCALPHA)
            platform_image_surf_unique = pygame.transform.scale(platform_image_surf_unique, (tile_width, tile_height))
        if self.__platform.tile_number == 1:
            # Si solo es uno, poner la version 'unique'
            self.__platform.surf.blit(platform_image_surf_unique, (0, 0))

    def build_floating_platform(self, name: list[str], ud: bool = False):
        platform_image_surf_beginning = pygame.image.load(name[0]).convert_alpha()
        platform_image_surf_middle = pygame.image.load(name[1]).convert_alpha()
        platform_image_surf_end = pygame.image.load(name[2]).convert_alpha()
        if ud:
            self.__platform.surf = pygame.Surface((self.__platform.width, tile_height/2), pygame.SRCALPHA)
            platform_image_surf_beginning = pygame.transform.scale(platform_image_surf_beginning,
                                                                   (tile_width, tile_height/2))
            platform_image_surf_middle = pygame.transform.scale(platform_image_surf_middle,
                                                                (tile_width, tile_height/2))
            platform_image_surf_end = pygame.transform.scale(platform_image_surf_end,
                                                             (tile_width, tile_height/2))
        else:
            self.__platform.surf = pygame.Surface((self.__platform.width, tile_height), pygame.SRCALPHA)
            platform_image_surf_beginning = pygame.transform.scale(platform_image_surf_beginning,
                                                                   (tile_width, tile_height))
            platform_image_surf_middle = pygame.transform.scale(platform_image_surf_middle,
                                                                (tile_width, tile_height))
            platform_image_surf_end = pygame.transform.scale(platform_image_surf_end,
                                                             (tile_width, tile_height))
        # No es solo uno, ir a la logica divertida
        tile_x = 0
        idx = 0
        while True:
            if idx == 0:
                # El primero siempre es _beginning
                self.__platform.surf.blit(platform_image_surf_beginning, (tile_x, 0))
            elif tile_x + tile_width >= self.__platform.width:
                # El ultimo siempre es _end
                self.__platform.surf.blit(platform_image_surf_end, (tile_x, 0))
            else:
                # Los de enmedio siempre seran 'middle'
                self.__platform.surf.blit(platform_image_surf_middle, (tile_x, 0))

            tile_x += tile_width
            if tile_x > self.__platform.width:
                break
            idx += 1

    def build_wall_platform(self, name: list[str]):
        self.__platform.surf = pygame.Surface((self.__platform.width, tile_height), pygame.SRCALPHA)
        platform_image_surf_beginning = pygame.image.load(name[0]).convert_alpha()
        platform_image_surf_middle = pygame.image.load(name[1]).convert_alpha()
        platform_image_surf_end = pygame.image.load(name[2]).convert_alpha()

        platform_image_surf_beginning = pygame.transform.scale(platform_image_surf_beginning,
                                                               (tile_width, tile_height))
        platform_image_surf_middle = pygame.transform.scale(platform_image_surf_middle,
                                                            (tile_width, tile_height))
        platform_image_surf_end = pygame.transform.scale(platform_image_surf_end,
                                                         (tile_width, tile_height))

    # Tiene continuidad hacia abajo? (es decir, no es flotante)
        self.__platform.surf = pygame.Surface((self.__platform.width, self.__platform.height), pygame.SRCALPHA)
        platform_image_surf_beginning_bottom = pygame.image.load(name[3]).convert_alpha()
        platform_image_surf_middle_bottom = pygame.image.load(name[4]).convert_alpha()
        platform_image_surf_end_bottom = pygame.image.load(name[5]).convert_alpha()

        platform_image_surf_beginning_bottom = pygame.transform.scale(platform_image_surf_beginning_bottom,
                                                                      (tile_width, tile_height))
        platform_image_surf_middle_bottom = pygame.transform.scale(platform_image_surf_middle_bottom,
                                                                   (tile_width, tile_height))
        platform_image_surf_end_bottom = pygame.transform.scale(platform_image_surf_end_bottom,
                                                                (tile_width, tile_height))

        # No es solo uno, ir a la logica divertida
        tile_x = 0
        idx = 0
        while True:
            if idx == 0:
                # El primero siempre es _beginning
                self.__platform.surf.blit(platform_image_surf_beginning, (tile_x, 0))
            elif tile_x + tile_width >= self.__platform.width:
                # El ultimo siempre es _end
                self.__platform.surf.blit(platform_image_surf_end, (tile_x, 0))
            else:
                # Los de enmedio siempre seran 'middle'
                self.__platform.surf.blit(platform_image_surf_middle, (tile_x, 0))

            if self.__platform.height > tile_height:
                # Si hay continuidad hacia abajo, misma logica para pintar los de
                # abajo y que no 'flote' la plataforma
                current_y = tile_height
                while current_y < self.__platform.height:
                    if idx == 0:
                        self.__platform.surf.blit(platform_image_surf_beginning_bottom, (tile_x, current_y))
                    elif tile_x + tile_width >= self.__platform.width:
                        self.__platform.surf.blit(platform_image_surf_end_bottom, (tile_x, current_y))
                    else:
                        self.__platform.surf.blit(platform_image_surf_middle_bottom, (tile_x, current_y))
                    current_y += tile_height

            tile_x += tile_width
            if tile_x > self.__platform.width:
                break
            idx += 1

    def build_platform_blocks(self, blocks: int):
        self.__platform.tile_number = blocks
        self.__platform.width = self.__platform.tile_number * tile_width

    def build_movable_x(self, move_range: int, move_direction: int):
        self.__platform.move = True
        self.__platform.move_range = move_range
        self.__platform.move_direction = move_direction

    def get_result(self) -> Platform:
        return self.__platform

    def reset(self):
        self.__platform = Platform()
