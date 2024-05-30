import os

import pygame
from player import Player


class EffectAnimation:
    def __init__(self, speed: float, player: Player, animation: int):
        self.speed = speed
        self.player: Player = player
        self.animation = False
        self.lightning_animation: list[pygame.image] = []
        self.index = 0
        self.counter = 0
        self.type_animation = animation
        if self.type_animation == 1:
            self.image = pygame.image.load(f"resources/assets/spped_up_image.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (30, 65))
            self.pos = pygame.math.Vector2(self.player.pos.x - 5, self.player.pos.y - 40)
            self.rect = self.image.get_rect(topright=self.pos)
        elif self.type_animation == 2:
            self.image = pygame.image.load(f"resources/assets/speed_down_image.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (50, 40))
            self.pos = pygame.math.Vector2(self.player.pos.x + 10, self.player.pos.y - 30)
            self.rect = self.image.get_rect(topright=self.pos)
        elif self.type_animation == 3:
            self.animation = True
            self.path_list = os.listdir(f"resources/assets/lightning")
            y = player.character.rect.midbottom[1] + (70 * (player.character.rect.midbottom[1] / 390))
            for sprite in self.path_list:
                image = pygame.image.load(f"resources/assets/lightning/{sprite}").convert_alpha()
                #image = pygame.transform.scale(image, (int(y / 1.56), y))
                image = pygame.transform.scale(image, (430, 750))
                self.lightning_animation.append(image)
            self.y_plus = (30 * (750/390))
            self.image = self.lightning_animation[int(self.index)]
            x = player.character.rect.midbottom[0] - self.image.get_rect().midtop[0] + 20
            self.pos = pygame.math.Vector2(x, -10)
            self.rect = self.image.get_rect(midbottom=(self.pos.x, y))
        elif self.type_animation == 4:
            self.image = pygame.image.load(f"resources/assets/bubble.png").convert_alpha()
            self.image = pygame.transform.scale(self.image, (120, 120))
            self.pos = pygame.math.Vector2(self.player.pos.x - 5, self.player.pos.y + 15)
            # self.pos = pygame.math.Vector2(0, 0)
            self.rect = self.image.get_rect(topright=self.pos)

    def update(self):
        if self.type_animation == 1:
            self.pos.x = self.player.pos.x - 5
            self.pos.y = self.player.pos.y - 40
            self.rect.topright = self.pos
        elif self.type_animation == 2:
            self.pos.x = self.player.pos.x + 25
            self.pos.y = self.player.pos.y - 25
            self.rect.topright = self.pos
        elif self.type_animation == 3:
            if self.rect.top <= -7:
                self.pos.x = self.player.pos.x + 20
                self.pos.y = self.player.pos.y + self.y_plus
                self.rect.midbottom = self.pos
        elif self.type_animation == 4:
            self.pos.x = self.player.pos.x - 5
            self.pos.y = self.player.pos.y + 15
            self.rect.midbottom = self.pos

        if self.animation:
            self.__animation()

    def __animation(self):
        if int(self.index) == 6:
            self.counter += 1
            if self.counter == 120:
                self.index += 1
                self.counter = 0
        else:
            self.index += 0.25
        if self.index >= len(self.lightning_animation):
            self.index = 0
        self.image = self.lightning_animation[int(self.index)]
