def right(x,y):    
    return sum(fly_list[x][y+m] for m in range(M) if y+m <= N-1)
def left(x,y):     
    return sum(fly_list[x][y-m] for m in range(M) if y-m >= 0)
def up(x,y):
    return sum(fly_list[x-m][y] for m in range(M) if x-m >= 0)
def down(x,y):
    return sum(fly_list[x+m][y] for m in range(M) if x+m <= N-1)
def right_down(x,y):
    return sum(fly_list[x+m][y+m] for m in range(M) if x+m<=N-1 and y+m<=N-1)
def right_up(x,y):
    return sum(fly_list[x-m][y+m] for m in range(M) if x-m>=0 and y+m<=N-1)
def left_up(x,y):
    return sum(fly_list[x-m][y-m] for m in range(M) if x-m>=0 and y-m>=0) 
def left_down(x,y):  
    return sum(fly_list[x+m][y-m] for m in range(M) if x+m<=N-1 and y-m>=0) 
def cross_kill(x,y):
    result = up(x,y)+down(x,y)+left(x,y)+right(x,y)-(3*fly_list[x][y])
    return result
def x_kill(x,y):
    result = right_down(x,y)+right_up(x,y)+left_down(x,y)+left_up(x,y)-(3*fly_list[x][y])
    return result

if __name__ == "__main__":
    test_case = int(input())
    
    
    for test in range(test_case):
        sum_list=[]
        fly_list = []
        N,M = map(int,input().split())
        for n in range(N):
            fly_list.append(list(map(int,input().split())))
        for x in range(N):
            for y in range(N):
                 sum_list.extend([cross_kill(x,y),x_kill(x,y)])
        result = max(sum_list)
        sum_list=[]
        print(f'#{test+1} {result}')