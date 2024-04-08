def fishman(x):
    global catch
    for i in range(R):
        if frame[x][i]:
            catch += frame[x][i][0]
            sharks.remove([x,i])
            frame[x][i] = []
            return

def sharkmove():
    for site in sharks:
        shark = frame[site[0]][site[1]]
        i,j = site[0]+delta[d][0], site[1]+delta[d][1]




R,C,M = map(int,input().split())
frame = [[[] for _ in range(C)] for _ in range(R)]
delta = [(0,0),(-1,0),(1,0),(0,1),(0,-1)]
sharks = []
for m in range(M):
    r,c,s,d,z = map(int,input().split())
    frame[r][c] = [s,d,z]
    sharks.append([r,c])
time = 1
catch = 0
while time <= C:
    fishman(time)
    sharkmove()
    time += 1
print(catch)
