# 좋은 알고리즘(코드)을 평가하는 척도 ( resource 적게 쓰고 일 하는 것)
# 모든 공통으로 사용하는 컴퓨팅 자원 => CPU(시간) + 메모리(공간)
# 시간 복잡도 증가 => 계산 량이 많다. => cpu 사용량 증가
    #점근적 표기법
    #빅O 표기법 -> 최악의 경우

# 알고리즘 문제 유형 중에 가장 어렵다고 보는 문제
# 어렵다는 건 나에네(인간) 어려운게 아니다. 컴한테 어려운..
# 최적화 문제 => 최적해를 찾는 문제


# 완전 탐색 => 가능한 경우의 수가 증가하면 시간도 증가
    # 백트래킹
    # 동적계획법

    # 분할 정복
    # 자료구조
    # 탐욕(구현이 어려움) => 판타스틱 알고리즘


#0131
def sub(arr,N):
    for i in range(1, 1 << n):
        s = 0
        for j in range(n):
            if i & (1 << j):
               s += arr[j]
arr = [3,6,7,1,5,4]
N=int(input())
arr = list(map(int,input().split()))
print(sub(arr,N))
