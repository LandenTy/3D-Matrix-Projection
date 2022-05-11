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

# PROGRAM
window = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
window.fill(BLACK)

class Vector:
    
    def __init__(self, vList, coordinates):
        
        self.coordinates = coordinates
        self.x = coordinates[0][0]
        self.y = coordinates[1][0]
        self.z = coordinates[2][0]
        
        vList.append(coordinates)


# TODO: OPTIMIZE VERTICE PLACEMENT TO LOOK SEAMLESS DURING ROTATION
class Vertice:
    
    def __init__(self, color, coordinates):
        
        global scale
        
        x = coordinates[0][0]
        y = coordinates[1][0]
        
        x += (SCREEN_WIDTH / 2)
        y -= (SCREEN_HEIGHT / 2) * -1
        
        pygame.draw.circle(window, color, (x, y), scale)
        pygame.display.flip()

class Wireframe:
    
    def __init__(self, vertexes, color, line_width):
        
        self.vertexes = vertexes
        x1 = vertexes[0].coordinates[0][0]
        x2 = vertexes[1].coordinates[0][0]
        y1 = vertexes[0].coordinates[1][0]
        y2 = vertexes[1].coordinates[1][0]
        
        pygame.draw.line(window, color, (x1, y1), (x2, y2), line_width)
        pygame.display.flip()

def scaleFactor(s):
    
    global scale
    scale = s

def clearScreen():
    
    global win
    window.fill(BLACK)

def Window(running):
    
    while running:
        
        for ev in pygame.event.get():
        
            if ev.type == pygame.QUIT:
                
                sys.exit()

pygame.display.flip()
