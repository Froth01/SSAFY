# 백트래킹
# 완전탐색 + 가지치기 -> 가능성이 없는(볼 필요 없는) 경우의 수를 제거하는 기법
# 완전탐색 -> 재귀 / 조건 가지치기

'''# 중복된 순열
arr = [i for i in range(1,4)]
# my code
lst = []
def Per(x):
    global lst
    if x == 3:
        print(lst)
        return
    for n in range(1,4):
        lst.append(n)
        Per(x+1)
        lst.pop()
Per(0)
print('------------------------')
# live
path = [0]*3
def dfs(level):
    # 기저 조건 - 이 문제에서는 3개를 뽑을 때까지 반복
    if level==3:
        print(*path)
        return
    # 들어가기 전
    # 다음 재귀 호출 - 다음에 갈 수 있는 곳들은 어디인가? > 이 문제에서는 3가지 경우의 수
    for i in range(len(arr)):
        path[level] = i+1
        dfs(level+1)

    # 갔다와서 할 로직
dfs(0)'''

# 조합
# 123,132,213, 231, 312, 321 ( 숫자는 한번만 사용 )
arr = [i for i in range(1,4)]
path = [0]*3

def dfs(level):
    # 기저 조건 - 이 문제에서는 3개를 뽑을 때까지 반복
    if level==3:
        print(*path)
        return
    # 갈 수 있는 후보군
    for i in range(len(arr)):
        # 여기는 못가
        if arr[i] in path:
            continue
        path[level] = arr[i]
        dfs(level+1)
        path[level]=0
    # 갔다와서 할 로직
dfs(0)
