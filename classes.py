import pygame
import os
import random
sound_setting = 1
pygame.mixer.init()
pygame.mixer.music.load("sounds/move.mp3")
shoot_sound = pygame.mixer.Sound("sounds/shoot.mp3")
death_sound = pygame.mixer.Sound("sounds/death.mp3")
pygame.mixer.music.play(-1)
pygame.mixer.music.set_volume(sound_setting)
left_image = pygame.image.load("textures/entity/bullet_4.png")
right_image = pygame.image.load("textures/entity/bullet_2.png")
up_image = pygame.image.load("textures/entity/bullet_1.png")
down_image = pygame.image.load("textures/entity/bullet_3.png")
class Block(pygame.sprite.Sprite):
    def __init__(self, texture, x, y, block_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.image.set_colorkey((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.width = 64
        self.rect.height = 64
        self.rect.center = (64 / 2, 64 / 2)
        self.rect.x = x
        self.rect.y = y
        self.block_type = block_type
        self.left_rect = (self.rect.x, self.rect.y, 1, 64)
        self.right_rect = (self.rect.x + 63, self.rect.y, 1, 64)
        self.up_rect = (self.rect.x, self.rect.y, 64, 1)
        self.down_rect = (self.rect.x, self.rect.y + 63, 64, 1)
        self.width = 64
        self.height = 64
        self.spawn_collide = []

class Player(pygame.sprite.Sprite):
    def __init__(self, texture_up, texture_up_1, texture_left, texture_left_1, texture_down, texture_down_1,
                 texture_right, texture_right_1, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture_up
        self.texture_up = texture_up
        self.texture_up.set_colorkey((0, 0, 1))
        self.texture_up_1 = texture_up_1
        self.texture_up_1.set_colorkey((0, 0, 1))
        self.texture_left = texture_left
        self.texture_left.set_colorkey((0, 0, 1))
        self.texture_left_1 = texture_left_1
        self.texture_left_1.set_colorkey((0, 0, 1))
        self.texture_down = texture_down
        self.texture_down.set_colorkey((0, 0, 1))
        self.texture_down_1 = texture_down_1
        self.texture_down_1.set_colorkey((0, 0, 1))
        self.texture_right = texture_right
        self.texture_right.set_colorkey((0, 0, 1))
        self.texture_right_1 = texture_right_1
        self.texture_right_1.set_colorkey((0, 0, 1))
        self.rect = self.image.get_rect()
        self.rect.center = (52 / 2, 52 / 2)
        self.rect.x = x
        self.rect.y = y
        self.speed = 2
        self.left_rect = (self.rect.x, self.rect.y,10,52)
        self.right_rect = (self.rect.x + 42, self.rect.y,10,52)
        self.up_rect = (self.rect.x, self.rect.y, 52, 10)
        self.down_rect = (self.rect.x, self.rect.y + 42, 52, 52 / 4)
        self.bullet = None
        self.last = 0
        self.cooldown = 150
        self.now = 0
        self.entity_type = "player"
        self.health = 3
        self.killed_coint = 0
        self.level = 1

    def update(self, blocks, entitys):
        self.now = pygame.time.get_ticks()
        if self.now - self.last >= self.cooldown:
            self.last = self.now
            self.animation()
        collide_fase = []
        keystate = pygame.key.get_pressed()
        for block in blocks:
            if self.rect.colliderect(block.rect):
                if block.block_type == 8:
                    self.speed = 7
                    break
                else:
                    self.speed = 2
            if block.block_type != 0 and block.block_type != 8 and block.block_type != 13:
                if block.rect.colliderect(self.left_rect):
                    collide_fase.append("left")
                if block.rect.colliderect(self.right_rect):
                    collide_fase.append("right")
                if block.rect.colliderect(self.up_rect):
                    collide_fase.append("up")
                if block.rect.colliderect(self.down_rect):
                    collide_fase.append("down")
        for entity in entitys:
            if entity != self:
                if entity.rect.colliderect(self.left_rect):
                    collide_fase.append("left")
                if entity.rect.colliderect(self.right_rect):
                    collide_fase.append("right")
                if entity.rect.colliderect(self.up_rect):
                    collide_fase.append("up")
                if entity.rect.colliderect(self.down_rect):
                    collide_fase.append("down")
        if keystate[pygame.K_LEFT] and self.rect.x > 0 and not "left" in collide_fase:
            if self.image != self.texture_left:
                self.image = self.texture_left_1
            self.rect.x -= self.speed
            pygame.mixer.music.set_volume(sound_setting)
        elif keystate[pygame.K_RIGHT] and self.rect.x < 716 and not "right" in collide_fase:
            if self.image != self.texture_right:
                self.image = self.texture_right_1
            self.rect.x += self.speed
            pygame.mixer.music.set_volume(sound_setting)
        elif keystate[pygame.K_UP] and self.rect.y > 0 and not "up" in collide_fase:
            if self.image != self.texture_up:
                self.image = self.texture_up_1
            self.rect.y -= self.speed
            pygame.mixer.music.set_volume(sound_setting)
        elif keystate[pygame.K_DOWN] and self.rect.y < 780 and not "down" in collide_fase:
            if self.image != self.texture_down:
                self.image = self.texture_down_1
            self.rect.y += self.speed
            pygame.mixer.music.set_volume(sound_setting)
        else:
            if self.image == self.texture_left_1:
                self.image = self.texture_left
            if self.image == self.texture_right_1:
                self.image = self.texture_right
            if self.image == self.texture_up_1:
                self.image = self.texture_up
            if self.image == self.texture_down_1:
                self.image = self.texture_down
            pygame.mixer.music.set_volume(0)
        collide_fase.clear()
        self.left_rect = (self.rect.x, self.rect.y + 5, 10, 42)
        self.right_rect = (self.rect.x + 42, self.rect.y + 5, 10, 42)
        self.up_rect = (self.rect.x + 5, self.rect.y, 42, 10)
        self.down_rect = (self.rect.x + 5, self.rect.y + 42, 42, 10)
    def spawn_bullet(self):
        if not self.bullet:
            if self.image == self.texture_left or self.image == self.texture_left_1:
                self.bullet = Bullet(self, self.rect.x + 10, self.rect.y + 24)
            if self.image == self.texture_right or self.image == self.texture_right_1:
                self.bullet = Bullet(self, self.rect.x + 40, self.rect.y + 24)
            if self.image == self.texture_down or self.image == self.texture_down_1:
                self.bullet = Bullet(self, self.rect.x + 23, self.rect.y + 40)
            if self.image == self.texture_up or self.image == self.texture_up_1:
                self.bullet = Bullet(self, self.rect.x + 3, self.rect.y + 10)
            shoot_sound.play(loops=0, maxtime=0, fade_ms=0)

    def animation(self):
        if self.image == self.texture_left:
            self.image = self.texture_left_1
        elif self.image == self.texture_left_1:
            self.image = self.texture_left
        if self.image == self.texture_right:
            self.image = self.texture_right_1
        elif self.image == self.texture_right_1:
            self.image = self.texture_right
        if self.image == self.texture_up:
            self.image = self.texture_up_1
        elif self.image == self.texture_up_1:
            self.image = self.texture_up
        if self.image == self.texture_down:
            self.image = self.texture_down_1
        elif self.image == self.texture_down_1:
            self.image = self.texture_down
    def damaget(self,all_sprites,Bots,Entitys,boom_sprites):
        self.health -= 1

class Bullet(pygame.sprite.Sprite):
    def __init__(self,owner,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.left_image = left_image
        self.right_image = right_image
        self.up_image = up_image
        self.down_image = down_image
        self.image = left_image
        self.speed = 5
        self.rect = self.image.get_rect()
        self.orientation = "up"
        self.orientation = None
        if self.owner.image == self.owner.texture_up or self.owner.image == self.owner.texture_up_1:
            self.orientation = "up"
            self.image = self.up_image
            self.rect = self.image.get_rect()
            self.rect.center = (1,1)
            self.rect.x = x + 52/2 - 6
            self.rect.y = y
        elif self.owner.image == self.owner.texture_left or self.owner.image == self.owner.texture_left_1:
            self.orientation = "left"
            self.image = self.left_image
            self.rect = self.image.get_rect()
            self.rect.center = (12 / 2, 16 / 2)
            self.rect.x = x
            self.rect.y = y
        elif self.owner.image == self.owner.texture_right or self.owner.image == self.owner.texture_right_1:
            self.orientation = "right"
            self.image = self.right_image
            self.rect = self.image.get_rect()
            self.rect.center = (12 / 2, 16 / 2)
            self.rect.x = x
            self.rect.y = y
        elif self.owner.image == self.owner.texture_down or self.owner.image == self.owner.texture_down_1:
            self.orientation = "down"
            self.image = self.down_image
            self.rect = self.image.get_rect()
            self.rect.center = (4 / 2, 6 / 2)
            self.rect.x = x
            self.rect.y = y
    def update(self,blocks,bullets,Entitys,all_sprites,Bots,boom_sprites):
        if self.orientation == "up" and self.orientation:
            self.rect.y -= self.speed
        if self.orientation == "left" and self.orientation:
            self.rect.x -= self.speed
        if self.orientation == "right" and self.orientation:
            self.rect.x += self.speed
        if self.orientation == "down" and self.orientation:
            self.rect.y += self.speed
        for block in blocks:
            if self.rect.colliderect(block.rect) and block.block_type == 9:
                block.remove(blocks)
            if block.block_type == 1:
                if block.width == 0 or block.height == 0:
                    block.block_type = 0
                if self.rect.colliderect(block.right_rect):
                    block.width -= 16
                    block.image = block.image.subsurface((0, 0, block.width, block.height))
                    block.rect.width -= 16
                    block.image.set_colorkey((255,255,255))
                    block.right_rect = (block.right_rect[0] - 16, block.rect.y, 1, block.height)
                    block.up_rect = (block.rect.x, block.rect.y, block.width, 1)
                    block.down_rect = (block.rect.x, block.rect.y + block.height - 1, block.width, 1)
                    bullets.remove(self)
                    bullets.remove(bullets)
                    self.owner.bullet = None
                if self.rect.colliderect(block.left_rect):
                    block.width -= 16
                    block.image = block.image.subsurface((0, 0, block.width, block.height))
                    block.rect.width -= 16
                    block.image.set_colorkey((255,255,255))
                    block.left_rect = (block.left_rect[0] + 16, block.rect.y, 1, block.height)
                    block.up_rect = (block.rect.x + 16, block.rect.y, block.width, 1)
                    block.down_rect = (block.rect.x + 16, block.rect.y + block.height - 1, block.width, 1)
                    block.rect.x += 16
                    bullets.remove(self)
                    bullets.remove(bullets)
                    self.owner.bullet = None
                if self.rect.colliderect(block.down_rect):
                    block.height -= 16
                    block.rect.height -= 16
                    block.image = block.image.subsurface((0, 0, block.width, block.height))
                    block.image.set_colorkey((255,255,255))
                    block.right_rect = (block.right_rect[0], block.right_rect[1], 1, block.height)
                    block.left_rect = (block.left_rect[0], block.left_rect[1], 1, block.height)
                    block.down_rect = (block.down_rect[0], block.down_rect[1] - 16, block.width, 1)
                    bullets.remove(self)
                    bullets.remove(bullets)
                    self.owner.bullet = None
                if self.rect.colliderect(block.up_rect):
                    block.height -= 16
                    block.rect.height -= 16
                    block.image = block.image.subsurface((0, 0, block.width, block.height))
                    block.image.set_colorkey((255,255,255))
                    block.right_rect = (block.right_rect[0], block.right_rect[1] + 16, 1, block.height)
                    block.left_rect = (block.left_rect[0], block.left_rect[1] + 16, 1, block.height)
                    block.up_rect = (block.rect.x, block.rect.y + 16, block.width, 1)
                    block.rect.y += 16
                    bullets.remove(bullets)
                    self.owner.bullet = None
                if self.rect.x < 0 or self.rect.x > 768 or self.rect.y < 0 or self.rect.y > 832:
                    bullets.remove(bullets)
                    self.owner.bullet = None
            elif block.block_type != 1 and block.block_type != 0 and block.block_type != 7 and block.block_type != 8 and block.block_type != 11 and block.block_type != 13:
                if self.rect.colliderect(block.rect):
                    bullets.remove(bullets)
                    self.owner.bullet = None
        for entity in Entitys:
            if self.rect.colliderect(entity):
                if self.owner != entity:
                    if self.owner.entity_type != entity.entity_type:
                        bullets.remove(bullets)
                        self.owner.bullet = None
                        if self.owner.entity_type == "player":
                            self.owner.killed_coint += 1
                        entity.damaget(all_sprites,Bots,Entitys,boom_sprites)
bot_texture_left = pygame.image.load("textures/entity/Enemy/2.png")
bot_texture_right = pygame.image.load("textures/entity/Enemy/4.png")
bot_texture_up = pygame.image.load("textures/entity/Enemy/1.png")
bot_texture_down = pygame.image.load("textures/entity/Enemy/3.png")

bot_texture_left_1 = pygame.image.load("textures/entity/Enemy/2_1.png")
bot_texture_right_1 = pygame.image.load("textures/entity/Enemy/4_1.png")
bot_texture_up_1 = pygame.image.load("textures/entity/Enemy/1_1.png")
bot_texture_down_1 = pygame.image.load("textures/entity/Enemy/3_1.png")
bot_killed_texture = pygame.image.load("textures/entity/Enemy/5.png")
class Bot(pygame.sprite.Sprite):
    def __init__(self, types, blocks,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.last_3 = pygame.time.get_ticks()
        self.cooldown = 300
        self.entity_type = "enemy"
        self.texture_left = bot_texture_left
        self.texture_left.set_colorkey((0, 0, 1))
        self.texture_right = bot_texture_right
        self.texture_right.set_colorkey((0, 0, 1))
        self.texture_up = bot_texture_up
        self.texture_up.set_colorkey((0, 0, 1))
        self.texture_down = bot_texture_down
        self.texture_down.set_colorkey((0, 0, 1))
        self.texture_left_1 = bot_texture_left_1
        self.texture_left_1.set_colorkey((0, 0, 1))
        self.texture_right_1 = bot_texture_right_1
        self.texture_right_1.set_colorkey((0, 0, 1))
        self.texture_up_1 = bot_texture_up_1
        self.texture_up_1.set_colorkey((0, 0, 1))
        self.texture_down_1 = bot_texture_down_1
        self.texture_down_1.set_colorkey((0, 0, 1))
        self.blocks = blocks
        self.types = types
        self.image = self.texture_down
        self.rect = self.image.get_rect()
        self.speed = 2
        self.left_rect = (self.rect.x, self.rect.y,10,52)
        self.right_rect = (self.rect.x + 42, self.rect.y,10,52)
        self.up_rect = (self.rect.x, self.rect.y, 52, 10)
        self.down_rect = (self.rect.x, self.rect.y + 42, 52, 52 / 4)
        self.bullet = None
        self.last = 0
        self.last_1 = 0
        self.shoot_cooldown = random.randint(300,700)
        self.animation_cooldown = 150
        self.rect.x = x
        self.rect.y = y
        self.now = 0
        self.rotate = "up"
        self.randim_id = random.randint(0,999)
    def update(self,blocks,entitys,boom_sprites):
        self.now = pygame.time.get_ticks()
        if self.now - self.last >= self.animation_cooldown:
            self.last = self.now
            self.animation()
        if self.now - self.last_1 >= self.shoot_cooldown:
            self.last_1 = self.now
            self.shoot()
        collide_fase = []
        score = random.randint(1,1000)
        if score == 0 or 1 < score < 998:
            for block in blocks:
                if self.rect.colliderect(block.rect):
                    if block.block_type == 8:
                        self.speed = 7
                        break
                    else:
                        self.speed = 2
                if block.block_type != 0 and block.block_type != 8 and block.block_type != 13:
                    if block.rect.colliderect(self.left_rect):
                        collide_fase.append("left")
                    if block.rect.colliderect(self.right_rect):
                        collide_fase.append("right")
                    if block.rect.colliderect(self.up_rect):
                        collide_fase.append("up")
                    if block.rect.colliderect(self.down_rect):
                        collide_fase.append("down")
            for entity in entitys:
                if entity != self:
                    if entity.rect.colliderect(self.left_rect):
                        collide_fase.append("left")
                    if entity.rect.colliderect(self.right_rect):
                        collide_fase.append("right")
                    if entity.rect.colliderect(self.up_rect):
                        collide_fase.append("up")
                    if entity.rect.colliderect(self.down_rect):
                        collide_fase.append("down")
            if not "left" in collide_fase and self.rect.x > 0 and self.rotate == "left":
                self.rect.x -= self.speed
            elif not "right" in collide_fase and self.rect.x < 716 and self.rotate == "right":
                self.rect.x += self.speed
            elif not "up" in collide_fase and self.rect.y > 0 and self.rotate == "up":
                self.rect.y -= self.speed
            elif not "down" in collide_fase and self.rect.y < 780 and self.rotate == "down":
                self.rect.y += self.speed
            else:
                score = random.randint(1,4)
                if score == 1:
                    self.rotate = "left"
                    self.image = self.texture_left
                if score == 2:
                    self.rotate = "right"
                    self.image = self.texture_right
                if score == 3:
                    self.rotate = "up"
                    self.image = self.texture_up
                if score == 4:
                    self.rotate = "down"
                    self.image = self.texture_down
        else:
            score = random.randint(1, 4)
            if score == 1:
                self.rotate = "left"
                self.image = self.texture_left
            if score == 2:
                self.rotate = "right"
                self.image = self.texture_right
            if score == 3:
                self.rotate = "up"
                self.image = self.texture_up
            if score == 4:
                self.rotate = "down"
                self.image = self.texture_down
        collide_fase.clear()
        self.left_rect = (self.rect.x, self.rect.y + 5, 10, 42)
        self.right_rect = (self.rect.x + 42, self.rect.y + 5, 10, 42)
        self.up_rect = (self.rect.x + 5, self.rect.y, 42, 10)
        self.down_rect = (self.rect.x + 5, self.rect.y + 42, 42, 10)
    def shoot(self):
        if not self.bullet:
            if self.image == self.texture_left or self.image == self.texture_left_1:
                self.bullet = Bullet(self, self.rect.x + 10, self.rect.y + 24)
            if self.image == self.texture_right or self.image == self.texture_right_1:
                self.bullet = Bullet(self, self.rect.x + 40, self.rect.y + 24)
            if self.image == self.texture_down or self.image == self.texture_down_1:
                self.bullet = Bullet(self, self.rect.x + 23, self.rect.y + 40)
            if self.image == self.texture_up or self.image == self.texture_up_1:
                self.bullet = Bullet(self, self.rect.x + 3, self.rect.y + 10)
            shoot_sound.play(loops=0, maxtime=0, fade_ms=0)
    def animation(self):
        if self.image == self.texture_left:
            self.image = self.texture_left_1
        elif self.image == self.texture_left_1:
            self.image = self.texture_left

        if self.image == self.texture_right:
            self.image = self.texture_right_1
        elif self.image == self.texture_right_1:
            self.image = self.texture_right

        if self.image == self.texture_up:
            self.image = self.texture_up_1
        elif self.image == self.texture_up_1:
            self.image = self.texture_up

        if self.image == self.texture_down:
            self.image = self.texture_down_1
        elif self.image == self.texture_down_1:
            self.image = self.texture_down
    def damaget(self,all_sprites,Bots,Entitys,boom_sprites):
        boom = Boom(self.rect.x,self.rect.y)
        boom_sprites.add(boom)
        self.remove(all_sprites)
        Bots.remove(self)
        Entitys.remove(self)
boom_texture = pygame.image.load("textures/entity/Enemy/5.png")
class Boom(pygame.sprite.Sprite):
    def __init__(self, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.boom_texture = boom_texture
        self.boom_texture.set_colorkey((0, 0, 1))
        self.image = self.boom_texture
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.last = pygame.time.get_ticks()
        self.cooldown = 600
        death_sound.play(loops=0, maxtime=0, fade_ms=0)
    def update(self,boom_sprites):
        now = pygame.time.get_ticks()
        if now - self.last >= self.cooldown:
            self.last = now
            boom_sprites.remove(self)
life_texture = pygame.image.load("textures/GUI/life.png")
life_1_texture = pygame.image.load("textures/GUI/life_1.png")
life_2_texture = pygame.image.load("textures/GUI/life_2.png")
class Gui(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.life_texture = life_texture
        self.life_texture.set_colorkey((0, 0, 1))
        self.life_1_texture = life_1_texture
        self.life_1_texture.set_colorkey((0, 0, 1))
        self.life_2_texture = life_2_texture
        self.life_2_texture.set_colorkey((0, 0, 1))
        self.image = self.life_2_texture
        self.rect = self.image.get_rect()
        self.rect.x = 670
        self.rect.y = 0
    def update(self,player,gui,GAME):
        if player.health == 3:
            self.image = life_2_texture
        if player.health == 2:
            self.image = life_1_texture
        if player.health == 1:
            self.image = life_texture
        if player.health < 1:
            self.remove(gui)
def off_sound():
    pygame.mixer.music.set_volume(0)
def set_sound_setting(sound_setting_self):
    global sound_setting
    sound_setting = sound_setting_self