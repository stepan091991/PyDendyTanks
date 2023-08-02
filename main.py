import os
import random
import sys
import pygame
from pygame.locals import *
import classes
import map
import load_textures
Bot_spawn_coint = 2
GAME = True
bots_off = 0
Bots = []
Entitys = []
Spawns = []
pygame.init()
pygame.font.init()
my_font = pygame.font.SysFont('Comic Sans MS', 15)
fps = 60
fpsClock = pygame.time.Clock()
width, height = 768, 832
LIGHT_BLUE = (64, 128, 255)
WHITE = (255, 255, 255)
screen = pygame.display.set_mode((width, height))
image1 = pygame.image.load(os.path.join("textures/blocks", 'block_5.png')).convert()
all_sprites = pygame.sprite.Group()
boom_sprites = pygame.sprite.Group()
blocks = pygame.sprite.Group()
bullets = pygame.sprite.Group()
gui = pygame.sprite.Group()
leaves_block = pygame.sprite.Group()
created_map = map.create_map()
for block in created_map:
    if block.block_type == 13:
        Spawns.append(block)
for block in created_map:
    if block.block_type == 7:
        leaves_block.add(block)
    else:
        blocks.add(block)
Player = load_textures.load_player()
spawn_collide = []
for i in range(Bot_spawn_coint):
    spawn = random.choice(Spawns)
    for bot in Bots:
        if spawn.rect.colliderect(bot.rect):
            spawn.spawn_collide.append("bot")
    if not spawn.spawn_collide:
        Bot = classes.Bot("type", blocks, spawn.rect.x, spawn.rect.y)
        all_sprites.add(Bot)
        Entitys.append(Bot)
        Bots.append(Bot)
Entitys.append(Player)
all_sprites.add(Player)
gui_ = classes.Gui()
gui.add(gui_)
GERB = True
# Game loop.
while GAME:
    for block in blocks:
        if block.block_type == 9:
            GERB = True
    if Player.health < 1 or not GERB:
        GAME = False
    if len(Bots) == 0 and bots_off == 0:
        Player.level += 1
        if Player.level < 10:
            Bot_spawn_coint += 1
        elif Player.level >= 10 < 20:
            Bot_spawn_coint += 2
        elif Player.level >= 20:
            Bot_spawn_coint += 3
        bots_off = Bot_spawn_coint
    if bots_off != 0:
        spawn = random.choice(Spawns)
        for bot in Bots:
            if spawn.rect.colliderect(bot.rect):
                spawn.spawn_collide.append("bot")
        if not spawn.spawn_collide:
            Bot = classes.Bot("type", blocks, spawn.rect.x, spawn.rect.y)
            all_sprites.add(Bot)
            Entitys.append(Bot)
            Bots.append(Bot)
            bots_off -= 1
        spawn.spawn_collide = []
    if Player.bullet is not None:
        bullets.add(Player.bullet)
    for bot in Bots:
        if bot.bullet is not None:
            bullets.add(bot.bullet)
    screen.fill((0, 0, 0))
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                Player.spawn_bullet()
    Player.update(blocks,Entitys)
    blocks.draw(screen)
    all_sprites.draw(screen)
    pygame.draw.rect(screen,WHITE,Player.rect,1)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.left_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.right_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.up_rect, 2)
    pygame.draw.rect(screen, LIGHT_BLUE, Player.down_rect, 2)
    bullets.update(blocks,bullets,Entitys,all_sprites,Bots,boom_sprites)
    bullets.draw(screen)
    leaves_block.update()
    leaves_block.draw(screen)
    for block in blocks:
        if block.block_type != 0 and block.block_type != 7:
            #pygame.draw.rect(screen, LIGHT_BLUE, block.rect, 1)
            #pygame.draw.rect(screen, WHITE, block.left_rect, 1)
            #pygame.draw.rect(screen, WHITE, block.right_rect, 1)
            #pygame.draw.rect(screen, WHITE, block.up_rect, 1)
            #pygame.draw.rect(screen, WHITE, block.down_rect, 1)
            pass
    for bot in Bots:
        #pygame.draw.rect(screen, WHITE, bot.rect, 1)
        #pygame.draw.rect(screen, LIGHT_BLUE, bot.left_rect, 2)
        #pygame.draw.rect(screen, LIGHT_BLUE, bot.right_rect, 2)
        #pygame.draw.rect(screen, LIGHT_BLUE, bot.up_rect, 2)
        #pygame.draw.rect(screen, LIGHT_BLUE, bot.down_rect, 2)
        bot.update(blocks, Entitys,boom_sprites)
    boom_sprites.update(boom_sprites)
    boom_sprites.draw(screen)
    gui.update(Player,gui,GAME)
    gui.draw(screen)
    text_surface = my_font.render(f"Bullets:{len(bullets)} Enemys:{len(Bots)} Objects:{len(all_sprites) + len(blocks) + len(leaves_block)} ",False, (255, 255, 255))
    screen.blit(text_surface, (0, 0))
    text_surface = my_font.render(
        f"Fps:{fpsClock}", False, (255, 255, 255))
    screen.blit(text_surface, (0, 16))
    text_surface = my_font.render(
        f"Health:{Player.health} Killed:{Player.killed_coint} Level:{Player.level}", False, (255, 255, 255))
    screen.blit(text_surface, (0, 32))
    text_surface = my_font.render(
        f"Spawns:{len(Spawns)} Bots_out:{bots_off}", False, (255, 255, 255))
    screen.blit(text_surface, (0, 48))
    text_surface = my_font.render(
        f"Spawn1_info:{Spawns[0].spawn_collide}", False, (255, 255, 255))
    screen.blit(text_surface, (0, 64))
    text_surface = my_font.render(
        f"Spawn2_info:{Spawns[1].spawn_collide}", False, (255, 255, 255))
    screen.blit(text_surface, (0, 80))
    pygame.display.flip()
    fpsClock.tick(fps)
    GERB = False
print("ВЫ ПРОИГРАЛИ!")

