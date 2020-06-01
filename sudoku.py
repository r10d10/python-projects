def main():
    board = [[0,0,3,0,2,0,6,0,0],
             [9,0,0,3,0,5,0,0,1],
             [0,0,1,8,0,6,4,0,0],
             [0,0,8,1,0,2,9,0,0],
             [7,0,0,0,0,0,0,0,8],
             [0,0,6,7,0,8,2,0,0],
             [0,0,2,6,0,9,5,0,0],
             [8,0,0,2,0,3,0,0,9],
             [0,0,5,0,1,0,3,0,0]]    
    solver(board, 0, 0)
    print('\n'.join(' '.join(map(str,sl)) for sl in board))

def solver(board, x, y):
    if x >= 0 and  y >= 8:
        print('\n'.join(' ').join(map(str, sl)) for sl in board)
        return
    for i in range(x, len(board)):
        for j in range(y, len(board[i])):
            if board[i][j] == 0:
                for n in range(1, 9):
                    board[i][j] = n
                    #print(n)
                    if check(board, i, j):
                        if j >= 8:
                            solver(board, i + 1, 0)

                            #print('\n'.join(' ').join(map(str, sl)) for sl in board)
                        else:
                            solver(board, i, j + 1)
                        
                            #print('\n'.join(' ').join(map(str, sl)) for sl in board)
                    board[i][j] = 0

def check(board, i, j):
    for jj in range(len(board[i])):
        if board[i][j] == board[i][jj] and j != jj:
            return False
    for ii in range(len(board)):
        if board[i][j] == board[ii][j] and i != ii:
            return False
    
    #print('\n'.join(' ').join(map(str, sl)) for sl in board)
    return True

if __name__ == "__main__":
    main()
