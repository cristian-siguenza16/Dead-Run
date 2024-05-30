import pygame

ASSET_WIDTH = 850
ASSET_HEIGHT = 500
SCREEN_WIDTH = 1000
SCREEN_HEIGHT = 700


class Playground:
    def __init__(self):
        self.add_background = False
        self.speed = 0
        self.mov_backgrounds = False
        self.background_surf_list = []
        self.background_rect_list = []
        self.surfaces = []
        self.rects = []
        self.positions = []
        self.background_surfaces = []
        self.bsrufaces_rects = []
        self.back_positions = []

    def get_first_and_last_position(self):
        return self.positions[0].x, self.positions[len(self.positions) - 1].x

    def update_background(self, delta_time: float):
        for i, vrect in enumerate(self.bsrufaces_rects):
            self.back_positions[i].x -= self.speed * delta_time
            vrect.x = int(self.back_positions[i].x)

    def build_assets(self, names: list[str], quantity: int, height: int):
        for i in range(0, quantity):
            var_surf = []
            for name in names:
                surf = pygame.image.load(name).convert_alpha()
                surf = pygame.transform.scale(surf, (ASSET_WIDTH, height))
                var_surf.append(surf)
            if len(var_surf) > 1:
                self.surfaces.append(var_surf)
            else:
                self.surfaces.append(var_surf[0])
            self.rects.append(var_surf[0].get_rect())
            self.positions.append(pygame.math.Vector2(0, 0))

    def build_background_assets(self, names: list[str]):
        var_surf = []
        for name in names:
            surf = pygame.image.load(name).convert_alpha()
            surf = pygame.transform.scale(surf, (SCREEN_WIDTH, SCREEN_HEIGHT))
            var_surf.append(surf)
        if len(var_surf) > 1:
            self.background_surfaces.append(var_surf)
        else:
            self.background_surfaces.append(var_surf[0])
        self.bsrufaces_rects.append(var_surf[0].get_rect())
        self.back_positions.append(pygame.math.Vector2(0, 0))
