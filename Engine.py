"""
Engine

Description:
"""
import pygame, sys
import Matrix_Projection_001 as mm
from math import sin, cos
pygame.init()

# Matrix(s) and Vector List(s)
projection = [[1, 0, 0], [0, 1, 0]]
vectorList = []

# Angle Degree Variables
angleZ = 0
angleY = 0

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

def Window():
    
    clock = pygame.time.Clock()
    clock.tick(30)
    
    for ev in pygame.event.get():
        
        if ev.type == pygame.QUIT:
                
            sys.exit()

# Functions
def Quad(x, y, z):
    
    p1 = Vector(vectorList, [[-50 + x], [-50 + y], [0 + z]])
    p2 = Vector(vectorList, [[50 + x], [-50 + y], [0 + z]])
    p3 = Vector(vectorList, [[-50 + x], [50 + y], [0 + z]])
    p4 = Vector(vectorList, [[50 + x], [50 + y], [0 + z]])
    
    # - DOES NOT WORK - e.Wireframe([p1, p2], (255, 255, 255), 2)

def Rotate():
    
    global angleZ
    global angleY
    
    while True:
    
        # Rotation Matrixes
        rotateZ = [[cos(angleZ), -sin(angleZ)], [-sin(angleZ), cos(angleZ)]]
        #rotateY = [[cos(angleY), -sin(angleY)], [sin(angleY), cos(angleY)]]
        
        # Clear Screen
        clearScreen()
        
        # Draws Vertices
        for x in range(len(vectorList)):
        
            projected = mm.matmul(projection, vectorList[x])
            rotatedZ = mm.matmul(rotateZ, projected)
            Vertice((255, 255, 255), rotatedZ)
            
        # Adds to Angles
        angleZ += 0.009
        
        Window()

pygame.display.flip()
