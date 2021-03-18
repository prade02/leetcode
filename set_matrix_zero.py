"""
problem: 
    in the given matrix of m x n, if a 0 is found, then the whole column and row should be updated to 0
    input is a list of list -> m is the length of list and n is the length of individual list inside the list

Approach 1:
    iterate through the lists (i x j), and append co ordinates of 0 to a list.
    once all co ordinates are gathered, iterate through the co ordinates list and update the main list with 0 for all these items
    the reason it can not be done in step 1: when a list is updated during iteration, subsequent iterations in the loop might be broken
        if we update a co ordinate to 0, the subsequent iteration might see the original value at this location as 0 and will update entire
        row and column - which is not desired.

Approah 2:
    iterate through the lists (i x j), and update locations which are 0 to '0' - though we are updating while iteration, this will not affect
    the logic since our logic here is to check 0 not '0'.
    once the first step is done, iterate through the list again (i x j) and update 0 with '0'.
"""

def set_zeroes(matrix):
    positions = []
    for i in range(len(matrix)):
        if not all(matrix[i]):
            for j in range(len(matrix[i])):
                if matrix[i][j] == 0:
                    positions.append([i, j])
    for position in positions:
        for i in range(len(matrix)):
            matrix[i][position[1]] = 0
        for i in range(len(matrix[0])):
            matrix[position[0]][i] = 0
    print(matrix)

def set_zeroes_v1(matrix):
    for i in range(len(matrix)):
        if 0 in matrix[i]:
            for j in range(len(matrix[0])):
                if matrix[i][j] == 0:
                    for g in range(len(matrix)):
                        if matrix[g][j] != 0:
                            matrix[g][j] = '0'
                    for g in range(len(matrix[0])):
                        if matrix[i][g] != 0:
                            matrix[i][g] = '0'
    for i in range(len(matrix)):
        if '0' in matrix[i]:
            for j in range(len(matrix[0])):
                if matrix[i][j] == '0':
                    matrix[i][j] = 0
    print(matrix)

# inp = [[1,1,1],[1,0,1],[1,1,1]]
# inp = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
inp = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
set_zeroes_v1(inp)