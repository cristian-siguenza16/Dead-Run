import random
from character import Character
from pygame import *
import pygame
from player_component import PlayerComponent
vec = pygame.math.Vector2  # for 2 dimensional


class Player(PlayerComponent):
    def __init__(self, character: Character, player_name: str, controls: dict[str, pygame.key]):
        self.character = character
        self.player_name = player_name
        # Gameplay
        self.pos = vec((50, 200))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.orientation = False
        self.jumping = False
        self.running = False
        self.sliding = False
        self.update_rect = False
        # Controls
        self.controls = controls
        self.lives: int = 3
        self.diamonds: int = 0
        self.points: int = 0
        self.is_alive = True
        self.shield = False
        self.with_effect = {'effect': False, 'effect_type': None, 'effect_value': None}
        self.finsihed = False   # Variable para verificar si ya finalizo

    def move(self):
        if self.character.upsidedown:
            self.acc = vec(0, -0.5)
        else:
            self.acc = vec(0, 0.5)
        pressed_keys = pygame.key.get_pressed()
        if pressed_keys[self.controls['left']] and not self.character.petrify:
            self.acc.x = -self.character.acc
            if not self.jumping and not self.sliding:
                self.character.running_left()
                self.running = True
                self.orientation = True

        elif pressed_keys[self.controls['right']] and not self.character.petrify:
            self.acc.x = self.character.acc
            if not self.jumping and not self.sliding:
                self.character.running_right()
                self.running = True
                self.orientation = False

        elif not pressed_keys[self.controls['left']] and not pressed_keys[self.controls['right']]:
            self.running = False

        self.acc.x += self.vel.x * self.character.friction
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        self.character.rect.midbottom = self.pos

    def update(self, platforms: pygame.sprite, kplatforms: pygame.sprite, speed: float):
        # Código Necesario para las colisiones con Plataformas de Pedro Es all el update
        self.pos.x -= speed
        # Verifica si se cayo (Fuera de la pantalla)
        if self.pos.y > 850 and not self.character.upsidedown:
            self.is_alive = False
            self.lives = 0
        elif self.pos.y < -150 and self.character.upsidedown:
            self.is_alive = False
            self.lives = 0

        if self.vel.y > 0 and not self.character.upsidedown:
            if self.jumping and not self.orientation:
                self.character.falling_down_right()
            elif self.jumping and self.orientation:
                self.character.falling_down_left()
        elif self.vel.y < 0 and self.character.upsidedown:
            if self.jumping and not self.orientation:
                self.character.falling_down_right()
            elif self.jumping and self.orientation:
                self.character.falling_down_left()
        # verificacion de las plataformas que se caen
        change = False
        for kentity in kplatforms:
            if self.character.rect.colliderect(kentity.rect):
                platforms.add(kentity)
                change = True
        # plataformas normales
        for entity in platforms:
            if self.character.rect.colliderect(entity.rect):
                if abs(entity.rect.left - self.character.rect.right) < 10 and self.vel.x >= 0:
                    self.pos.x += entity.rect.left - self.character.rect.right
                    self.vel.x = 0
                if abs(entity.rect.right - self.character.rect.left) < 10 and self.vel.x <= 0:
                    self.pos.x -= self.character.rect.left - entity.rect.right
                    self.vel.x = 0

                if self.vel.y > 0 and not self.character.upsidedown:
                    if abs(entity.rect.top - self.character.rect.bottom) <= 20:
                        self.pos.y = entity.rect.top + 1
                        self.vel.y = 0
                        self.jumping = False
                        self.sliding = False
                        if not self.running and self.orientation:
                            self.character.idle_left()
                            self.character.jump_start = True

                        elif not self.running and not self.orientation:
                            self.character.idle_right()
                            self.character.jump_start = True

                if self.vel.y < 0 and self.character.upsidedown:
                    if abs(entity.rect.bottom - self.character.rect.top) <= 20:
                        self.pos.y = self.character.rect.bottom + abs(entity.rect.bottom - self.character.rect.top)
                        self.vel.y = 0
                        self.jumping = False
                        self.sliding = False

                        if not self.running and self.orientation:
                            self.character.idle_left()
                            self.character.jump_start = True

                        elif not self.running and not self.orientation:
                            self.character.idle_right()
                            self.character.jump_start = True

                if self.vel.y < 0 and not self.character.upsidedown:
                    if abs(entity.rect.bottom - self.character.rect.top) <= 10:
                        self.pos.y += entity.rect.bottom - self.character.rect.top
                        self.vel.y = 0
                        self.jumping = False
                if self.vel.y > 0 and self.character.upsidedown:
                    if abs(entity.rect.top - self.character.rect.bottom) <= 10:
                        self.pos.y -= entity.rect.top - self.character.rect.bottom + 5
                        self.vel.y = 0
                        self.jumping = False
                # la plataforma se va para abajo
                if change and entity.killable:
                    if entity.move_counter == 12:
                        entity.move_y = True
                    else:
                        entity.move_counter += 1
                    platforms.remove(entity)

    def jump(self, jumping: event,  platforms: pygame.sprite, kplatforms: pygame.sprite):
        hits = pygame.sprite.spritecollide(self.character, platforms, False)
        hits1 = pygame.sprite.spritecollide(self.character, kplatforms, False)
        if jumping.type == pygame.KEYDOWN:
            if jumping.key == self.controls['jump'] and not self.character.petrify:
                if hits1:
                    hits = hits1
                if hits and not self.jumping and not self.orientation and not self.sliding and \
                        not self.character.upsidedown:
                    self.jumping = True
                    self.vel.y = self.character.jump_height
                    self.character.jump_right()
                elif hits and not self.jumping and self.orientation and not self.sliding and \
                        not self.character.upsidedown:
                    self.jumping = True
                    self.vel.y = self.character.jump_height
                    self.character.jump_left()
                elif hits and not self.jumping and not self.orientation and not self.sliding and \
                        self.character.upsidedown:
                    self.jumping = True
                    self.vel.y = -self.character.jump_height
                    self.character.jump_right()
                elif hits and not self.jumping and self.orientation and not self.sliding and \
                        self.character.upsidedown:
                    self.jumping = True
                    self.vel.y = -self.character.jump_height
                    self.character.jump_left()

    def cancel_jump(self, jumping: event):
        if jumping.type == pygame.KEYUP:
            if jumping.key == self.controls['jump']:
                if self.jumping:
                    if self.vel.y < -3 and not self.orientation and not self.character.upsidedown:
                        self.vel.y = -3
                        self.character.falling_down_right()
                    elif self.vel.y < -3 and self.orientation and not self.character.upsidedown:
                        self.vel.y = -3
                        self.character.falling_down_left()
                    elif self.vel.y > 3 and not self.orientation and self.character.upsidedown:
                        self.vel.y = 3
                        self.character.falling_down_right()
                    elif self.vel.y > 3 and self.orientation and self.character.upsidedown:
                        self.vel.y = 3
                        self.character.falling_down_left()

    def slide(self, platforms: pygame.sprite):
        pressed_keys = pygame.key.get_pressed()
        hits = pygame.sprite.spritecollide(self.character, platforms, False)
        if pressed_keys[self.controls['down']] and not self.character.petrify:
            self.update_rect = False
            if hits and not self.sliding and not self.orientation:
                if self.character.slide_distance <= 175:
                    self.sliding = True
                    self.vel.x = self.character.slide
                    self.pos += self.vel + 0.5 * self.acc
                    self.character.slide_distance += self.vel.x + 0.5 * self.acc.x
                    self.character.slide_right()
                    # print(self.character.slide_distance)
                if self.character.slide_distance >= 175 and self.sliding:
                    self.character.reset_rect()
                    self.update_rect = True
                    if self.character.upsidedown:
                        self.pos.y += 20

            elif hits and not self.sliding and self.orientation:
                if self.character.slide_distance <= 175:
                    self.sliding = True
                    self.vel.x = -self.character.slide
                    self.pos += self.vel + 0.5 * self.acc
                    self.character.slide_distance += abs(self.vel.x) + 0.5 * self.acc.x
                    self.character.slide_left()
                    # print(self.character.slide_distance)
                if self.character.slide_distance >= 175 and self.sliding:
                    self.character.reset_rect()
                    self.update_rect = True
                    if self.character.upsidedown:
                        self.pos.y += 20
                    # print("Llego al limite")

        elif self.character.slide_distance >= 175:
            self.character.slide_distance = 0
            self.update_rect = True
            # print("Llego al limite 2")

        if not pressed_keys[self.controls['down']] and not self.update_rect:
            self.character.reset_rect()
            self.character.slide_distance = 0
            self.update_rect = True
            if self.character.upsidedown:
                self.pos.y += 20
            # print("Entro")

    def get_reaction(self) -> dict:
        return {'none': None}

    def get_lives(self):
        return self.lives

    def get_diamonds(self):
        return self.diamonds

    def update_collision_items(self, world: pygame.sprite, players: list['Player']):
        items = world.get_items_group()
        item_hit = pygame.sprite.spritecollide(self.character, items, False)
        if item_hit:
            if pygame.sprite.collide_mask(self.character, item_hit[0]):
                react = item_hit[0].get_reaction()
                player = random.randint(0, len(players) - 1)
                item_hit[0].set_concrete_player_component(self)
                if "Diamond" in react:
                    self.diamonds = item_hit[0].get_diamonds()
                elif "Heart" in react:
                    if self.lives < 3:
                        self.lives = item_hit[0].get_lives()
                elif "Speed_up" in react:
                    self.character.acc += react['Speed_up']
                    world.add_effect_animation(0, self, 1)
                    self.with_effect = {'effect': True, 'effect_type': 'speed_up', 'effect_value': react['Speed_up']}
                elif "Speed_down" in react:
                    react['Player'] = player
                    world.add_effect_animation(0, players[react['Player']], 2)
                    players[react['Player']].character.acc += react['Speed_down']
                    players[react['Player']].with_effect = \
                        {'effect': True, 'effect_type': 'speed_down', 'effect_value': react['Speed_down']}
                elif "Lightning" in react:
                    react['Player'] = player
                    if players[react['Player']].is_alive:
                        players[react['Player']].lives -= react['Lightning']
                        players[react['Player']].with_effect = \
                            {'effect': True, 'effect_type': 'lightning', 'effect_value': None}
                        world.add_effect_animation(0, players[react['Player']], 3)
                        if players[react['Player']].lives <= 0:
                            players[react['Player']].is_alive = False
                        players[react['Player']].character.petrify = True
                item_hit[0].kill()

    def update_collision_obstacles(self, world: pygame.sprite, nplayer: int):
        obstacle = world.get_obstacle_group()
        obstacle_hits = pygame.sprite.spritecollide(self.character, obstacle, False)
        if obstacle_hits:
            if pygame.sprite.collide_mask(self.character, obstacle_hits[0]) and not self.shield:
                self.lives -= 1
                if self.lives <= 0:
                    self.is_alive = False
                world.add_effect_animation(nplayer, self, 4)
                self.shield = True
        portal = world.get_portal_group()
        portal_hits = pygame.sprite.spritecollide(self.character, portal, False)
        if portal_hits:
            if pygame.sprite.collide_mask(self.character, portal_hits[0]):
                if "next_portal" in portal_hits[0].next:
                    if self.character.upsidedown:
                        self.character.upsidedown = False
                    else:
                        self.character.upsidedown = True

                    self.pos.x = portal_hits[0].next['next_portal'][0]
                    self.pos.y = portal_hits[0].next['next_portal'][1]
                    self.character.rect.x = portal_hits[0].next['next_portal'][0]
                    self.character.rect.y = portal_hits[0].next['next_portal'][1]

    def check_final_portal(self, world: pygame.sprite, mundo: int):
        portal = world.final_portal
        if pygame.sprite.collide_mask(self.character, portal) and not self.finsihed:
            if self.character.rect.midbottom[0] >= portal.rect.midbottom[0] - 30 and mundo < 3:
                self.finsihed = True
                self.character.petrify = True
                self.points += world.get_winner_value
            if mundo == 3:
                self.finsihed = True
                self.character.petrify = True
                self.points += world.get_winner_value

    def reset_player(self, acc: float,  friction: float, sliding: float, jump_height: float):
        # Gameplay
        self.pos = vec((50, 200))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.orientation = False
        self.jumping = False
        self.running = False
        self.sliding = False
        self.update_rect = False
        self.lives: int = 3
        self.is_alive = True
        self.shield = False
        self.with_effect = {'effect': False, 'effect_type': None, 'effect_value': None}
        self.finsihed = False  # Variable para verificar si ya finalizo

        # REINICIAR CARACTERISTICAS DEL CHARACTER
        self.character.acc = acc
        self.character.friction = friction
        self.character.jump_height = jump_height
        self.character.slide = sliding
        self.character.slide_distance = 0
        self.character.upsidedown = False
        self.character.petrify = False
