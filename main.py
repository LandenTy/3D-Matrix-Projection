"""
main

Description:
"""
# Modules
import Matrix_Projection_001 as mm
import Engine as e

# Variables
projection = [[1, 0, 0], [0, 1, 0]]
vectorList = []

# Points
p1 = e.Vector(vectorList, [[-50], [-50], [0]])
p2 = e.Vector(vectorList, [[50], [-50], [0]])
p3 = e.Vector(vectorList, [[-50], [50], [0]])
p4 = e.Vector(vectorList, [[50], [50], [0]])

# Program
for x in range(len(vectorList)):
    
    projected = mm.matmul(projection, vectorList[x])
    e.Vertice((255, 255, 255), projected)

e.Window(True)
