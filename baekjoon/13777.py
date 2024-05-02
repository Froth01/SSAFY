while True:
    target = int(input())
    if target == 0:
        exit()
    low = 1
    end = 50
    while True:
        mid = (low + end) // 2
        if target == mid:
            print(mid)
            break
        elif target < mid:
            end = mid-1
            print(mid,end=' ')
        elif target > mid:
            low = mid+1
            print(mid, end=' ')
