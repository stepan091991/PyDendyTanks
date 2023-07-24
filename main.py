import os
import sys
import pygame
from pygame.locals import *
import classes
import map
import load_textures
pygame.init()
fps = 60
fpsClock = pygame.time.Clock()
width, height = 768, 832
LIGHT_BLUE = (64, 128, 255)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
image1 = pygame.image.load(os.path.join("textures/blocks", 'block_5.png')).convert()
all_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
leaves_block = pygame.sprite.Group()
created_map = map.create_map()
for block in created_map:
    if block.block_type == 11:
        leaves_block.add(block)
    else:
        blocks.add(block)
Player = load_textures.load_player()
all_sprites.add(Player)
# Game loop.
while True:
    if Player.bullet is not None:
        bullets.add(Player.bullet)
    screen.fill((255, 255, 255))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.spawn_bullet()
    Player.update(blocks)
    blocks.draw(screen)
    all_sprites.draw(screen)
    pygame.draw.rect(screen,WHITE,Player.rect,1)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.left_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.right_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.up_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.down_rect, 2)
    for bullet in bullets:
        pygame.draw.rect(screen, LIGHT_BLUE, bullet.rect, 2)
    bullets.update(blocks)
    bullets.draw(screen)
    leaves_block.update()
    leaves_block.draw(screen)
    for block in blocks:
        if block.block_type != 0:
            pygame.draw.rect(screen, WHITE, block.left_rect, 1)
            pygame.draw.rect(screen, WHITE, block.right_rect, 1)
            pygame.draw.rect(screen, WHITE, block.up_rect, 1)
            pygame.draw.rect(screen, WHITE, block.down_rect, 1)
    pygame.display.flip()
    fpsClock.tick(fps)
