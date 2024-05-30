import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.width = 0
        self.height = 0
        self.speed = 0
        self.tile_number = 0
        self.killable = False
        self.move = False
        self.move_y = False
        self.move_direction = 0
        self.move_counter = 0
        self.move_range = 0
        self.surf = None
        # Ya lo demas no tiene chiste
        self.pos = pygame.math.Vector2(0, 0)
        self.rect = None

    def update(self, delta_time: int):
        self.pos.x -= self.speed * delta_time
        self.rect.x = self.pos.x
        if self.move:
            self.pos.x += self.move_direction * self.speed * delta_time
            self.move_counter += 1
            if abs(self.move_counter) > self.move_range / self.speed:
                self.move_direction *= -1
                self.move_counter *= -1
        if self.move_y:
            self.pos.y += 10
            self.rect.y = self.pos.y
            if self.pos.y > 800:
                self.kill()

        if self.rect.right < -83:
            self.kill()
