import pygame
import os

left_image = pygame.image.load("textures/entity/bullet_4.png")
right_image = pygame.image.load("textures/entity/bullet_2.png")
up_image = pygame.image.load("textures/entity/bullet_1.png")
down_image = pygame.image.load("textures/entity/bullet_3.png")
class Block(pygame.sprite.Sprite):
    def __init__(self, texture, x, y, block_type):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture
        self.rect = self.image.get_rect()
        self.rect.center = (64 / 2, 64 / 2)
        self.rect.x = x
        self.rect.y = y
        self.block_type = block_type
        self.left_rect = (self.rect.x, self.rect.y, 5, 64)
        self.right_rect = (self.rect.x + 59, self.rect.y, 5, 64)
        self.up_rect = (self.rect.x, self.rect.y, 64, 5)
        self.down_rect = (self.rect.x, self.rect.y + 59, 64, 5)

class Player(pygame.sprite.Sprite):
    def __init__(self, texture_up, texture_up_1, texture_left, texture_left_1, texture_down, texture_down_1,
                 texture_right, texture_right_1, x, y):
        pygame.sprite.Sprite.__init__(self)
        self.image = texture_up
        self.texture_up = texture_up
        self.texture_up_1 = texture_up_1
        self.texture_left = texture_left
        self.texture_left_1 = texture_left_1
        self.texture_down = texture_down
        self.texture_down_1 = texture_down_1
        self.texture_right = texture_right
        self.texture_right_1 = texture_right_1
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

    def update(self, blocks):
        collide_fase = []
        keystate = pygame.key.get_pressed()
        for block in blocks:
            if block.block_type != 0 and block.block_type != 11:
                if block.rect.colliderect(self.left_rect):
                    collide_fase.append("left")
                if block.rect.colliderect(self.right_rect):
                    collide_fase.append("right")
                if block.rect.colliderect(self.up_rect):
                    collide_fase.append("up")
                if block.rect.colliderect(self.down_rect):
                    collide_fase.append("down")
        if keystate[pygame.K_LEFT] and self.rect.x > 0 and not "left" in collide_fase:
            if self.image != self.texture_left:
                self.image = self.texture_left
            self.rect.x -= self.speed
        elif keystate[pygame.K_RIGHT] and self.rect.x < 716 and not "right" in collide_fase:
            if self.image != self.texture_right:
                self.image = self.texture_right
            self.rect.x += self.speed
        elif keystate[pygame.K_UP] and self.rect.y > 0 and not "up" in collide_fase:
            if self.image != self.texture_up:
                self.image = self.texture_up
            self.rect.y -= self.speed
        elif keystate[pygame.K_DOWN] and self.rect.y < 780 and not "down" in collide_fase:
            if self.image != self.texture_down:
                self.image = self.texture_down
            self.rect.y += self.speed
        collide_fase.clear()
        self.left_rect = (self.rect.x, self.rect.y + 5, 10, 42)
        self.right_rect = (self.rect.x + 42, self.rect.y + 5, 10, 42)
        self.up_rect = (self.rect.x + 5, self.rect.y, 42, 10)
        self.down_rect = (self.rect.x + 5, self.rect.y + 42, 42, 10)
    def spawn_bullet(self):
        self.bullet = Bullet(self, self.rect.x, self.rect.y)
        print("yes")

class Bullet(pygame.sprite.Sprite):
    def __init__(self,owner,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.owner = owner
        self.left_image = left_image
        self.right_image = right_image
        self.up_image = up_image
        self.down_image = down_image
        self.speed = 5
        if self.owner.image == self.owner.texture_up:
            self.orientation = "up"
            self.image = self.up_image
            self.rect = self.image.get_rect()
            self.rect.center = (1,1)
            self.rect.x = x + 52/2 - 6
            self.rect.y = y
        if self.owner.image == self.owner.texture_left:
            self.orientation = "left"
            self.image = self.left_image
            self.rect = self.image.get_rect()
            self.rect.center = (12 / 2, 16 / 2)
            self.rect.x = x
            self.rect.y = y
        if self.owner.image == self.owner.texture_right:
            self.orientation = "right"
            self.image = self.right_image
            self.rect = self.image.get_rect()
            self.rect.center = (12 / 2, 16 / 2)
            self.rect.x = x
            self.rect.y = y
        if self.owner.image == self.owner.texture_down:
            self.orientation = "down"
            self.image = self.down_image
            self.rect = self.image.get_rect()
            self.rect.center = (4 / 2, 6 / 2)
            self.rect.x = x
            self.rect.y = y
    def update(self,blocks):
        if self.orientation == "up":
            self.rect.y -= self.speed
        if self.orientation == "left":
            self.rect.x -= self.speed
        if self.orientation == "right":
            self.rect.x += self.speed
        if self.orientation == "down":
            self.rect.y += self.speed
        for block in blocks:
            if block.block_type != 0 and block.block_type != 11:
                if block.rect.colliderect(self.rect):
                    self.rect.x = 2000