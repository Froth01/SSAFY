def cycle(arr):
    global count
    sum_num = arr[0] + arr[1]
    new = arr[1] * 10 + sum_num
    if arr!=list(map(int,str(new))):
        count += 1
        return cycle(list(new))
    else:
        return arr



data = int(input())
count = 1
cycle(data)
print(count)
