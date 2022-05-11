"""
main

Description:
"""
# Modules
import Matrix_Projection_001 as mm
import Engine as e
from math import sin, cos

# Matrix(s) and Vector List(s)
projection = [[1, 0, 0], [0, 1, 0]]
vectorList = []

# Angle Degree Variables
angleZ = 0
angleY = 0

# Points
p1 = e.Vector(vectorList, [[-50], [-50], [0]])
p2 = e.Vector(vectorList, [[50], [-50], [0]])
p3 = e.Vector(vectorList, [[-50], [50], [0]])
p4 = e.Vector(vectorList, [[50], [50], [0]])

# Program
while True:
    
    # Rotation Matrixes
    rotateZ = [[cos(angleZ), -sin(angleZ)], [-sin(angleZ), cos(angleZ)]]
    
    #rotateY = [[cos(angleY), -sin(angleY)], [sin(angleY), cos(angleY)]]
    
    # Clear Screen
    e.clearScreen()
    
    # Draws Vertices
    for x in range(len(vectorList)):
    
        projected = mm.matmul(projection, vectorList[x])
        rotatedZ = mm.matmul(rotateZ, projected)
        e.Vertice((255, 255, 255), rotatedZ)
        
    # Adds to Angles
    angleZ += 0.01

e.Window(True)
