import sys

input = sys.stdin.readline

N = int(input())
need = list(map(int, input().split()))

# 각 공장에서의 라면 구입 비용
factory_costs = [3, 5, 7]

# 총 비용을 저장할 변수
total_cost = 0

# 각 공장에서 라면을 구매하는 방법을 순회하며 최소 비용을 계산
for i in range(N):
    # 현재 공장에서의 라면 구입 비용을 저장할 변수
    min_cost = float('inf')

    # 현재 공장에서부터 시작하여 가능한 모든 구매 방법을 고려
    for j in range(3):
        # 현재 공장에서부터 j개의 공장까지의 라면 구입 비용을 계산
        cost = sum(min(need[i:i + j + 1]) * factory_costs[k] for k in range(j + 1))
        # 최소 비용을 업데이트
        min_cost = min(min_cost, cost)

    # 최소 비용을 총 비용에 더함
    total_cost += min_cost

    # 구입한 라면 수만큼 라면 필요량에서 빼줌
    for j in range(3):
        if i + j < N:
            need[i + j] -= min(need[i:i + j + 1])

print(total_cost)
