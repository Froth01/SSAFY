import sys
input = sys.stdin.readline

def value_in(x):
    global trigger
    if x==len(zero):
        trigger = True
        return
    for v in range(1,10):
        if v not in set(sudoku[zero[x][0]]):
            if v not in set(y_sudoku[zero[x][1]]):
                if v not in set(cube_sudoku[zero[x][0]//3][zero[x][1]//3]):
                    sudoku[zero[x][0]][zero[x][1]] = v
                    y_sudoku[zero[x][1]][zero[x][0]] = v
                    cube_sudoku[zero[x][0]//3][zero[x][1]//3][(zero[x][0]%3)*3+(zero[x][1]%3)] = v
                    value_in(x+1)
                    if trigger:
                        answer[x] = v
                        return

sudoku = [list(map(int,input().split())) for _ in range(9)]
y_sudoku = list(map(list,zip(*sudoku)))
cube_sudoku = [[[] for _ in range(3)] for _ in range(3)]
for i in range(0,7,3):
    for j in range(0,7,3):
        for ii in range(i,i+3):
            for jj in range(j,j+3):
                cube_sudoku[ii//3][jj//3].append(sudoku[ii][jj])

trigger = False
zero = []
for i in range(9):
    for j in range(9):
        if sudoku[i][j]==0:
            zero.append((i,j))
answer = [0]*len(zero)
value_in(0)
for line in sudoku:
    print(*line)