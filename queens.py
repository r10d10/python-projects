#!/usr/bin/python2

def solver(board, col, n):
    global sol
    if len(board) >= n:
        sol += 1 
        print('Solution #' + str(sol))
        for i in range(n):
            for j in range(n):
                if j == board[i]:
                    print('Q'),
                else:
                    print('-'),
            print
        print
        #print('Solution: '+ ' '.join(map(str, board)))
        return

    for i in range(n):
        board.append(i)    
        if check(board) == True:
            col += 1
            solver(board, col, n)
        board.pop()
        col -= 1

def check(board):
    for i in range(len(board) - 1):
        if board [-1] == board [i]:
            return False
    for j in range(len(board) - 1):
        if board[-1] + (len(board) - j - 1) == board[j]:
            return False 
        if board[-1] - (len(board) - j - 1)  == board[j]:
            return False
    return True

def main():
    global sol
    col = 0
    n = input("Enter size: ")
    board = []
    if n > 0:
        solver(board, col, n)
    if sol > 0 and n > 0:
        print('Total number of solution: '+ str(sol))
    else:
        print('No solutions.')

sol = 0

if __name__ == "__main__":
    main()
