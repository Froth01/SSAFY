def merge_sort(lst):
    if len(lst) <= 1:
        return lst

    mid = len(lst) // 2
    # 왼쪽 -> lst[:mid], 오른쪽 -> lst[mid:]
    l = merge_sort(lst[:mid])
    r = merge_sort(lst[mid:])
    # 왼쪽과 오른쪽을 병합한다.
    result = []
    # 왼쪽과 오른쪽 모두 자료가 있을 경우
    while l and r:
        if l[0] < r[0]:
            result.append(l.pop(0))
        else:
            result.append(r.pop(0))

    result.extend(l)
    result.extend(r)
    return result

arr = [69,10,30,2,16,8,32,21]
sorted_arr = merge_sort(arr)
print(sorted_arr)