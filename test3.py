def right(x,y):
    right_source = []
    for m in range(M):
        if y+m > N-1 :
            pass
        else:
            right_source.append(fly_list[x][y+m])
    result = sum(right_source)-fly_list[x][y]        
    return result
def left(x,y):
    left_source = []
    for m in range(M):
        if y-m < 0 :
            pass
        else:
            left_source.append(fly_list[x][y-m])
    result = sum(left_source)-fly_list[x][y]        
    return result
def up(x,y):
    up_source=[]
    for m in range(M):
        if x-m < 0 :
            pass
        else:
            up_source.append(fly_list[x-m][y])
    result = sum(up_source)-fly_list[x][y]
    return result
def down(x,y):
    down_source=[]
    for m in range(M):
        if x+m > N-1 :
            pass
        else:
            down_source.append(fly_list[x+m][y])
    result = sum(down_source)-fly_list[x][y]
    return result
def right_down(x,y):
    source = []
    for m in range(M):
        if x+m>N-1 or y+m>N-1:
            pass
        else:
            source.append(fly_list[x+m][y+m])
    result = sum(source)-fly_list[x][y]
    return result
def right_up(x,y):
    source = []
    for m in range(M):
        if x-m<0 or y+m>N-1:
            pass
        else:
            source.append(fly_list[x-m][y+m])
    result = sum(source)-fly_list[x][y]
    return result
def left_up(x,y):
    source = []
    for m in range(M):
        if x-m<0 or y-m<0:
            pass
        else:
            source.append(fly_list[x-m][y-m])
    result = sum(source)-fly_list[x][y]
    return result
def left_down(x,y):  
    source = []
    for m in range(M):
        if x+m>N-1 or y-m<0:
            pass
        else:
            source.append(fly_list[x+m][y-m])
    result = sum(source)-fly_list[x][y]
    return result  
def cross_kill(x,y):
    result = up(x,y)+down(x,y)+left(x,y)+right(x,y)+fly_list[x][y]
    return result
def x_kill(x,y):
    result = right_down(x,y)+right_up(x,y)+left_down(x,y)+left_up(x,y)+fly_list[x][y]
    return result
if __name__ == "__main__":
    test_case = int(input())
    fly_list = []
    sum_list = []
    for test in range(test_case):
        N,M = map(int,input().split())
        for n in range(N):
            fly_list.append(list(map(int,input().split())))
        for x in range(N):
            for y in range(N):
                 sum_list.append(cross_kill(x,y))
                 sum_list.append(x_kill(x,y))
        result = max(sum_list)
        print(f'#{test+1} {result}')