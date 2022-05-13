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
maxIndex = 0

CLOSE_WINDOW = False

ROTATE_X = "ROTATE_X"
ROTATE_Y = "ROTATE_Y"
ROTATE_Z = "ROTATE_Z"

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

# DOESN'T CURRENTLY WORK - WIP (WORK IN PROGRESS)
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
    
    global CLOSE_WINDOW
    
    clock = pygame.time.Clock()
    clock.tick(10)
    
    while not CLOSE_WINDOW:
        
        for ev in pygame.event.get():
        
            if ev.type == pygame.QUIT:
                    
                CLOSE_WINDOW = True

class Quad:
    
    def __init__(self, (x, y, z), minIndex, maxIndex):
        
        p1 = Vector(vectorList, [[-50 + x], [-50 - y], [0 + z]])
        p2 = Vector(vectorList, [[50 + x], [-50 - y], [0 + z]])
        p3 = Vector(vectorList, [[-50 + x], [50 - y], [0 + z]])
        p4 = Vector(vectorList, [[50 + x], [50 - y], [0 + z]])
        
        self.minIndex = vectorList.index(p1.coordinates)
        self.maxIndex = vectorList.index(p4.coordinates)
        self.maxIndex += 1
    
    # - DOES NOT WORK - e.Wireframe([p1, p2], (255, 255, 255), 2)

def Draw(shape):
    
    # Draws Vertices
    for x in range(shape.minIndex, shape.maxIndex):
        
        projected = mm.matmul(projection, vectorList[x])
        Vertice((255, 255, 255), projected)

def Rotate(shape, (axis, angle)):
    
    # Rotation Matrixes
    if axis == "ROTATE_Z":
        
        rotateZ = [[cos(angle), -sin(angle)], [-sin(angle), cos(angle)]]
    
    elif axis == "ROTATE_Y":
    
        rotateY = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
        
    # Clear Screen
    clearScreen()
        
    # Draws Vertices
    for x in range(shape.minIndex, shape.maxIndex):
        
        projected = mm.matmul(projection, vectorList[x])
        rotatedZ = mm.matmul(rotateZ, projected)
        Vertice((255, 255, 255), rotatedZ)

pygame.display.flip()
