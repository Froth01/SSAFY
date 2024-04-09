import sys
input = sys.stdin.readline

def fishman(x):
    global catch
    for i in range(R):
        if frame[i][x][2]>0:
            catch += frame[i][x][2]
            sharks.remove([i,x])
            frame[i][x] = [0,0,0]
            return

def sharkmove():
    global sharks
    new_shark = []
    for site in sharks:
        i,j = site[0],site[1]
        speed,dir,size = frame[i][j]
        frame[i][j] = [0,0,0]
        for s in range(speed):
            i,j = i+delta[dir][0], j+delta[dir][1]
            if i<0 or i>R-1 or j<0 or j>C-1:
                if dir%2:
                    dir+=1
                else:
                    dir-=1
                i,j = i+delta[dir][0]*2, j+delta[dir][1]*2
        if frame[i][j][2]>size:
            continue
        elif frame[i][j] != [0,0,0]:
            if [i,j] in new_shark:
                new_shark.remove([i,j])
        frame[i][j] = [speed,dir,size]
        new_shark.append([i,j])
    sharks = new_shark




R,C,M = map(int,input().split())
if M == 0:
    print(0)
    exit()
frame = [[[0,0,0] for _ in range(C)] for _ in range(R)]
delta = [(0,0),(-1,0),(1,0),(0,1),(0,-1)]
sharks = []
for m in range(M):
    r,c,s,d,z = map(int,input().split())
    frame[r-1][c-1] = [s,d,z]
    sharks.append([r-1,c-1])
catch = 0
for t in range(C):
    fishman(t)
    sharkmove()
print(catch)
