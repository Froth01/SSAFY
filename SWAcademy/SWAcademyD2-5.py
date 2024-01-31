#1974. 사전학습 스도쿠 검증

def check_right(a,b,result):
    x_line = sudoku[a]
    for i in range(9):
        if i != b and x_line[i] == x_line[b]:
            result = 0
    return result

def check_up(a,b,result):
    x_line = []
    for a in range(9):
        x_line.append(sudoku[a][b])
    for c in range(1,10):
        if x_line.count(c)>1:
            result = 0
    return result

def check_square(a,b,result) :
    square = []
    for i in range(3 * (a // 3), 3 * (a // 3) + 3):
        for j in range(3 * (b // 3), 3 * (b // 3) + 3):
            square.append(sudoku[i][j])

    for c in range(1, 10):
        if square.count(c) > 1:
            result = 0
            break
    return result

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        sudoku = []
        result = 1
        for n in range(9):
            sudoku.append(list(map(int,input().split())))
        for x in range(9):
            for y in range(9):
                result = check_right(x,y,result)
                result = check_up(x,y,result)
                result = check_square(x,y,result)
                if result==0 :
                    break
        print(f'#{t+1} {result}')
