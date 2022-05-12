"""
Demo

Description:
"""
import Engine as e

rotate = 0.1
rotationSpeed = 0.009
    
# Shapes
q = e.Quad((0, 200, 0), 0, 0)
q1 = e.Quad((0, 0, 0), 0, 0)

while not e.CLOSE_WINDOW:
    
    e.Draw(q)
    
    e.Rotate(q1, (e.ROTATE_Z, rotate))
    rotate += rotationSpeed
