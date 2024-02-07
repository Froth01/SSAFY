def triangle(num):
    num_lst = [0]*num
    num_lst[0] = num_lst[-1] = 1
    if len(num_lst)<=2:
        return num_lst
    for n in range(1,len(num_lst)-1):
        num_lst[n]=triangle(num-1)[n-1]+triangle(num-1)[n]
    return num_lst

T = int(input())
for t in range(T):
    N = int(input())
    print(f'#{t+1}')
    for r in range(1,N+1):
        print(*triangle(r))



