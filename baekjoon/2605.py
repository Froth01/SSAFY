N = int(input())
pick = list(map(int,input().split()))
new_arr = [1]
for i in range(2,N+1):
    new_arr.insert(i-pick[i-1]-1,i)
print(*new_arr)