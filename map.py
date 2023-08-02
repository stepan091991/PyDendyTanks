import os
import pygame
import classes
map_1 = [0,13,0,1,0,0, 0, 0,0, 13, 0,0,1,
         0,0,0,1,0,0, 0, 0,0, 0, 0,0,1,
         1,1,0,1,1,0, 0, 0,0, 0, 0,0,1,
         1,0,0,0,1,0, 0, 0,0, 1, 0,0,1,
         1,0,1,1,1,0, 0, 0,0, 0, 0,0,1,
         1,0,0,1,0,0, 0, 0,0, 3, 0,0,1,
         1,1,0,1,0,0, 0, 0,0, 0, 0,0,1,
         1,0,0,0,0,0, 0, 0,0,7,7,0,1,
         1,0,0,8,0,0, 0, 0,0,7,7,0,1,
         1,0,0,8,0,0, 0, 0,0,7,7,0,1,
         1,0,0,8,0,11, 0, 0,0, 0, 0,0,1,
         1,0,0,0,0,1, 1, 1,0, 0, 0,0,1,
         1,1,1,1,1,1, 9,1,1,1, 1, 1,1]
textures_dir = "textures/blocks"
loaded_files = {}
files = os.listdir(textures_dir)
index = 0
for file in files:
    loaded_files.update({index:pygame.image.load(os.path.join(textures_dir, file))})
    print(file)
    index += 1

def create_map():
    maxX = 768
    maxY = 832
    x = 0
    y = 0
    created_map = []
    for block in map_1:
        created_map.append(classes.Block(loaded_files.get(block),x,y,block))
        if x == maxX:
            x = 0
            y += 64
        else:
            x += 64
    print(created_map)
    return created_map