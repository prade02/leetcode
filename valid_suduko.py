
def isValidSudoku(board):
    def validate_3x3(board):
        for m in range(0,9,3):
            for n in range(0,9,3):
                temp = []
                for i in range(3):
                    for j in range(3):
                        if board[i+m][j+n] == '.':
                            pass
                        elif board[i+m][j+n] in temp:
                            return False
                        else:
                            temp.append(board[i+m][j+n])
        return True

    def validate_unique_items_in_inner(board):
        for row in board:
            s = set(row)
            s.remove('.')
            if len(row) - row.count('.') != len(s):
                return False
        return True

    def validate_column(board):
        main = []
        for i in range(9):
            inner = []
            for j in range(9):
                inner.append(board[j][i])
            main.append(inner)
        return validate_unique_items_in_inner(main)
    
    if not validate_3x3(board):
        return False
    if not validate_unique_items_in_inner(board):
        return False
    if not validate_column(board):
        return False
    return True



x = [["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]

print(isValidSudoku(x))