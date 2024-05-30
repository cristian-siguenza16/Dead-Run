import pygame
from obstacle import Obstacle
from playground import Playground
from obstacle_builder import ObstacleBuilder
from platform_builder import PlatformBuilder
from playground_builder import PlaygroundBuilder
from diamond import Diamond
from heart import Heart
from mistery_box import MisteryBox
from implementation_world_creator import ImplementationWorldCreator
from effect_animation import EffectAnimation
from player import Player


# 576, 324
ASSET_WIDTH = 850
ASSET_HEIGHT = 500
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class WorldCreator(ImplementationWorldCreator):
    def __init__(self, name: str, path: str, speed: float, players: int):
        self.__name = name
        self.__path = path
        self.__speed = speed
        self.__platforms = pygame.sprite.Group()
        self.__obstacles = pygame.sprite.Group()
        self.__portales_ud: list[Obstacle] = []
        self.__final_portal: Obstacle | None = None
        self.__playground = Playground()
        self.__obstacle_builder = ObstacleBuilder()
        self.__platform_builder = PlatformBuilder()
        self.__playground_builder = PlaygroundBuilder()
        self.__final = False
        self.__killable_plaforms = pygame.sprite.Group()
        self.__item_group = pygame.sprite.Group()
        self.__animation_effect: EffectAnimation | None = None
        self.__animation_shield: list[EffectAnimation | None] = []
        for i in range(players):
            self.__animation_shield.append(None)
        self.__winer_value: int = 4

    def solid_background(self, file_name: list[str]):
        for i, file in enumerate(file_name):
            file_name[i] = self.__path + file
        self.__playground_builder.build_background(self.__speed, file_name)
        self.__playground = self.__playground_builder.get_result()

    def load_assets(self, names: list[str], quantity: int, a_height: int = ASSET_HEIGHT):
        for i, file in enumerate(names):
            names[i] = self.__path + file
        self.__playground.build_assets(names, quantity, a_height)

    def setup_assets(self, y_offset: int):
        for i, pos in enumerate(self.__playground.positions):
            pos.x = ASSET_WIDTH * i
            pos.y = SCREEN_HEIGHT - self.__playground.rects[i].height + y_offset
            self.__playground.rects[i].x = pos.x
            self.__playground.rects[i].y = pos.y

    def update(self, delta_time: int):
        last_one = False
        for i, vrect in enumerate(self.__playground.rects):
            self.__playground.positions[i].x -= self.__speed * delta_time
            vrect.x = int(self.__playground.positions[i].x)
            if vrect.x <= -500:
                last_one = True
            else:
                last_one = False

        if last_one:
            self.__final = True

    def render(self, dest):
        if self.__playground.add_background:
            for i, background_surf in enumerate(self.__playground.background_surf_list):
                dest.blit(background_surf, self.__playground.background_rect_list[i])
        if self.__playground.mov_backgrounds:
            for i, vsurface in enumerate(self.__playground.background_surfaces):
                if type(vsurface) == list:
                    for j in range(0, len(vsurface)):
                        dest.blit(vsurface[j], self.__playground.bsrufaces_rects[i])
                else:
                    dest.blit(vsurface, self.__playground.bsrufaces_rects[i])
        for i, vsurface in enumerate(self.__playground.surfaces):
            if type(vsurface) == list:
                for j in range(0, len(vsurface)):
                    dest.blit(vsurface[j], self.__playground.rects[i])
            else:
                dest.blit(vsurface, self.__playground.rects[i])

    def add_killable_platfrom(self, tiles_path: dict[str, str], height_platform: int, blocks: int, x: int):
        self.__platform_builder.reset()
        self.__platform_builder.build_image(height_platform, 0, self.__speed)
        self.__platform_builder.build_platform_blocks(blocks)
        self.__platform_builder.build_unique_image(tiles_path['unique'])
        self.__platform_builder.build_position(x, height_platform, 64, True)
        self.__killable_plaforms.add(self.__platform_builder.get_result())

    def add_platform(self, tiles_path: dict[str, str], y: int, blocks: int, x: int,
                     height: int = 64, ud: bool = False):
        self.__platform_builder.reset()
        self.__platform_builder.build_image(y, 0, self.__speed)
        self.__platform_builder.build_platform_blocks(blocks)
        names = []
        if 'unique' in tiles_path:
            self.__platform_builder.build_unique_image(tiles_path['unique'], ud)
        else:
            for key in tiles_path.keys():
                names.append(tiles_path[key])

            if len(names) == 3:
                self.__platform_builder.build_floating_platform(names, ud)
            elif len(names) == 6:
                self.__platform_builder.build_wall_platform(names)

        self.__platform_builder.build_position(x, y, height)
        self.__platforms.add(self.__platform_builder.get_result())

    def add_movable_platform(self, tiles_path: dict[str, str], height_platform: int, blocks: int,
                             x: int, move_range: int, direction: int, height: int = 64, ud: bool = False):
        self.__platform_builder.reset()
        self.__platform_builder.build_image(height_platform, 0, self.__speed)
        self.__platform_builder.build_platform_blocks(blocks)
        names = []
        if 'unique' in tiles_path:
            self.__platform_builder.build_unique_image(tiles_path['unique'], ud)
        else:
            for key in tiles_path.keys():
                names.append(tiles_path[key])

            if len(names) == 3:
                self.__platform_builder.build_floating_platform(names, ud)
            elif len(names) == 6:
                self.__platform_builder.build_wall_platform(names)

        self.__platform_builder.build_movable_x(move_range, direction)
        self.__platform_builder.build_position(x, height_platform, height)
        self.__platforms.add(self.__platform_builder.get_result())

    def render_platform(self, screen):
        for platform in self.__platforms:
            screen.blit(platform.surf, platform.rect)
            # pygame.draw.rect(screen, (255, 255, 255), platform.rect, 2)
        for killable_p in self.__killable_plaforms:
            screen.blit(killable_p.surf, killable_p.rect)

    def update_platform(self, delta_time: int):
        for platform in self.__platforms:
            platform.update(delta_time)
        for killable_p in self.__killable_plaforms:
            killable_p.update(delta_time)

    def add_obstacle(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        self.__obstacle_builder.reset()
        self.__obstacle_builder.build_image(height, widht, self.__speed)
        self.__obstacle_builder.build_unique_image(obstacle_path['unique'])
        self.__obstacle_builder.build_position(x, y)
        self.__obstacles.add(self.__obstacle_builder.get_result())

    def add_portal_ud(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        self.__obstacle_builder.reset()
        self.__obstacle_builder.build_image(height, widht, self.__speed)
        self.__obstacle_builder.build_unique_image(obstacle_path['unique'])
        self.__obstacle_builder.build_position(x, y)
        self.__portales_ud.append(self.__obstacle_builder.get_result())
        if 'next_portal' in obstacle_path:
            self.__portales_ud[len(self.__portales_ud) - 1].next = {"next_portal": obstacle_path['next_portal']}

    def add_movable_obstacle(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int,
                             move_range: int, move_direction: int, move_x: bool, move_y: bool):
        self.__obstacle_builder.reset()
        self.__obstacle_builder.build_image(height, widht, self.__speed)

        if 'unique' in obstacle_path:
            self.__obstacle_builder.build_unique_image(obstacle_path['unique'])
        else:
            self.__obstacle_builder.build_animation_image(obstacle_path['animations'])

        if move_x:
            self.__obstacle_builder.build_movable_x(move_range, move_direction)
        if move_y:
            self.__obstacle_builder.build_movable_y(move_range, move_direction)

        self.__obstacle_builder.build_position(x, y)
        self.__obstacles.add(self.__obstacle_builder.get_result())

    def render_obstacle(self, screen):
        screen.blit(self.__final_portal.image, self.__final_portal.rect)
        for obstacle in self.__obstacles:
            screen.blit(obstacle.image, obstacle.rect)
        for portal in self.__portales_ud:
            screen.blit(portal.image, portal.rect)

    def update_obstacle(self, delta_time: int):
        self.__final_portal.update(delta_time)
        for obstacle in self.__obstacles:
            obstacle.update(delta_time)
        for portal in self.__portales_ud:
            portal.update(delta_time)

    def load_background_assets(self, names: list[str]):
        for i, file in enumerate(names):
            names[i] = self.__path + file
        self.__playground.build_background_assets(names)

    def setup_background_assets(self):
        self.__playground.mov_backgrounds = True
        for i, pos in enumerate(self.__playground.back_positions):
            pos.x = SCREEN_WIDTH * i
            pos.y = SCREEN_HEIGHT - self.__playground.bsrufaces_rects[i].height + 0
            self.__playground.bsrufaces_rects[i].x = pos.x
            self.__playground.bsrufaces_rects[i].y = pos.y

    def update_background(self, delta_time: float):
        self.__playground.update_background(delta_time)

    def get_first_and_last_position(self):
        return self.__playground.get_first_and_last_position()

    def add_diamond(self, diamond_path: dict[str, any], height: int, widht: int, x: int, y: int,
                    diamond_value: int):
        if 'animations' in diamond_path:
            diamond_path['animation'] = True
            diamond_path['move_x'] = True
            diamond_path['move_y'] = False
        self.__item_group.add(Diamond(None, diamond_path, height, widht, x, y, self.__speed, diamond_value))

    def add_heart(self, heart_path: dict[str, any], height: int, widht: int, x: int, y: int):
        heart_path['animation'] = True
        heart_path['move_x'] = True
        heart_path['move_y'] = False
        self.__item_group.add(Heart(None, heart_path, height, widht, x, y, self.__speed))

    def add_misterybox(self, misterybox_path: dict[str, any], height: int, widht: int, x: int, y: int):
        self.__item_group.add(MisteryBox(None, misterybox_path, height, widht, x, y, self.__speed))

    def render_item(self, screen):
        self.__item_group.draw(screen)

    def update_item(self, delta_time: int):
        for item in self.__item_group:
            item.update(delta_time)

    def get_platform_group(self) -> pygame.sprite.Group:
        return self.__platforms

    def get_obstacle_group(self) -> pygame.sprite.Group:
        return self.__obstacles

    def get_portal_group(self) -> pygame.sprite.Group:
        group_portal = pygame.sprite.Group()
        for portal in self.__portales_ud:
            group_portal.add(portal)
        return group_portal

    def get_items_group(self) -> pygame.sprite.Group:
        return self.__item_group

    def add_final_portal(self, obstacle_path: dict[str, any], height: int, widht: int, x: int, y: int):
        self.__obstacle_builder.reset()
        self.__obstacle_builder.build_image(height, widht, self.__speed)
        self.__obstacle_builder.build_unique_image(obstacle_path['unique'])
        self.__obstacle_builder.build_position(x, y)
        self.__final_portal = self.__obstacle_builder.get_result()

    def add_effect_animation(self, nplayer: int, player: Player, effect_type: int):
        if effect_type < 4:
            self.__animation_effect = EffectAnimation(self.__speed, player, effect_type)
        else:
            self.__animation_shield[nplayer] = EffectAnimation(self.__speed, player, effect_type)

    def render_effect(self, screen):
        screen.blit(self.__animation_effect.image, self.__animation_effect.rect)

    def render_effect_shield(self, screen, nplayer: int):
        screen.blit(self.__animation_shield[nplayer].image, self.__animation_shield[nplayer].rect)

    def update_effect(self, nplayer: int, shield: bool = False):
        if shield:
            self.__animation_shield[nplayer].update()
        else:
            self.__animation_effect.update()

    @property
    def final(self):
        return self.__final

    def set_final(self, final: bool):
        self.__final = final

    @property
    def final_portal(self):
        return self.__final_portal

    @property
    def killable_plaforms(self):
        return self.__killable_plaforms

    @property
    def speed(self):
        return self.__speed

    @property
    def get_winner_value(self):
        temp = self.__winer_value
        self.__winer_value -= 1
        return temp
