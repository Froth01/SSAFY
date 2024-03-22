# import sys
# sys.setrecursionlimit(100000)

def num_glue(y_site,x_site):
    global num
    for d in range(4):
        di = y_site+dti[d]
        dj = x_site+dtj[d]
        if 0 > di or di >= 4 or 0 > dj or dj >= 4:
          continue
        else:
            num+=frame[di][dj]
            if len(num)==7:
                nums.add(num)
                num=num[:6]
            else:
                num_glue(di,dj)
    num=num[:-1]

T = int(input())
for t in range(T):
    frame = [list(input().split()) for _ in range(4)]
    nums = set()
    dti = [0,1,0,-1]
    dtj = [1,0,-1,0]
    for i in range(4):
        for j in range(4):
            num = frame[i][j]
            num_glue(i,j)
    print(f'#{t+1} {len(nums)}')

