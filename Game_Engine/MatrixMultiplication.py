"""
MatrixMultiplication
Description:
"""
def vecMatrix(v):
    m = [[3], [1]]
    m[0][0] = v.x
    m[1][0] = v.y
    m[1][0] = v.z
    
    return m

def printMatrix(m):
    
    cols = len(m[0])
    rows = len(m)
    print(str(rows) + "x" + str(cols))
    print("-------------------")
    
    for i in range(0, rows):
        
        for j in range(0, cols):
            
            print(str(m[i][j]) + " ")
        
        print()

def matmul(matA, matB):
    
    colsA = len(matA[0])
    rowsA = len(matA)
    
    colsB = len(matB[0])
    rowsB = len(matB)
    
    if colsA != rowsB:
        
        print("Columns of Matrix A must match Rows of Matrix B...")
        return None
    
    result = [[rowsA], [rowsB]]
    
    for i in range(0, rowsA):
        
        for j in range(0, colsB):
            
            totalSum = 0
            for k in range(0, colsA):
                
                totalSum += matA[i][k] * matB[k][j]
            
            result[i][j] = totalSum
    
    return result
