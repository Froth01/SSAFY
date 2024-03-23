import sys
input = sys.stdin.readline
from collections import deque

def find_k(y,x):
    queue = deque()
    queue.append((y,x,frame[y][x]))

    while queue:
        i,j,key = queue.popleft()
        # 현재까지 붙인 문자열 정보를 딕셔너리에 저장
        if key not in used:
            used[key] = 1
        else:
            used[key] += 1
        # 주어지는 문자열 길이까지만 저장
        if len(key) >= 5:
            return
        # 8방향 탐색, 환형은 나머지 계산으로 적용
        for d in range(8):
            di = (i + delta[d][0]) % N
            dj = (j + delta[d][1]) % M
            queue.append((di,dj,key+frame[di][dj]))

# 초기 입력
N,M,K = map(int,input().split())
frame = [list(input().rstrip()) for _ in range(N)]

# 8방향 탐색 경로
delta = [(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1),(-1,0),(-1,1)]

# 전체 정보를 저장할 dict와 list, 값 입력
used = dict()
result = []
for i in range(N):
    for j in range(M):
        find_k(i,j)

# 문자를 입력받고, 저장된 dict에서 결과 출력
for _ in range(K):
    word = input().rstrip()
    if word in used:
        result.append(used[word])
    else:
        result.append(0)

for answer in result:
    print(answer)

