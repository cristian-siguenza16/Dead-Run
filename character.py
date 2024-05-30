import pygame
import os


class Character(pygame.sprite.Sprite):
    def __init__(self, acc: float,  friction: float, sliding: float, jump_height: float, name: str):

        super().__init__()
        # Personaje
        self.sprite_idle_right: list[pygame.image] = []
        self.sprite_idle_left: list[pygame.image] = []

        self.sprite_running_right: list[pygame.image] = []
        self.sprite_running_left: list[pygame.image] = []

        self.sprite_jump_start_right: list[pygame.image] = []
        self.sprite_jump_loop_right: list[pygame.image] = []

        self.sprite_jump_start_left: list[pygame.image] = []
        self.sprite_jump_loop_left: list[pygame.image] = []

        self.sprite_falling_down_right: list[pygame.image] = []
        self.sprite_falling_down_left: list[pygame.image] = []

        self.sprite_sliding_right: list[pygame.image] = []
        self.sprite_sliding_left: list[pygame.image] = []
        self.name = name
        path_list = os.listdir(f"resources/sprites/{name}/Idle Blinking")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Idle Blinking/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(19, 19, 68, 92)
            self.sprite_idle_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_idle_left.append(image)

        path_list = os.listdir(f"resources/sprites/{name}/Jump Start")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Jump Start/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(19, 19, 68, 92)
            self.sprite_jump_start_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_jump_start_left.append(image)

        path_list = os.listdir(f"resources/sprites/{name}/Jump Loop")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Jump Loop/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(19, 19, 68, 92)
            self.sprite_jump_loop_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_jump_loop_left.append(image)

        path_list = os.listdir(f"resources/sprites/{name}/Running")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Running/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(19, 19, 68, 92)
            self.sprite_running_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_running_left.append(image)

        path_list = os.listdir(f"resources/sprites/{name}/Falling Down")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Falling Down/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(19, 19, 68, 92)
            self.sprite_falling_down_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_falling_down_left.append(image)

        path_list = os.listdir(f"resources/sprites/{name}/Sliding")
        for sprite in path_list:
            image = pygame.image.load(f"resources/sprites/{name}/Sliding/{sprite}").convert_alpha()
            image = pygame.transform.scale(image, (110, 130))
            image = image.subsurface(0, 46, 68, 72)
            self.sprite_sliding_right.append(image)
            image = pygame.transform.flip(image, True, False)
            self.sprite_sliding_left.append(image)

        self.image_ghost = pygame.image.load("resources/assets/ghost.png").convert_alpha()
        self.image_ghost = pygame.transform.scale(self.image_ghost, (110, 130))
        self.current_sprite_idle_right: float = 0
        self.current_sprite_idle_left: float = 0

        self.current_sprite_running_right: float = 0
        self.current_sprite_running_left: float = 0

        self.current_sprite_jump_right: float = 0
        self.current_sprite_jump_left: float = 0
        self.jump_start: float = True

        self.current_sprite_falling_down_right: float = 0
        self.current_sprite_falling_down_left: float = 0

        self.current_sprite_sliding_right: float = 0
        self.current_sprite_sliding_left: float = 0

        self.image = self.sprite_idle_right[int(self.current_sprite_idle_right)]
        self.rect = self.image.get_rect()
        self.rect.topleft = [50, 200]

        # Caracteristicas
        self.acc = acc
        self.friction = friction
        self.jump_height = jump_height
        self.slide = sliding
        self.slide_distance: float = 0
        self.upsidedown: bool = False  # Pedro
        self.petrify: bool = False  # PARALIZA AL CARACTER

    def idle_right(self):
        self.current_sprite_idle_right += 0.20
        if self.current_sprite_idle_right >= len(self.sprite_idle_right):
            self.current_sprite_idle_right = 0
        self.image = self.sprite_idle_right[int(self.current_sprite_idle_right)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def idle_left(self):
        self.current_sprite_idle_left += 0.20
        if self.current_sprite_idle_left >= len(self.sprite_idle_left):
            self.current_sprite_idle_left = 0
        self.image = self.sprite_idle_left[int(self.current_sprite_idle_left)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def running_right(self):
        self.current_sprite_running_right += 0.30
        if self.current_sprite_running_right >= len(self.sprite_running_right):
            self.current_sprite_running_right = 0
        self.image = self.sprite_running_right[int(self.current_sprite_running_right)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def running_left(self):
        self.current_sprite_running_left += 0.30
        if self.current_sprite_running_left >= len(self.sprite_running_left):
            self.current_sprite_running_left = 0
        self.image = self.sprite_running_left[int(self.current_sprite_running_left)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def jump_right(self):
        if self.jump_start:
            self.current_sprite_jump_right += 1
            if self.current_sprite_jump_right >= len(self.sprite_jump_start_right):
                self.current_sprite_jump_right = 0
                self.jump_start = False
            self.image = self.sprite_jump_start_right[int(self.current_sprite_jump_right)]
            if self.upsidedown:
                self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.current_sprite_jump_right += 1
            if self.current_sprite_jump_right >= len(self.sprite_jump_loop_right):
                self.current_sprite_jump_right = 0
            self.image = self.sprite_jump_loop_right[int(self.current_sprite_jump_right)]
            if self.upsidedown:
                self.image = pygame.transform.flip(self.image, False, True)

    def jump_left(self):
        if self.jump_start:
            self.current_sprite_jump_left += 1
            if self.current_sprite_jump_left >= len(self.sprite_jump_start_left):
                self.current_sprite_jump_left = 0
                self.jump_start = False
            self.image = self.sprite_jump_start_left[int(self.current_sprite_jump_left)]
            if self.upsidedown:
                self.image = pygame.transform.flip(self.image, False, True)
        else:
            self.current_sprite_jump_left += 1
            if self.current_sprite_jump_left >= len(self.sprite_jump_loop_left):
                self.current_sprite_jump_left = 0
            self.image = self.sprite_jump_loop_left[int(self.current_sprite_jump_left)]
            if self.upsidedown:
                self.image = pygame.transform.flip(self.image, False, True)

    def falling_down_right(self):
        self.current_sprite_falling_down_right += 1
        if self.current_sprite_falling_down_right >= len(self.sprite_falling_down_right):
            self.current_sprite_falling_down_right = 0
        self.image = self.sprite_falling_down_right[int(self.current_sprite_falling_down_right)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def falling_down_left(self):
        self.current_sprite_falling_down_left += 1
        if self.current_sprite_falling_down_left >= len(self.sprite_falling_down_left):
            self.current_sprite_falling_down_left = 0
        self.image = self.sprite_falling_down_left[int(self.current_sprite_falling_down_left)]
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def slide_right(self):
        self.current_sprite_sliding_right += 1
        if self.current_sprite_sliding_right >= len(self.sprite_sliding_right):
            self.current_sprite_sliding_right = 0
        self.image = self.sprite_sliding_right[int(self.current_sprite_sliding_right)]
        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def slide_left(self):
        self.current_sprite_sliding_left += 1
        if self.current_sprite_sliding_left >= len(self.sprite_sliding_left):
            self.current_sprite_sliding_left = 0
        self.image = self.sprite_sliding_left[int(self.current_sprite_sliding_left)]
        self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
        if self.upsidedown:
            self.image = pygame.transform.flip(self.image, False, True)

    def reset_rect(self):
        if self.upsidedown:
            self.image = self.sprite_idle_right[int(self.current_sprite_idle_right)]
            self.image = pygame.transform.flip(self.image, False, True)
            print(self.rect)
            self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
            print(self.rect)
        else:
            self.image = self.sprite_idle_right[int(self.current_sprite_idle_right)]
            self.rect = self.image.get_rect(x=self.rect.x, y=self.rect.y)
