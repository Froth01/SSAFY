def plus(x,value):
    global cnt
    if x==N:
        if value==S:
            cnt+=1
        return
    plus(x+1,value+nums[x])
    plus(x+1,value)

N,S = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
plus(0,0)
if S==0 and cnt==0:
    print(0)
elif S==0:
    print(cnt-1)
else:
    print(cnt)
