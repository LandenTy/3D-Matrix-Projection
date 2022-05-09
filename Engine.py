"""
Engine

Description:
"""
import pygame, sys
from math import sin, cos
pygame.init()

# WINDOW
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

#COLORS
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# VARIABLES
scale = 5
angle = 0
rotation = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]

# PROGRAM
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
window.fill(BLACK)

class Vector:
    
    def __init__(self, vList, coordinates):
        
        self.x = coordinates[0][0]
        self.y = coordinates[1][0]
        self.z = coordinates[2][0]
        
        vList.append(coordinates)

class Vertice:
    
    def __init__(self, color, coordinates):
        
        global scale
        
        x = coordinates[0][0]
        y = coordinates[1][0]
        
        x += (SCREEN_WIDTH / 2)
        y -= (SCREEN_HEIGHT / 2) * -1
        
        pygame.draw.circle(window, color, (x, y), scale)
        pygame.display.flip()

def scaleFactor(s):
    
    global scale
    scale = s

def Window(running):
    global angle
    
    while running:
        
        for ev in pygame.event.get():
        
            if ev.type == pygame.QUIT:
                
                sys.exit()
        
        angle += 0.01

pygame.display.flip()
