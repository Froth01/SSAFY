def left_push(lst):
    for n in range(N):
        line = []
        for m in range(N):
            if lst[n][m]!=0:
                line.append(lst[n][m])
        x = 1
        while True:
            if x >= len(line):
                break
            elif line[x-1]==0:
                line.pop(x-1)
            elif line[x-1]==line[x]:
                line[x-1]=2*line[x]
                line.pop(x)
                x+=1
            else:
                x+=1
        while len(line)<N:
            line.append(0)
        lst[n]=line

def right_push(lst):
    for n in range(N):
        line = []
        for m in range(N):
            if lst[n][m]!=0:
                line.append(lst[n][m])
        line.reverse()
        x = 1
        while True:
            if x >= len(line):
                break
            elif line[x-1]==0:
                line.pop(x-1)
            elif line[x-1]==line[x]:
                line[x-1]=2*line[x]
                line.pop(x)
                x+=1
            else:
                x+=1
        while len(line)<N:
            line.append(0)
        line.reverse()
        lst[n]=line

def up_push(lst):
    new_frame=[[]*N for _ in range(N)]
    for n in range(N):
        line = []
        for m in range(N):
            if lst[m][n]!=0:
                line.append(lst[m][n])
        x = 1
        while True:
            if x >= len(line):
                break
            elif line[x-1]==0:
                line.pop(x-1)
            elif line[x-1]==line[x]:
                line[x-1]=2*line[x]
                line.pop(x)
                x+=1
            else:
                x+=1
        while len(line)<N:
            line.append(0)
        for i in range(N):
            new_frame[i].append(line[i])
    for l in range(len(lst)):
        lst[l]=new_frame[l]

def down_push(lst):
    new_frame=[[]*N for _ in range(N)]
    for n in range(N):
        line = []
        for m in range(N):
            if lst[m][n]!=0:
                line.append(lst[m][n])
        line.reverse()
        x = 1
        while True:
            if x >= len(line):
                break
            elif line[x-1]==0:
                line.pop(x-1)
            elif line[x-1]==line[x]:
                line[x-1]=2*line[x]
                line.pop(x)
                x+=1
            else:
                x+=1
        while len(line)<N:
            line.append(0)
        line.reverse()
        for i in range(N):
            new_frame[i].append(line[i])
    for l in range(len(lst)):
        lst[l]=new_frame[l]

if __name__ == "__main__":
    T = int(input())
    for t in range(T):
        N,S = input().split()
        N = int(N)
        frame = [list(map(int,input().split())) for _ in range(N)]
        if S == 'left':
            left_push(frame)
        elif S == 'right':
            right_push(frame)
        elif S == 'up':
            up_push(frame)
        elif S == 'down':
            down_push(frame)
        print(f'#{t+1}')
        for l in range(len(frame)):
            print(*frame[l])
