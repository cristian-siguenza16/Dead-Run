import pygame


class Obstacle(pygame.sprite.Sprite):
    def __init__(self):
        super(Obstacle, self).__init__()
        self.widht = 0
        self.height = 0
        self.speed = 0
        self.move_y = False
        self.move_x = False
        self.animation = False
        self.image = None
        self.animation_list = []
        self.move_range = 0
        self.index = 0
        self.next = {}
        self.move_counter = 0
        self.move_direction = 0
        self.pos = pygame.math.Vector2(0, 0)
        self.rect = None
        self.mask = None

    def __animation_x(self):
        self.pos.x += self.move_direction * self.speed
        self.index += 0.15
        if self.index >= len(self.animation_list):
            self.index = 0
        self.image = self.animation_list[int(self.index)]
        self.mask = pygame.mask.from_surface(self.image)

    def __animation_y(self, delta_time: int):
        self.pos.y += self.move_direction * self.speed * delta_time
        self.move_counter += 1
        if abs(self.move_counter) > int(self.move_range / self.speed):
            self.move_direction *= -1
            self.move_counter *= -1
            self.index += 1
            if self.index >= len(self.animation_list):
                self.index = 0
            self.image = self.animation_list[self.index]
            self.mask = pygame.mask.from_surface(self.image)

    def update(self, delta_time: int):
        self.pos.x -= self.speed * delta_time
        self.rect.topleft = self.pos
        if 'next_portal' in self.next:
            self.next['next_portal'][0] -= self.speed * delta_time
        if self.animation:
            if self.move_y:
                self.__animation_y(delta_time)
            if self.move_x:
                self.__animation_x()
        self.mask = pygame.mask.from_surface(self.image)

        if self.rect.right < -50:
            self.kill()
