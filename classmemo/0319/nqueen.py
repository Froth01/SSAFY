def backtracking(n):
    global cnt
    if n==N:
        cnt+=1
        return
    else:
        for j in range(N):
            if check(n,j):
                queen[n]= [n,j,n-j,n+j]
                backtracking(n+1)

def check(i,j):
    if i == 0:
        return True
    for d in range(i):
        if queen[d][0] == i or queen[d][1] == j or queen[d][2] == i-j or queen[d][3] == i+j:
            return False
    return True




if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N = int(input())
        queen = [0]*N
        cnt = 0
        backtracking(0)
        print(f'#{t+1} {cnt}')
