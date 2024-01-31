
#0131
'''
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
'''
#1차 배열 생성 => 길이
'''
N = 5
arr = [0]*N
'''
#2차 배열 생성 => 행과 열의 크기


# N=5 # 5*5
# arr = [[0]*N for _ in range(N)]
# arr[0][0] = 1
# arr[3][2] = 1
# for line in arr:
#     print(*line)
'''
N=5 # N*M
M=4
arr = [[0]*M for _ in range(N)]
arr[0][0] = 1
arr[3][2] = 1
for line in arr:
    print(*line)
'''

# 색칠 done
# 섬
# 부분합
#
# 파리
# 스도쿠
# 어디에

#종료조건에 사용할 변수 생성
i = 0 #초기값
while i<5: # 종료 조건에 변수가 있어야 한다.
    #반복할 내용
    print(i)
    i += 2
print('=================')
for i in range(5):
    i += 2
    print(i)