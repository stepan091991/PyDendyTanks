import os
import pygame
import classes
import json
def create_map(map_file):
    import classes
    textures_dir = "textures/blocks"
    loaded_files = {}
    files = os.listdir(textures_dir)
    index = 0
    for file in files:
        print(file)
        loaded_files.update({index: pygame.image.load(os.path.join(textures_dir, file)).convert()})
        index += 1
    map_1 = json.load(map_file)["map"]
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
    return created_map