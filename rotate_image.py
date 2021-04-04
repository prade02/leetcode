def rotate(matrix):
    main = []
    for j in range(len(matrix)):
        inner = []
        for i in range(len(matrix)-1, -1, -1):
            inner.append(matrix[i][j])
        main.append(inner)
    matrix[:] = main[:]

""" 
def rotate(matrix):
    for i in range(len(matrix)):
        for j in range(i,len(matrix)):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
 """
x = [[1,2,3],[4,5,6],[7,8,9]]
rotate(x)
print(x)