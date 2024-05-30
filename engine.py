import world_creator
from world_creator import WorldCreator
import pygame
import sys
from button import Button
from character import Character
from player import Player
from implementation_world_creator import ImplementationWorldCreator


class Engine:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Dead Run")
        pygame.mixer.music.load("resources\\music\\hurry_up_and_run.wav")
        self.screen = pygame.display.set_mode([world_creator.SCREEN_WIDTH + 200, world_creator.SCREEN_HEIGHT])
        self.clock = pygame.time.Clock()
        # DECLARACION DE LO QUE NECESITA EL MUNDO.
        # Direccion de items
        self.path_item = "resources\\items\\"
        self.path_letter = "resources\\assets\\font.ttf"
        self.world: ImplementationWorldCreator | None = None
        # heart animations
        self.heart_animations = \
            {'animations': [self.path_item + 'heart_1.png', self.path_item + 'heart_2.png',
                            self.path_item + 'heart_3.png',
                            self.path_item + 'heart_4.png', self.path_item + 'heart_5.png',
                            self.path_item + 'heart_6.png',
                            self.path_item + 'heart_7.png', self.path_item + 'heart_8.png',
                            self.path_item + 'heart_9.png',
                            self.path_item + 'heart_10.png']}
        # diamond animations
        self.diamond1_animations = {
            'animations': [self.path_item + 'diamond_1.png', self.path_item + 'diamond_2.png',
                           self.path_item + 'diamond_3.png',
                           self.path_item + 'diamond_4.png', self.path_item + 'diamond_5.png',
                           self.path_item + 'diamond_6.png',
                           self.path_item + 'diamond_7.png', self.path_item + 'diamond_8.png',
                           self.path_item + 'diamond_9.png',
                           self.path_item + 'diamond_10.png']}
        self.diamond2_animations = {
            'animations': [self.path_item + 'diamond2_1.png', self.path_item + 'diamond2_2.png',
                           self.path_item + 'diamond2_3.png',
                           self.path_item + 'diamond2_4.png', self.path_item + 'diamond2_5.png',
                           self.path_item + 'diamond2_6.png',
                           self.path_item + 'diamond2_7.png', self.path_item + 'diamond2_8.png',
                           self.path_item + 'diamond2_9.png',
                           self.path_item + 'diamond2_10.png']}
        self.diamond3_animations = {
            'animations': [self.path_item + 'diamond3_1.png', self.path_item + 'diamond3_2.png',
                           self.path_item + 'diamond3_3.png',
                           self.path_item + 'diamond3_4.png', self.path_item + 'diamond3_5.png',
                           self.path_item + 'diamond3_6.png',
                           self.path_item + 'diamond3_7.png', self.path_item + 'diamond3_8.png',
                           self.path_item + 'diamond3_9.png',
                           self.path_item + 'diamond3_10.png']}

        # CARACTERES
        self.player_objects = {'character': [], 'controls': []}
        self.player_objects['character'].append(Character(0.5, -0.12, 1.50, -15, 'Reaper_Man_1'))
        self.player_objects['character'].append(Character(0.65, -0.11, 1.50, -12.5, 'Reaper_Man_2'))
        self.player_objects['character'].append(Character(0.55, -0.12, 1.85, -13, 'Reaper_Man_3'))
        self.player_objects['character'].append(Character(0.5, -0.11, 1.75, -14, 'Reaper_Man_4'))
        self.player_objects['controls'].append(
            {'jump': pygame.K_UP, 'right': pygame.K_RIGHT, 'left': pygame.K_LEFT, 'down': pygame.K_DOWN})
        self.player_objects['controls'].append(
            {'jump': pygame.K_w, 'right': pygame.K_d, 'left': pygame.K_a, 'down': pygame.K_s})
        self.player_objects['controls'].append(
            {'jump': pygame.K_i, 'right': pygame.K_l, 'left': pygame.K_j, 'down': pygame.K_k})
        self.player_objects['controls'].append(
            {'jump': pygame.K_KP8, 'right': pygame.K_KP6, 'left': pygame.K_KP4, 'down': pygame.K_KP5})

        # PLAYERS
        self.actual_players = 1
        self.p1 = Player(self.player_objects['character'][0], 'Player 1',
                         self.player_objects['controls'][0])
        self.p2 = None
        self.p3 = None
        self.p4 = None

        self.possible_attacks = {"possible_attacks_p1": [self.p1],
                                 "possible_attacks_p2": None,
                                 "possible_attacks_p3": None,
                                 "possible_attacks_p4": None}

        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.p1.character)

        self.players_list = []
        self.players_list.append(self.p1)

        # parte de la pantalla
        self.background_image = pygame.image.load("resources\\assets\\background_main.png").convert_alpha()
        self.background_image = pygame.transform.scale(self.background_image, (1200, 700))
        self.background_winers_image = pygame.image.load("resources\\assets\\Background.png").convert_alpha()
        self.background_winers_image = pygame.transform.scale(self.background_winers_image, (1200, 700))
        self.bg_info = pygame.image.load("resources\\assets\\background_info.png").convert_alpha()
        self.life_img = pygame.image.load("resources\\assets\\life.png").convert_alpha()
        self.life_img = pygame.transform.scale(self.life_img, (40, 40))
        self.diamond_img = pygame.image.load("resources\\assets\\diamond.png").convert_alpha()
        self.diamond_img = pygame.transform.scale(self.diamond_img, (40, 40))
        self.dead_img = pygame.image.load("resources\\assets\\dead.png").convert_alpha()
        self.dead_img = pygame.transform.scale(self.dead_img, (50, 50))
        self.pause_rect = pygame.image.load("resources\\assets\\pause_rect.png").convert_alpha()
        self.pause_rect = pygame.transform.scale(self.pause_rect, (700, 450))
        self.one_player_img = pygame.image.load("resources\\assets\\player1.png").convert_alpha()
        self.one_player_img = pygame.transform.scale(self.one_player_img, (270, 570))
        self.twp_player_img = pygame.image.load("resources\\assets\\player2.png").convert_alpha()
        self.twp_player_img = pygame.transform.scale(self.twp_player_img, (270, 570))
        self.tree_player_img = pygame.image.load("resources\\assets\\player3.png").convert_alpha()
        self.tree_player_img = pygame.transform.scale(self.tree_player_img, (270, 570))
        self.four_player_img = pygame.image.load("resources\\assets\\player4.png").convert_alpha()
        self.four_player_img = pygame.transform.scale(self.four_player_img, (270, 570))
        # Fuente
        self.font_23 = pygame.font.Font(self.path_letter, 23)

    def __get_font(self, size):  # Returns Press-Start-2P in the desired size
        return pygame.font.Font(self.path_letter, size)

    def __assets_world1(self):
        # Backgrounds
        self.world.load_assets(["grass&road.png"], 1)
        self.world.load_assets(["grasses.png", "grass&road.png"], 6)
        self.world.load_assets(["grasses.png", "grass&road.png", "4.png"], 2)
        self.world.load_assets(["grasses.png", "grass&road.png"], 6)
        self.world.load_assets(["grasses.png", "grass&road.png", "4.png"], 1)
        self.world.setup_assets(60)

    def __platforms_world1(self):
        platform_path = "resources\\worlds\\darkForest\\Tiles\\"
        # Diccionarios para las plataformas
        tiles = {'beginning': platform_path + 'Tile_01.png', 'middle': platform_path + 'Tile_02.png',
                 'end': platform_path + 'Tile_03.png'}
        tiles2 = {'beginning': platform_path + 'Tile_01.png', 'middle': platform_path + 'Tile_02.png',
                  'end': platform_path + 'Tile_03.png',
                  'beginning_bottom': platform_path + 'Tile_11.png', 'middle_bottom': platform_path + 'Tile_12.png',
                  'end_bottom': platform_path + 'Tile_13.png'}
        tiles_floor = {'beginning': platform_path + 'Tile_25.png', 'middle': platform_path + 'Tile_25.png',
                       'end': platform_path + 'Tile_25.png',
                       'beginning_bottom': platform_path + 'Tile_12.png',
                       'middle_bottom': platform_path + 'Tile_12.png',
                       'end_bottom': platform_path + 'Tile_12.png'}
        # Añadir plataformas
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 300, 1, 1400, 32)
        self.world.add_platform(tiles, 450, 5, 1500)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 240, 1, 3000, 32)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 270, 1, 4700, 32)
        self.world.add_platform(tiles, 350, 4, 5000)
        self.world.add_platform(tiles, 450, 3, 5400)
        self.world.add_platform(tiles, 500, 2, 5750)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 550, 1, 6100, 32)

        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 300, 1, 6250, 32)

        self.world.add_platform(tiles2, 460, 5, 6400)
        # world1.add_platform({'unique': path2 + 'Tile_39.png'}, 400, 1, 6500)
        # world1.add_platform(tiles, 300, 3, 12000)

        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 250, 1, 8000, 32)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 300, 1, 8200, 32)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 400, 1, 8400, 32)
        self.world.add_platform(tiles, 450, 10, 8600)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 350, 1, 9500, 32)
        self.world.add_platform({'unique': platform_path + 'Tile_39.png'}, 350, 1, 9700, 32)

        self.world.add_platform({'unique': platform_path + 'Tile_01.png'}, 320, 1, 12000)
        self.world.add_platform({'unique': platform_path + 'Tile_01.png'}, 370, 1, 12300)

        # Piso
        self.world.add_platform(tiles_floor, 120, 96, 0)
        self.world.add_platform(tiles_floor, 120, 92, 6912)
        self.world.add_platform(tiles_floor, 120, 9, 13056)

    def __obstacles_world1(self):
        obstacle_path = "resources\\worlds\\darkForest\\Objects\\"
        self.world.add_obstacle({'unique': obstacle_path + '2.png'}, 60, 100, 1620, 170)
        self.world.add_obstacle({'unique': obstacle_path + '1.png'}, 100, 150, 3770, 210)
        self.world.add_obstacle({'unique': obstacle_path + '6.png'}, 200, 150, 9000, 310)
        self.world.add_obstacle({'unique': obstacle_path + '4.png'}, 100, 150, 10500, 210)

        self.world.add_obstacle({'unique': obstacle_path + '3.png'}, 50, 60, 3000, 290)
        # self.world.add_obstacle({'unique': obstacle_path + '8.png'}, 100, 150, 12000, 400)

        self.world.add_final_portal({'unique': obstacle_path + 'part03.png'}, 350, 350, 13300, 430)
        # world1.add_platform({'unique': path2 + 'Tile_39.png'}, 300, 1, 5250)

    def __items_world1(self):
        # Añadir Items
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 1630, 600)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 3000, 200, 3)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 3930, 180, 1)
        self.world.add_heart(self.heart_animations, 60, 50, 5100, 500)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 5750, 300)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 6550, 600, 5)
        self.world.add_heart(self.heart_animations, 60, 50, 8000, 300)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 8700, 600)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 9200, 500, 1)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 9750, 500, 5)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 12150, 500)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 13000, 250, 3)

    def __assets_world2(self):
        # Backgrounds
        self.world.load_assets(["floor.png"], 2)
        # ponerlo en el segundo para contrastar fondo
        self.world.load_assets(["lava.png"], 3)
        self.world.load_assets(["back.png"], 4)
        self.world.load_assets(["floor.png"], 2)
        self.world.load_assets(["back.png"], 2)
        self.world.load_assets(["lava.png"], 2)
        self.world.setup_assets(0)

    def __platforms_world2(self):
        # Direccion de plataformas
        platform_path = "resources\\worlds\\LandOfDeadlyLaughs\\Tiles\\"
        # tiles plataformas
        tiles4 = {'beginning': platform_path + 'tile20.png', 'middle': platform_path + 'tile20.png',
                  'end': platform_path + 'tile20.png'}
        tiles5 = {'beginning': platform_path + 'tile21.png', 'middle': platform_path + 'tile21.png',
                  'end': platform_path + 'tile21.png'}
        # tiles 2 (muros, pisos)
        tiles_floor = {'beginning': platform_path + 'Ground_02.png', 'middle': platform_path + 'Ground_02.png',
                       'end': platform_path + 'Ground_02.png',
                       'beginning_bottom': platform_path + 'Ground_06.png',
                       'middle_bottom': platform_path + 'Ground_06.png',
                       'end_bottom': platform_path + 'Ground_06.png'}
        tiles_ground = {'beginning': platform_path + 'Ground_06.png', 'middle': platform_path + 'Ground_06.png',
                        'end': platform_path + 'Ground_06.png',
                        'beginning_bottom': platform_path + 'Ground_06.png',
                        'middle_bottom': platform_path + 'Ground_06.png',
                        'end_bottom': platform_path + 'Ground_06.png'}
        # agregacion de plataformas, piso
        # PISOOOOOOOOOOOOOOOO
        self.world.add_platform(tiles_floor, 70, 27, 0)
        # Añadir plataformas
        # (y, cantida bloques, x)
        self.world.add_platform(tiles4, 260, 2, 1000, 32)
        self.world.add_platform(tiles4, 410, 3, 1256, 32)
        self.world.add_platform(tiles5, 210, 2, 1700, 32)
        # Segunda parte del contraste
        self.world.add_platform(tiles5, 310, 2, 2000, 32)
        self.world.add_platform(tiles5, 410, 2, 2300, 32)
        self.world.add_platform(tiles5, 510, 3, 2600, 32)
        self.world.add_platform(tiles5, 410, 2, 2900, 32)
        self.world.add_platform(tiles5, 260, 2, 2650, 32)
        self.world.add_platform(tiles5, 310, 3, 3100, 32)
        self.world.add_platform(tiles5, 210, 4, 3400, 32)
        self.world.add_platform(tiles5, 310, 2, 3740, 32)
        self.world.add_platform(tiles5, 410, 2, 3968, 32)
        self.world.add_platform(tiles5, 310, 3, 4196, 32)
        # PISOOOOOO
        self.world.add_platform(tiles_ground, 70, 54, 4250)
        # cuarta parte del mundo
        self.world.add_platform(tiles4, 210, 2, 5300, 32)
        self.world.add_platform(tiles4, 310, 3, 5600, 32)
        self.world.add_platform(tiles5, 210, 3, 6200, 32)
        self.world.add_platform(tiles5, 310, 3, 6500, 32)
        self.world.add_platform(tiles5, 410, 3, 6800, 32)
        self.world.add_platform(tiles5, 210, 2, 6700, 32)
        self.world.add_platform(tiles_floor, 70, 27, 7652)
        self.world.add_platform(tiles4, 210, 2, 8500, 32)
        self.world.add_platform(tiles5, 310, 2, 8700, 32)
        self.world.add_platform(tiles4, 410, 2, 8900, 32)
        self.world.add_platform(tiles4, 510, 5, 9100, 32)
        self.world.add_platform(tiles4, 210, 2, 9700, 32)
        self.world.add_platform(tiles4, 190, 4, 10500, 32)
        # PISOOOOOO
        self.world.add_platform(tiles_ground, 70, 26, 9380)
        # ultimo piso
        self.world.add_platform(tiles5, 210, 2, 11200, 32)
        self.world.add_platform(tiles5, 310, 2, 11400, 32)
        self.world.add_platform(tiles5, 210, 3, 11600, 32)
        self.world.add_platform(tiles5, 310, 2, 11800, 32)
        self.world.add_platform(tiles5, 410, 2, 12000, 32)
        self.world.add_platform(tiles5, 310, 2, 12300, 32)
        self.world.add_platform(tiles5, 510, 2, 12200, 32)
        self.world.add_platform(tiles5, 110, 4, 12500, 32)

    def __obstacles_world2(self):
        # Direccion de obstaculos
        obstacle_path = "resources\\worlds\\LandOfDeadlyLaughs\\Objects\\"
        # Primera parte del contraste
        self.world.add_obstacle({'unique': obstacle_path + 'crystal_lime2.png'}, 100, 180, 700, 170)
        self.world.add_obstacle({'unique': obstacle_path + 'chest.png'}, 50, 50, 1365, 450)
        self.world.add_obstacle({'unique': obstacle_path + 'marker_statue4.png'}, 100, 70, 1330, 170)
        self.world.add_obstacle({'unique': obstacle_path + 'lava_drop1_3.png'}, 50, 50, 2070, 310)
        self.world.add_obstacle({'unique': obstacle_path + 'stalagmite4.png'}, 100, 90, 2650, 600)
        self.world.add_obstacle({'unique': obstacle_path + 'lava_drop1_6.png'}, 50, 50, 3180, 350)
        # tercera parte del contraste
        self.world.add_obstacle({'unique': obstacle_path + 'lava_drop1_7.png'}, 40, 40, 4200, 350)
        self.world.add_obstacle({'unique': obstacle_path + 'marker_statue1.png'}, 100, 70, 4520, 150)
        self.world.add_obstacle({'unique': obstacle_path + 'lava_tile9.png'}, 60, 60, 4525, 180)
        self.world.add_obstacle({'unique': obstacle_path + 'cave_rock3.png'}, 120, 120, 5000, 190)
        self.world.add_obstacle({'unique': obstacle_path + 'stalagmite4.png'}, 100, 90, 5900, 170)
        self.world.add_obstacle({'unique': obstacle_path + 'canyon_rock1.png'}, 250, 250, 7000, 320)
        # PISOOOOOO
        self.world.add_obstacle({'unique': obstacle_path + 'tile40.png'}, 30, 120, 7880, 100)
        self.world.add_obstacle({'unique': obstacle_path + 'tile40.png'}, 30, 120, 8050, 100)
        self.world.add_obstacle({'unique': obstacle_path + 'desert_rock4.png'}, 80, 80, 9200, 580)
        self.world.add_obstacle({'unique': obstacle_path + 'torch2_1.png'}, 130, 130, 9400, 190)
        self.world.add_obstacle({'unique': obstacle_path + 'Skeleton.png'}, 110, 130, 10000, 180)
        self.world.add_obstacle({'unique': obstacle_path + 'tile40.png'}, 30, 128, 10500, 205)
        self.world.add_obstacle({'unique': obstacle_path + 'tile40.png'}, 30, 128, 10628, 205)
        # ultimo piso
        self.world.add_obstacle({'unique': obstacle_path + 'stalagmite4.png'}, 70, 50, 11600, 270)
        self.world.add_final_portal({'unique': obstacle_path + 'door.png'}, 250, 250, 12500, 350)

    def __items_world2(self):
        # items
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 1100, 550)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 1450, 170, 1)
        self.world.add_heart(self.heart_animations, 60, 50, 2700, 320)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 3500, 370, 3)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 6550, 380, 5)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 6900, 200)
        self.world.add_heart(self.heart_animations, 60, 50, 7800, 150)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 8600, 290, 1)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 9450, 290)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 10490, 330, 5)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 11190, 330)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 11750, 270, 3)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 12400, 400, 5)

    def __assets_world3(self):
        # BACKGROUNDS MOVIBLES
        self.world.load_background_assets(["bg_dragonhell.png"])
        self.world.load_background_assets(["bg_greeninferno.png"])
        self.world.load_background_assets(["bg_dragonflame_upsidedown.png"])
        self.world.load_background_assets(["bg_greeninferno2.png"])
        self.world.load_background_assets(["bg_dragonhellend3.png"])
        # PARTE DE LOS ASSETS MOVIBLES
        self.world.load_assets(["background_01.png"], 3)
        self.world.load_assets(["near.png"], 1)
        self.world.load_assets(["near.png", "lava.png"], 2)
        self.world.load_assets(["background_01.png"], 2)
        self.world.load_assets(["lava_upsidedown.png"], 3, world_creator.SCREEN_HEIGHT)
        self.world.load_assets(["near.png"], 3)
        self.world.load_assets(["background_01.png", "lava.png"], 2)
        # SE CARGAN LOS ASSETS A LAS LISTAS PARA PONERLAS UNA DETRAS DE OTRA
        self.world.setup_assets(0)
        self.world.setup_background_assets()

    def __platforms_world3(self):
        # direccion img plataformas
        platform_path = "resources\\worlds\\dragonHell\\tiles\\"

        # tiles plataformas flotantes
        tiles_ground = {'beginning': platform_path + 'ground_7.png', 'middle': platform_path + 'ground_8.png',
                        'end': platform_path + 'ground_9.png'}
        tiles_bridge = {'beginning': platform_path + 'bridge_1.png', 'middle': platform_path + 'bridge_2.png',
                        'end': platform_path + 'bridge_1.png'}
        tiles_volcano = {'beginning': platform_path + 'volcano_03.png', 'middle': platform_path + 'volcano_04.png',
                         'end': platform_path + 'volcano_05.png'}
        tiles_volcano_ud = {'beginning': platform_path + 'volcano_ud_1.png',
                            'middle': platform_path + 'volcano_ud_2.png',
                            'end': platform_path + 'volcano_ud_3.png'}
        tiles_volcano_ud2 = {'beginning': platform_path + 'volcano_ud_4.png',
                             'middle': platform_path + 'volcano_ud_5.png',
                             'end': platform_path + 'volcano_ud_6.png'}
        # plataformas de piso (Crear muros)
        tiles_wall = {'beginning': platform_path + 'ground_1.png', 'middle': platform_path + 'ground_2.png',
                      'end': platform_path + 'ground_3.png',
                      'beginning_bottom': platform_path + 'ground_4.png',
                      'middle_bottom': platform_path + 'ground_5.png',
                      'end_bottom': platform_path + 'ground_6.png'}
        # agregacion de plataformas
        self.world.add_platform(tiles_wall, 400, 6, 5)  # PISO
        self.world.add_platform(tiles_ground, 500, 4, 600)  # flotante
        self.world.add_platform(tiles_wall, 200, 4, 570)  # PISO
        self.world.add_platform(tiles_ground, 275, 3, 990)  # flotante
        self.world.add_platform(tiles_wall, 350, 4, 1408)  # PISO
        # destruible
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 485, 1, 1890)
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 380, 1, 2074)
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 475, 1, 2238)
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 580, 1, 2402)
        # normal
        self.world.add_platform(tiles_wall, 40, 11, 1853)  # PISO
        # cambio de background 1
        self.world.add_platform({'unique': platform_path + 'volcano_02.png'}, 140, 1, 2657, 32)
        self.world.add_platform({'unique': platform_path + 'volcano_02.png'}, 230, 1, 2775, 32)
        self.world.add_platform({'unique': platform_path + 'volcano_02.png'}, 320, 1, 2927, 32)
        self.world.add_platform({'unique': platform_path + 'volcano_02.png'}, 120, 1, 2927, 32)
        self.world.add_platform(tiles_wall, 40, 5, 3121)  # PISO

        # movibles
        self.world.add_movable_platform(tiles_bridge, 140, 2, 3600, 90, -1, 32)  # flotante
        self.world.add_movable_platform(tiles_bridge, 280, 3, 3950, 80, 1, 32)  # flotante
        self.world.add_movable_platform(tiles_bridge, 390, 3, 4300, 100, -1, 32)  # flotante
        self.world.add_movable_platform(tiles_bridge, 400, 2, 4800, 110, 1, 32)  # flotante
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 90, 1, 4800)
        # 3 caminos
        self.world.add_platform(tiles_wall, 40, 23, 5080)  # PISO
        self.world.add_platform(tiles_ground, 290, 22, 5144)  # flotante
        self.world.add_platform(tiles_ground, 540, 21, 5208)  # flotante

        self.world.add_platform({'unique': platform_path + 'volcano_02.png'}, 150, 1, 6704, 32)
        # cambio de background 2
        # muro impasable se invierte el mundo
        for i in range(0, 13):
            self.world.add_platform({'unique': platform_path + 'brick_1.png'}, 60 * i, 1, 6768)
        # plataformas
        self.world.add_platform(tiles_volcano_ud, 568, 4, 6900, 32, True)  # flotante
        self.world.add_platform(tiles_volcano_ud, 478, 3, 7250, 32, True)  # flotante
        self.world.add_movable_platform({'unique': platform_path + 'volcano_ud_7.png'}, 388, 1, 7558, 40, 1, 32, True)
        self.world.add_platform(tiles_volcano_ud2, 278, 3, 7752, 32, True)  # flotante
        self.world.add_platform(tiles_volcano_ud2, 168, 2, 8080, 32, True)  # flotante
        self.world.add_platform({'unique': platform_path + 'volcano_ud_8.png'}, 398, 1, 8270, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_7.png'}, 278, 1, 8380, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_8.png'}, 528, 1, 8410, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_7.png'}, 158, 1, 8500, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_8.png'}, 428, 1, 8510, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_7.png'}, 318, 1, 8635, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_8.png'}, 418, 1, 8740, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_8.png'}, 518, 1, 8855, 32, True)
        self.world.add_platform({'unique': platform_path + 'volcano_ud_7.png'}, 378, 1, 8995, 32, True)
        self.world.add_platform(tiles_volcano_ud2, 278, 2, 9137, 32, True)  # flotante

        # cambio de background 3
        # muro impasable regresa a lo normal
        for i in range(0, 13):
            self.world.add_platform({'unique': platform_path + 'brick_1.png'}, 60 * i, 1, 9318)
        # PLATAFORMAS
        self.world.add_platform(tiles_wall, 100, 4, 9380)  # PISO
        self.world.add_platform(tiles_wall, 200, 3, 9736)  # PISO
        self.world.add_platform(tiles_wall, 300, 2, 10028)  # PISO
        self.world.add_platform({'unique': platform_path + 'bridge_1.png'}, 400, 1, 10256, 32)
        self.world.add_platform({'unique': platform_path + 'bridge_2.png'}, 500, 1, 10420, 32)
        self.world.add_platform({'unique': platform_path + 'bridge_1.png'}, 530, 1, 10534, 32)
        self.world.add_platform({'unique': platform_path + 'bridge_2.png'}, 580, 1, 10648, 32)
        # destruible
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 50, 1, 10490)
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 50, 1, 10600)
        # movibles
        self.world.add_movable_platform({'unique': platform_path + 'volcano_02.png'}, 100, 1, 10832, 60, -1, 32)
        self.world.add_movable_platform({'unique': platform_path + 'volcano_02.png'}, 210, 1, 11006, 62, 1, 32)
        self.world.add_movable_platform({'unique': platform_path + 'volcano_02.png'}, 310, 1, 11180, 57, -1, 32)
        self.world.add_movable_platform({'unique': platform_path + 'volcano_02.png'}, 410, 1, 11364, 65, 1, 32)
        # normal
        self.world.add_platform(tiles_wall, 250, 6, 11564)  # PISO
        # movibles
        self.world.add_movable_platform(tiles_volcano, 50, 2, 12048, 75, -1, 32)  # flotante
        self.world.add_movable_platform(tiles_volcano, 180, 2, 12315, 78, 1, 32)  # flotante
        # cambio de background 3
        self.world.add_movable_platform(tiles_volcano, 310, 2, 12523, 60, -1, 32)  # flotante
        self.world.add_movable_platform(tiles_volcano, 70, 2, 12800, 70, 1, 32)  # flotante
        # kit movible
        self.world.add_movable_platform(tiles_volcano, 180, 3, 12932, 30, 1, 32)
        self.world.add_movable_platform(tiles_volcano, 335, 2, 12996, 30, 1, 32)
        self.world.add_movable_platform({'unique': platform_path + 'volcano_02.png'}, 490, 1, 13060, 30, 1, 32)
        self.world.add_movable_platform(tiles_wall, 610, 2, 13100, 30, 1)  # PISO
        # destruible
        self.world.add_killable_platfrom({'unique': platform_path + 'brick_2.png'}, 580, 1, 12700)
        # normal
        self.world.add_platform(tiles_wall, 400, 2, 13319)  # PISO
        self.world.add_platform(tiles_wall, 230, 2, 13550)  # PISO

    def __obstacles_world3(self):
        # direccion de obstaculos
        obstacle_path = "resources\\worlds\\dragonHell\\objects\\"
        # diccionarios de obstaculos movibles
        fireball_y = {'animations': [obstacle_path + 'fireball_11.png', obstacle_path + 'fireball_12.png']}
        fireball_x = {'animations': [obstacle_path + 'fireball_h1.png', obstacle_path + 'fireball_h2.png',
                                     obstacle_path + 'fireball_h3.png', obstacle_path + 'fireball_h4.png']}
        # agregacion de obstaculos
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 40, 100, 150, 435)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'rock_2.png'}, 75, 75, 800, 575)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'rock_2.png'}, 100, 100, 675, 295)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'stones.png'}, 100, 100, 1480, 450)  # Obstaculo
        self.world.add_movable_obstacle(fireball_y, 60, 45, 2213, 400, 80, 3, False, True)  # Obstaculo movible y
        self.world.add_obstacle({'unique': obstacle_path + 'volcano.png'}, 130, 170, 2153, 170)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 40, 64, 2927, 350)  # Obstaculo
        # cambio de background 1
        self.world.add_obstacle({'unique': obstacle_path + 'rock_1.png'}, 130, 130, 3210, 170)  # Obstaculo
        # movibles
        self.world.add_movable_obstacle(fireball_y, 100, 70, 3600, 140, 100, 3, False, True)  # Obstaculo movible y
        self.world.add_movable_obstacle(fireball_y, 100, 70, 4450, 190, 150, 3, False, True)  # Obstaculo movible y
        # 3 caminos
        # ABAJO
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 5180, 230)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 5480, 75)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 5700, 230)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 6020, 75)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 6280, 75)  # Obstaculo
        # MEDIO
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 5240, 325)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 5480, 325)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 5700, 480)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 6020, 480)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 60, 75, 6280, 325)  # Obstaculo
        # ARRIBA
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 100, 150, 5380, 635)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 5700, 730)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 100, 150, 6020, 635)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 120, 150, 6280, 730)  # Obstaculo
        self.world.add_portal_ud({'unique': obstacle_path + 'portal.png',
                                  'next_portal': [7006, 574]}, 280, 220, 6550, 550)  # PORTAL ENVIA
        # cambio de background 2
        # Obstaculos del upsidedown
        self.world.add_portal_ud({'unique': obstacle_path + 'portal_ud.png'}, 280, 220, 6900, 300)  # PORTAL RECIBE
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 40, 64, 7820, 248)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes_ud.png'}, 40, 64, 8740, 388)  # Obstaculo
        self.world.add_portal_ud({'unique': obstacle_path + 'portal_ud.png',
                                  'next_portal': [9496, 426]}, 280, 220, 9100, 260)  # PORTAL ENVIA
        # Obstaculos del regreso a fisicas normales
        # cambio de background 3
        self.world.add_portal_ud({'unique': obstacle_path + 'portal.png'}, 280, 220, 9390, 500)  # PORTAL RECIBE
        self.world.add_obstacle({'unique': obstacle_path + 'rock_1.png'}, 90, 90, 9790, 285)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 30, 30, 10125, 330)  # Obstaculo
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 30, 64, 10534, 560)  # Obstaculo
        self.world.add_movable_obstacle(fireball_y, 60, 45, 11750, 550, 65, 3, False, True)  # Obstaculo movible y
        self.world.add_obstacle({'unique': obstacle_path + 'volcano.png'}, 130, 170, 11690, 380)  # Obstaculo
        self.world.add_movable_obstacle(fireball_y, 100, 70, 12445, 300, 110, 3, False, True)  # Obstaculo movible y
        # cambio de background 4
        self.world.add_movable_obstacle(fireball_y, 100, 70, 13235, 290, 170, 3, False, True)  # Obstaculo movible y
        self.world.add_obstacle({'unique': obstacle_path + 'spikes.png'}, 30, 64, 13319, 425)  # Obstaculo
        self.world.add_movable_obstacle(fireball_y, 100, 70, 13470, 200, 140, 3, False, True)  # Obstaculo movible y
        # BOLAS DE FUEGO EN X
        self.world.add_movable_obstacle(fireball_x, 50, 50, 1900, 350, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 4800, 170, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 6150, 300, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 9300, 450, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 14050, 430, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 16730, 240, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 19854, 450, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 21808, 290, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_movable_obstacle(fireball_x, 50, 50, 25072, 200, 100, -1, True, False)  # Obstaculo movible x
        self.world.add_final_portal({'unique': obstacle_path + 'Star.png'}, 100, 100, 13600, 350)

    def __items_world3(self):
        # Items
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 2600, 640)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 2665, 200, 5)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 3900, 400, 1)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 4805, 150, 3)
        self.world.add_heart(self.heart_animations, 60, 50, 5900, 350)
        self.world.add_diamond(self.diamond3_animations, 60, 50, 6450, 620, 5)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 6450, 110)
        self.world.add_misterybox({'unique': self.path_item + 'bonus_ud.png'}, 64, 64, 8515, 350)
        self.world.add_diamond(self.diamond1_animations, 60, 50, 10655, 650, 1)
        self.world.add_heart(self.heart_animations, 60, 50, 10500, 110)
        self.world.add_diamond(self.diamond2_animations, 60, 50, 11200, 400, 3)
        self.world.add_misterybox({'unique': self.path_item + 'bonus.png'}, 64, 64, 12700, 650)

    def __run_game(self, mundo: int):
        run = True
        cont_shield = []
        cont_effect = []
        for i in range(len(self.players_list)):
            cont_shield.append(0)
            cont_effect.append(0)

        cont_static = 0
        var_speed = 0
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        while run:
            self.clock.tick(60)
            all_dead_cont = 0
            for player in self.players_list:
                if not player.is_alive:
                    all_dead_cont += 1

            if all_dead_cont == len(self.players_list):
                self.world.set_final(True)

            if not self.world.final:
                if mundo == 3:
                    first, last = self.world.get_first_and_last_position()
                    if -1500 >= first >= -3499:
                        self.world.update_background(0.5)
                    if -5800 >= first >= -6799:
                        self.world.update_background(1.0)
                    if -8350 >= first >= -9349:
                        self.world.update_background(1.0)
                    if last <= 1501:
                        self.world.update_background(0.5)
                # Verificacion de todos choques con obstaculos y el portal final de todos los jugadores
                for i, player in enumerate(self.players_list):
                    player.check_final_portal(self.world, mundo)
                    player.update_collision_obstacles(self.world, i)  # CRISTIAN
                    if player.shield:
                        cont_shield[i] += 1
                        if cont_shield[i] == 200:
                            player.shield = False
                            cont_shield[i] = 0
                # aqui iba lo de items

                # Verificacion de movimiento, actualizacion y deslizarce de los players
                for player in self.players_list:
                    if player.is_alive:
                        player.move()
                        player.update(self.world.get_platform_group(), self.world.killable_plaforms, var_speed)
                        player.slide(self.world.get_platform_group())

                for vevent in pygame.event.get():
                    if vevent.type == pygame.KEYDOWN:
                        if vevent.key == pygame.K_SPACE:
                            self.__pause()
                    if vevent.type == pygame.QUIT:
                        """pygame.quit()
                        sys.exit()"""
                        self.__main_menu()
                    # Verificacion de salto de todos los players
                    for player in self.players_list:
                        if player.is_alive:
                            player.jump(vevent, self.world.get_platform_group(), self.world.killable_plaforms)
                            player.cancel_jump(vevent)

                if cont_static == 100:
                    var_speed = self.world.speed
                    self.world.update(1)
                    self.world.update_platform(1)
                    self.world.update_obstacle(1)
                    self.world.update_item(1)
                else:
                    cont_static += 1

                self.screen.fill((19, 64, 28))
                self.world.render(self.screen)
                self.world.render_platform(self.screen)
                self.world.render_obstacle(self.screen)
                self.world.render_item(self.screen)
                # Verificacion de obtencion de items y posibles ataques
                for i, player in enumerate(self.players_list):
                    if player.is_alive:
                        player.update_collision_items(self.world, self.possible_attacks[f"possible_attacks_p{i + 1}"])
                        if player.with_effect['effect']:
                            cont_effect[i] += 1
                            self.world.update_effect(0, False)
                            self.world.render_effect(self.screen)
                            if player.with_effect['effect_type'] == 'lightning':
                                if cont_effect[i] == 150:
                                    player.with_effect['effect'] = False
                                    player.character.petrify = False
                                    cont_effect[i] = 0
                            elif cont_effect[i] == 300:
                                player.with_effect['effect'] = False
                                cont_effect[i] = 0
                                if player.with_effect['effect_type'] == 'speed_up':
                                    player.character.acc -= player.with_effect['effect_value']
                                else:
                                    player.character.acc += player.with_effect['effect_value'] * - 1
                        if player.shield:
                            self.world.update_effect(i, True)
                            self.world.render_effect_shield(self.screen, i)
                for player in self.players_list:
                    if player.is_alive:
                        # self.moving_sprites.draw(self.screen)
                        self.screen.blit(player.character.image, player.character.rect)
                # DIBUJAR ATRIBUTOS DEL JUGADOR
                self.screen.blit(self.bg_info, (0, 0))

                for i, player in enumerate(self.players_list):
                    # PLAYER
                    options_text = self.font_23.render(f"PLAYER {i + 1}", True, "White")
                    options_rect = options_text.get_rect(center=(1100, 70 * (i + 1) + (i * 100)))  # 240 410 580
                    self.screen.blit(options_text, options_rect)
                    # VIDAS O MUERTE
                    if player.is_alive:
                        self.screen.blit(self.life_img, self.life_img.get_rect(center=(1050, 120 * (i + 1) + (i * 50))))
                        options_text = self.font_23.render(f"X {player.lives}", True, "White")
                        options_rect = options_text.get_rect(center=(1125, 120 * (i + 1) + (i*50)))  # 290 460 630
                        self.screen.blit(options_text, options_rect)
                    else:
                        self.screen.blit(self.dead_img, self.dead_img.get_rect(center=(1100, 120 * (i + 1) + (i*50))))
                    # DIAMANTES
                    self.screen.blit(self.diamond_img,
                                     self.diamond_img.get_rect(center=(1050, 170 * (i + 1))))
                    options_text = self.font_23.render(f"X {player.diamonds}", True, "White")
                    options_rect = options_text.get_rect(center=(1125, 170 * (i + 1) + 5))
                    self.screen.blit(options_text, options_rect)

                pygame.display.flip()
                pygame.display.update()

            else:
                options_text = self.__get_font(20).render("PRESIONE ENTER", True, "White")
                options_rect = options_text.get_rect(center=(800, 600))
                self.screen.blit(options_text, options_rect)
                options_text1 = self.__get_font(20).render("PARA CONTINUAR...", True, "White")
                options_rect1 = options_text1.get_rect(center=(800, 650))
                self.screen.blit(options_text1, options_rect1)
                pygame.display.flip()
                pygame.display.update()
                for vevent in pygame.event.get():
                    if vevent.type == pygame.QUIT:
                        """pygame.quit()
                        sys.exit()"""
                        self.__main_menu()
                    if vevent.type == pygame.KEYDOWN:
                        if vevent.key == pygame.K_RETURN:
                            run = False
        # RESETEAR EL PLAYER Y CHARACTER
        for i, player in enumerate(self.players_list):
            if i == 0:
                player.reset_player(0.5, -0.12, 1.50, -15)
            elif i == 1:
                player.reset_player(0.65, -0.11, 1.50, -12.5)
            elif i == 2:
                player.reset_player(0.55, -0.12, 1.85, -13)
            elif i == 3:
                player.reset_player(0.5, -0.11, 1.75, -14)

    def __play(self):
        # last_frame_time = -1
        for mundo in range(1, 4):
            cont = 0
            if mundo == 1:
                while cont < 500:
                    self.screen.fill("Black")
                    options_text = self.__get_font(30 + int(cont / 20)).render("MUNDO 1", True, "White")
                    options_rect = options_text.get_rect(center=(600, 300))
                    self.screen.blit(options_text, options_rect)
                    options_text = self.__get_font(45 + int(cont / 25)).render("DARK FOREST", True, "White")
                    options_rect = options_text.get_rect(center=(600, 500))
                    self.screen.blit(options_text, options_rect)
                    pygame.display.update()
                    cont += 1

                # PRIMER MUNDO ----- CLAUDIA
                path_world1 = "resources\\worlds\\darkForest\\Background\\"
                # declaracion del primer mundo
                pygame.display.set_caption("Dark Forest")
                self.world = WorldCreator("Dark Forest", path_world1, 3, len(self.players_list))
                self.world.solid_background(["BG_Decor.png", "Middle_Decor.png"])
                self.__assets_world1()
                self.__platforms_world1()
                self.__obstacles_world1()
                self.__items_world1()
            elif mundo == 2:
                while cont < 500:
                    self.screen.fill("Black")
                    options_text = self.__get_font(30 + int(cont / 20)).render("MUNDO 2", True, "White")
                    options_rect = options_text.get_rect(center=(600, 300))
                    self.screen.blit(options_text, options_rect)
                    options_text = self.__get_font(35 + int(cont / 25)).render("LAND OF DEADLY LAUGHS", True, "White")
                    options_rect = options_text.get_rect(center=(600, 500))
                    self.screen.blit(options_text, options_rect)
                    pygame.display.update()
                    cont += 1

                # SEGUNDO MUNDO -----  FER
                path4 = "resources\\worlds\\LandOfDeadlyLaughs\\background\\"
                # Declaracion del segundo mundo
                pygame.display.set_caption("Land Of Deadly Laughs")
                self.world = WorldCreator("Land Of Deadly Laughs", path4, 3, len(self.players_list))
                self.world.solid_background(["postapocalypse3.png"])
                self.__assets_world2()
                self.__platforms_world2()
                self.__obstacles_world2()
                self.__items_world2()

            elif mundo == 3:
                while cont < 500:
                    self.screen.fill("Black")
                    options_text = self.__get_font(30 + int(cont / 20)).render("MUNDO 3", True, "White")
                    options_rect = options_text.get_rect(center=(600, 300))
                    self.screen.blit(options_text, options_rect)
                    options_text = self.__get_font(40 + int(cont / 25)).render("DRAGON HELL", True, "White")
                    options_rect = options_text.get_rect(center=(600, 500))
                    self.screen.blit(options_text, options_rect)
                    pygame.display.update()
                    cont += 1

                # TERCER MUNDO ----- CRISTIAN
                path_world3 = "resources\\worlds\\dragonHell\\background\\"
                # Declaracion del tercer mundo
                self.world = WorldCreator("Dragon Hell", path_world3, 3, len(self.players_list))
                self.world.solid_background(["bg_dragonhell.png"])
                pygame.display.set_caption("Dragon Hell")
                self.__assets_world3()
                self.__platforms_world3()
                self.__obstacles_world3()
                self.__items_world3()
            self.screen.fill("Black")
            pygame.display.update()

            # correr el mundo
            self.__run_game(mundo)

        # IMPRIMIR LUGARES DE PERSONAJES
        run = True
        points = []
        for i, player in enumerate(self.players_list):
            points.append([player.points + int(player.diamonds/3), i+1])
        print(points)
        points = sorted(points, reverse=True)
        print(points)
        self.screen.blit(self.background_winers_image, self.background_winers_image.get_rect())
        for i, player in enumerate(points):
            # PLAYER
            options_text = self.__get_font(70).render(f"{i+1}", True, "White")
            options_rect = options_text.get_rect(center=(200, 100 * (i + 1) + (i * 65)))  # 240 410 580
            self.screen.blit(options_text, options_rect)

            options_text = self.font_23.render(f"PLAYER {player[1]}", True, "White")
            options_rect = options_text.get_rect(center=(600, 70 * (i + 1) + (i * 100)))  # 240 410 580
            self.screen.blit(options_text, options_rect)
            options_text = self.font_23.render(f"POINTS {player[0]}", True, "White")
            options_rect = options_text.get_rect(center=(600, 120 * (i + 1) + (i * 50)))  # 290 460 630
            self.screen.blit(options_text, options_rect)

            options_text = self.font_23.render("PRESIONE ENTER", True, "White")
            options_rect = options_text.get_rect(center=(1000, 600))
            self.screen.blit(options_text, options_rect)
            options_text1 = self.font_23.render("PARA CONTINUAR...", True, "White")
            options_rect1 = options_text1.get_rect(center=(1000, 650))
            self.screen.blit(options_text1, options_rect1)
            pygame.display.update()
        while run:
            for vevent in pygame.event.get():
                if vevent.type == pygame.QUIT:
                    run = False
                if vevent.type == pygame.KEYDOWN:
                    if vevent.key == pygame.K_RETURN:
                        run = False
        # Regresar al menu
        self.__main_menu()

    def __options(self):
        pygame.display.set_caption("Dead Run")
        while True:
            self.clock.tick(60)
            options_mouse_pos = pygame.mouse.get_pos()

            self.screen.fill("white")

            options_text = self.__get_font(45).render("MULTIPLAYER", True, "Black")
            options_rect = options_text.get_rect(center=(600, 50))
            self.screen.blit(options_text, options_rect)

            one_player = Button(image=self.one_player_img, pos=(150, 400), text_input="1 PLAYER",
                                font=self.__get_font(25), base_color="Black", hovering_color="Green")

            two_players = Button(image=self.twp_player_img, pos=(450, 400), text_input="2 PLAYERS",
                                 font=self.__get_font(25), base_color="Black", hovering_color="Green")
            tree_players = Button(image=self.tree_player_img, pos=(750, 400), text_input="3 PLAYERS",
                                  font=self.__get_font(25), base_color="Black", hovering_color="Green")
            four_players = Button(image=self.four_player_img, pos=(1050, 400), text_input="4 PLAYERS",
                                  font=self.__get_font(25), base_color="Black", hovering_color="Green")

            one_player.change_color(options_mouse_pos)
            two_players.change_color(options_mouse_pos)
            tree_players.change_color(options_mouse_pos)
            four_players.change_color(options_mouse_pos)
            one_player.update(self.screen)
            two_players.update(self.screen)
            tree_players.update(self.screen)
            four_players.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if one_player.check_for_input(options_mouse_pos):
                        self.actual_players = 1
                        self.__main_menu()
                    if two_players.check_for_input(options_mouse_pos):
                        self.actual_players = 2
                        self.__main_menu()
                    if tree_players.check_for_input(options_mouse_pos):
                        self.actual_players = 3
                        self.__main_menu()
                    if four_players.check_for_input(options_mouse_pos):
                        self.actual_players = 4
                        self.__main_menu()

            pygame.display.update()

    def __main_menu(self):
        # mundo = 1
        self.screen.blit(self.background_image, (0, 0))
        pygame.mixer.music.set_volume(0.2)
        pygame.mixer.music.play(-1)
        while True:
            self.clock.tick(60)
            menu_mouse_pos = pygame.mouse.get_pos()
            menu_text = self.__get_font(100).render("DEAD RUN", True, "#f6ecf5")  # b68f40
            menu_rect = menu_text.get_rect(center=(600, 100))

            play_button = Button(image=pygame.image.load("resources/assets/Play Rect.png").convert_alpha(),
                                 pos=(600, 250), text_input="PLAY", font=self.__get_font(75), base_color="#d7fcd4",
                                 hovering_color="White")
            options_button = Button(image=pygame.image.load("resources/assets/Options Rect.png").convert_alpha(),
                                    pos=(600, 400), text_input="PLAYERS", font=self.__get_font(75),
                                    base_color="#d7fcd4", hovering_color="White")
            quit_button = Button(image=pygame.image.load("resources/assets/Quit Rect.png").convert_alpha(),
                                 pos=(600, 550), text_input="QUIT", font=self.__get_font(75), base_color="#d7fcd4",
                                 hovering_color="White")

            self.screen.blit(menu_text, menu_rect)

            for button in [play_button, options_button, quit_button]:
                button.change_color(menu_mouse_pos)
                button.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if play_button.check_for_input(menu_mouse_pos):
                        if self.actual_players == 1:
                            self.__one_player()
                        elif self.actual_players == 2:
                            self.__two_players()
                        elif self.actual_players == 3:
                            self.__three_players()
                        elif self.actual_players == 4:
                            self.__four_players()
                        pygame.mixer.music.stop()
                        self.__play()
                    if options_button.check_for_input(menu_mouse_pos):
                        self.__options()
                    if quit_button.check_for_input(menu_mouse_pos):
                        pygame.quit()
                        sys.exit()

            pygame.display.update()

    def __one_player(self):
        self.p1 = Player(self.player_objects['character'][0], 'Player 1',
                         self.player_objects['controls'][0])
        self.p2 = None
        self.p3 = None
        self.p4 = None

        self.possible_attacks = {"possible_attacks_p1": [self.p1],
                                 "possible_attacks_p2": None,
                                 "possible_attacks_p3": None,
                                 "possible_attacks_p4": None}

        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.p1.character)

        self.players_list = []
        self.players_list.append(self.p1)

    def __two_players(self):
        self.p1 = Player(self.player_objects['character'][0], 'Player 1',
                         self.player_objects['controls'][0])
        self.p2 = Player(self.player_objects['character'][1], 'Player 2',
                         self.player_objects['controls'][1])
        self.p3 = None
        self.p4 = None

        self.possible_attacks = {"possible_attacks_p1": [self.p2],
                                 "possible_attacks_p2": [self.p1],
                                 "possible_attacks_p3": None,
                                 "possible_attacks_p4": None}

        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.p1.character)
        self.moving_sprites.add(self.p2.character)

        self.players_list = []
        self.players_list.append(self.p1)
        self.players_list.append(self.p2)

    def __three_players(self):
        self.p1 = Player(self.player_objects['character'][0], 'Player 1',
                         self.player_objects['controls'][0])
        self.p2 = Player(self.player_objects['character'][1], 'Player 2',
                         self.player_objects['controls'][1])
        self.p3 = Player(self.player_objects['character'][2], 'Player 3',
                         self.player_objects['controls'][2])
        self.p4 = None

        self.possible_attacks = {"possible_attacks_p1": [self.p2, self.p3],
                                 "possible_attacks_p2": [self.p1, self.p3],
                                 "possible_attacks_p3": [self.p1, self.p2],
                                 "possible_attacks_p4": None}

        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.p1.character)
        self.moving_sprites.add(self.p2.character)
        self.moving_sprites.add(self.p3.character)

        self.players_list = []
        self.players_list.append(self.p1)
        self.players_list.append(self.p2)
        self.players_list.append(self.p3)

    def __four_players(self):
        self.p1 = Player(self.player_objects['character'][0], 'Player 1',
                         self.player_objects['controls'][0])
        self.p2 = Player(self.player_objects['character'][1], 'Player 2',
                         self.player_objects['controls'][1])
        self.p3 = Player(self.player_objects['character'][2], 'Player 3',
                         self.player_objects['controls'][2])
        self.p4 = Player(self.player_objects['character'][3], 'Player 4',
                         self.player_objects['controls'][3])
        self.possible_attacks = {"possible_attacks_p1": [self.p2, self.p3, self.p4],
                                 "possible_attacks_p2": [self.p1, self.p3, self.p4],
                                 "possible_attacks_p3": [self.p1, self.p2, self.p4],
                                 "possible_attacks_p4": [self.p1, self.p2, self.p3]}
        self.moving_sprites = pygame.sprite.Group()
        self.moving_sprites.add(self.p1.character)
        self.moving_sprites.add(self.p2.character)
        self.moving_sprites.add(self.p3.character)
        self.moving_sprites.add(self.p4.character)
        self.players_list = []
        self.players_list.append(self.p1)
        self.players_list.append(self.p2)
        self.players_list.append(self.p3)
        self.players_list.append(self.p4)

    def __pause(self):
        pause = True
        while pause:
            self.clock.tick(60)
            options_mouse_pos = pygame.mouse.get_pos()

            self.screen.blit(self.pause_rect, self.pause_rect.get_rect(center=(500, 350)))

            options_text = self.__get_font(50).render("PAUSE", True, "White")
            options_rect = options_text.get_rect(center=(500, 175))
            self.screen.blit(options_text, options_rect)

            btn_play = Button(image=None, pos=(500, 400), text_input="RESUME", font=self.__get_font(40),
                              base_color="White", hovering_color="Green")

            btn_play.change_color(options_mouse_pos)
            btn_play.update(self.screen)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if btn_play.check_for_input(options_mouse_pos):
                        pause = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        pause = False
            pygame.display.update()

    def dead_run_play(self):
        self.__main_menu()
