import sys
input = sys.stdin.readline

sudoku = []
zero = []
y_sudoku = [[] for _ in range(9)]
cube_sudoku = [[[] for _ in range(3)] for _ in range(3)]
for i in range(9):
    line = list(map(int,input().split()))
    sudoku.append(line)
    for j in range(len(line)):
        if line[j]==0:
            zero.append([i,j])
for j in range(9):
    for i in range(9):
        y_sudoku[j].append(sudoku[i][j])
for i in range(0,7,3):
    for j in range(0,7,3):
        cube = []
        for ii in range(i,i+3):
            for jj in range(j,j+3):
                cube_sudoku[ii//3][jj//3].append(sudoku[ii][jj])
m = 1
while zero:
    t = zero.pop(0)
    x = sudoku[t[0]]
    y = y_sudoku[t[1]]
    s = cube_sudoku[t[0]//3][t[1]//3]
    while True:
        n = m%10
        if n == 0:
            m+=1
            continue
        elif n in x:
            m+=1
            continue
        elif n in y:
            m+=1
            continue
        elif n in s:
            m+=1
            continue
        else:
            sudoku[t[0]][t[1]]=n
            y_sudoku[t[1]][t[0]]=n
            cube_sudoku[t[0]//3][t[1]//3][(t[0]%3)*3+(t[1]%3)]=n
            m+=1
            break
for s in sudoku:
    print(*s)

