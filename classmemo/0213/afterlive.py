# 재귀 함수
'''
알고리즘에서 재귀함수의 사용
- 동적계획법(점화식을 구현)
- 그래프 탐색(DFS 재귀로 구현), 트리 순회
- 백트래킹(DFS로 구현)
- 분할정복(이진탐색..)
'''

# i=0
# while i<3:
#     print('hello')
#     i+=1

# 재귀함수 반복의 종료는 더이상 호출을 하지 않아야함
# 재귀호출을 할지 어떻게/어떤식으로 판단하지?
# 매개변수를 통해서 판단
cnt = 0
def print_hello(i,n):
    if i == n:
        global cnt
        cnt+=1
        print('여기까지')
    else:
        print_hello(i+1,n)
        print_hello(i+1,n)
print_hello(0,3)
print(cnt)