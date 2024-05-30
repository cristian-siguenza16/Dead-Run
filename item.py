import pygame
from player_component import PlayerComponent

SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class Item(pygame.sprite.Sprite, PlayerComponent):
    def __init__(self, player: PlayerComponent | None, tiles_path: dict[str, any], height: int,
                 widht: int, x: int, y: int, speed: float):
        super(Item, self).__init__()
        self.player = player
        self.widht = widht
        self.height = height
        self.y = y
        self.speed = speed
        self.move_y = False
        self.move_x = False
        if "unique" in tiles_path:
            self.animation = False
            self.image = pygame.image.load(tiles_path["unique"]).convert_alpha()
            self.image = pygame.transform.scale(self.image, (self.widht, self.height))
        elif "animation" in tiles_path:
            self.animation = True
            self.animation_list = []
            self.index = 0
            for path in tiles_path['animations']:
                self.image = pygame.image.load(path).convert_alpha()
                self.image = pygame.transform.scale(self.image, (self.widht, self.height))
                self.animation_list.append(self.image)
            self.move_y = tiles_path['move_y']
            self.move_x = tiles_path['move_x']
            self.image = self.animation_list[self.index]
            self.mask = pygame.mask.from_surface(self.image)
        else:
            self.image = None
            self.animation_list = None

        self.pos = pygame.math.Vector2(x, SCREEN_HEIGHT - self.y)
        self.rect = self.image.get_rect(topleft=(x, self.pos.y))

    def update(self, delta_time):
        self.pos.x -= self.speed * delta_time
        self.rect.topleft = self.pos
        if self.animation:
            if self.move_x:
                self.__animation_x()

        if self.rect.right < -50:
            self.kill()

    def get_reaction(self) -> dict:
        return self.player.get_reaction()

    def get_lives(self) -> int:
        return self.player.get_lives()

    def get_diamonds(self) -> int:
        return self.player.get_diamonds()

    def __animation_x(self):
        self.index += 0.15
        if self.index >= len(self.animation_list):
            self.index = 0
        self.image = self.animation_list[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)

    def set_concrete_player_component(self, player: PlayerComponent):
        self.player = player
