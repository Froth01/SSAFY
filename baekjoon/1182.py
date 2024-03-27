def plus(x,value):
    global cnt
    if x!=0 and value==S:
        cnt+=1
        return
    for i in range(x,len(nums)):
        if value+nums[i] > S:
            continue
        plus(i+1,value+nums[i])

N,S = map(int,input().split())
nums = list(map(int,input().split()))
cnt = 0
plus(0,0)
print(cnt)
