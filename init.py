import pygame, draw

def init():
    #init variables
    res = draw.getRes()
    
    #init
    pygame.init()
    print("pygame init")
    draw.setupScreen(res)
    draw.loadAssets()
    print("screen init")
