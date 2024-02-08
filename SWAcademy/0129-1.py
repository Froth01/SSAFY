T = int(input())
for t in range(T):
    N = int(input())
    fall = []
    num_list = list(map(int, input().split()))
    for n in range(len(num_list)):
        fall.append((len(num_list)-n)-(num_list.count(num_list[n])-1))
    print(f'#{t+1} {max(fall)}')
















