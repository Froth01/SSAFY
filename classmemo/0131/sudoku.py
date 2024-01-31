T = int(input())
for t in range(T):
    result = 0
    sudoku = []
    sudoku.append(list(map(int,input().split())))
    for i in range(len(sudoku)):
        row = set()
        for j in range(len(sudoku)):
            if sudoku[i][j] not in set(sudoku[i]):
                result = 0
            row.add(sudoku[j][i])
            for s in range(3):

        if len(low)!=9:
            result = 0