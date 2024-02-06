nums = ['ZRO','ONE','TWO','THR','FOR','FIV','SIX','SVN','EGT','NIN']
T= int(input())
for t in range(T):
    case,length = map(str,input().split())
    source = list(map(str,input().split()))

    count = {}
    for i in range(10):
        count[nums[i]]=0
    for s in source:
        count[s]+=1
    print(case)
    for key in count:
        print((key+' ')*count[key], end='')
    print()