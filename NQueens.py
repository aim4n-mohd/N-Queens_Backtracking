N = int(input("How rows/cols/queens? "))

board = [[0]*N for _ in range(N)]
solutions = []

def check(board, row, col):
    for i in range(N):
        if i!=row:
            if board[i][col]:
                return False
        if i!=col:
            if board[row][i]:
                return False
    
    direction = [(-1,-1),(-1,1)]
    
    for dr,dc in direction:
        r = dr + row
        c = dc + col

        while 0<=r<N and 0<=c<N:
            if board[r][c]:
                return False
            r+=dr
            c+=dc

    return True


def queen(board, row, col=0):

    if row==N:
        solutions.append([r[:] for r in board])
        return
    
    for col in range(N):
        if check(board, row, col):
            board[row][col] = 1
            queen(board, row+1)
            board[row][col] = 0


queen(board, 0)
for i,sol in enumerate(solutions):
    print(f"\n\nSolution - {i+1}:")
    for j in sol:
        print(j)
print(f"Total Solutions - {len(solutions)}.")
