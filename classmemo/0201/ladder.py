import sys
sys.stdin = open('ladder input.txt')


for T in range(10):
    t = int(input())
    field = []
    for f in range(100):
        field.append(list(map(int,input().split())))
    for j in range(100):
        if field[99][j]==2:
            end = j
    i=99
    j=end
    while i>0:
        if 0<=j-1<=99 and field[i][j-1]==1:
            while 0<=j-1<=99 and field[i][j-1]==1:
                j-=1
        elif 0<=j+1<=99 and field[i][j+1]==1:
            while 0<=j+1<=99 and field[i][j+1]==1:
                j+=1
        i-=1
    print(f'#{t} {j}')
