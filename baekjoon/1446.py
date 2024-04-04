# 기본 정보 입력
N,D = map(int,input().split())
# 지름길 리스트
shortcut = []
# 각 지름길 입력
for _ in range(N):
    start, end, dist = map(int,input().split())
    # 지름길이 더 멀거나 도착점 지나는 길은 안넣음
    if end-start < dist or end > D:
        continue
    shortcut.append((start,end,dist))
# 모든 길 거리를 리스트로 저장
highway = [n for n in range(D+1)]
# 길 하나씩 가며 지름길 시작점일때 지름길 대입
# 중첩대입으로 더 작은값으로 갱신하며 진행
for h in range(len(highway)):
    # 지름길 적용시 그 중간부분 값이 변하므로 계속 최신화
    highway[h] = min(highway[h], highway[h-1]+1)
    for cut in shortcut:
        if h==cut[0]:
            highway[cut[1]] = min(highway[cut[1]],highway[h]+cut[2])
print(highway[-1])







