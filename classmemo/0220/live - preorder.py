'''
13
1 2 1 3 2 4 3 5 3 6 4 7 5 8 5 9 6 10 6 11 7 12 11 13
'''
def pre_order(T):
    if T:
        print(T,end=' ')
        pre_order(left[T])
        pre_order(right[T])

N = int(input())  # 1번부터 N번까지인 정점
arr = list(map(int,input().split()))
left = [0]*(N+1) # 부모를 인덱스로 왼쪽자식번호 저장
right = [0]*(N+1) # 부모를 인덱스로 오른쪽자식번호 저장
par = [0]*(N+1) #자식을 인덱스로 부모 저장

for i in range(N-1):
    p, c = arr[i*2], arr[i*2+1]
    if left[p] == 0:
        left[p] = c
    else:
        right[p] = c
    par[c] = p

c = N
while par[c]!=0:
    c = par[c]
root = c
print(root)
pre_order(root)