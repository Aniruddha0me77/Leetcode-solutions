def setZeroes( matrix: list) :
    m = []
    n = []

    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                m.append(i)
                n.append(j)

    for k in range(len(m)):
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                if k < len(m):
                    if i == m[k] or j == n[k]:
                        matrix[i][j] = 0

            
    print(matrix)




setZeroes([[1,1,1],
           [1,0,1],
           [1,1,1]])
setZeroes([[0,1,2,0],[3,4,5,2],[1,3,1,5]])