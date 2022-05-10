"""
main

Description:
"""
# Modules
import Matrix_Projection_001 as mm
import Engine as e
from math import sin, cos

# Variables
angle = 10

# Matrixes and Vector List(s)
projection = [[1, 0, 0], [0, 1, 0]]
rotateX = [[cos(angle), -sin(angle)], [-sin(angle), cos(angle)]]
rotateY = [[cos(angle), -sin(angle)], [sin(angle), cos(angle)]]
vectorList = []

# Points
p1 = e.Vector(vectorList, [[-50], [-50], [0]])
p2 = e.Vector(vectorList, [[50], [-50], [0]])
p3 = e.Vector(vectorList, [[-50], [50], [0]])
p4 = e.Vector(vectorList, [[50], [50], [0]])

p5 = e.Vector(vectorList, [[-50], [-50], [-10]])
p6 = e.Vector(vectorList, [[50], [-50], [-10]])
p7 = e.Vector(vectorList, [[-50], [50], [-10]])
p8 = e.Vector(vectorList, [[50], [50], [-10]])

# Program
for x in range(len(vectorList)):
    
    projected = mm.matmul(projection, vectorList[x])
    rotated = mm.matmul(rotateX, projected)
    e.Vertice((255, 255, 255), rotated)

e.Window(True)
