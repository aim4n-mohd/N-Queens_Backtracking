init_board = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
N = 4

solutions = []

def check(board, row, col):
    

    for i in range(N):
        if i!=row:
            if board[i][col]:
                return False
    for i in range(N):
        if i!=col:
            if board[row][i]:
                return False
            
    directions = ((-1,-1),(-1,1))
        
    for dr,dc in directions:
        new_row = row + dr
        new_col = col + dc
        if 0<=new_row<row and 0<=new_col<col:
            if board[new_row][new_col]:
                return False
    return True


def queen(board, row, col=0):
    
    if check(board, row, col):
        board[row][col] = 1
    else:
        return None
    if row!=N-1:
        for i in range(N):
            queen(board, row+1, i)
    return board

for i in range(N):
    board = [[0,0,0,0],
              [0,0,0,0],
              [0,0,0,0],
              [0,0,0,0]]
    print(queen(board, i))
