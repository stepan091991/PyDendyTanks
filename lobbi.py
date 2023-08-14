import os
import sys
import map
import main
import pygame
import random
import pygame_widgets
from pygame_widgets.dropdown import Dropdown

width, height = 768, 832
FPS = 30

# Задаем цвета
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Создаем игру и окно
pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("My Game")
clock = pygame.time.Clock()
pygame.font.init()
my_font = pygame.font.Font('font/Nineteen Eighty Seven.otf', 40)
files = os.listdir("maps/")
valies = []
for i in range(len(files)):
    valies.append(i)

# Цикл игры
running = True
dropdown = Dropdown(
    screen, 120, 300, 200, 35, name='Select map',choices=files,borderRadius=3,borderColor=WHITE, values=files, direction='down', textHAlign='left')
while running:
    screen.fill(BLACK)
    pygame.display.set_caption("DendyTankGamePyLauncher by Stepan4ek")
    # Держим цикл на правильной скорости
    # Ввод процесса (события)
    events = pygame.event.get()
    for event in events:
        # check for closing window
        if event.type == pygame.QUIT:
            if dropdown.getSelected():
                print(main.Game(Debug=False,map_text=open(f"maps/{dropdown.getSelected()}","r")))

    # Рендеринг
    pygame_widgets.update(events)
    text_surface = my_font.render(
        f"Танки Python", False, (255, 255, 255))
    screen.blit(text_surface, (5, 5))
    pygame.display.flip()
    clock.tick(FPS)
pygame.quit()