import os
import pygame
import classes
textures_dir = "textures/entity/Player"
def load_player():
    files = os.listdir(textures_dir)
    loaded_Player_files = {}
    index = 0
    for file in files:
        loaded_Player_files.update({index:pygame.image.load(os.path.join(textures_dir, file))})
        index += 1
    return classes.Player(loaded_Player_files.get(6),loaded_Player_files.get(7),loaded_Player_files.get(2),loaded_Player_files.get(3),loaded_Player_files.get(0),loaded_Player_files.get(1),loaded_Player_files.get(4),loaded_Player_files.get(5),256,702)