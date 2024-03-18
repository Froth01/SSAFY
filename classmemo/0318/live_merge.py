def merge_sort(low, high): #구간의 시작과 끝
    if low>=high : return

    #2분할
    mid = (low + high) // 2
    merge_sort(low,mid)
    merge_sort(mid+1,high)

    #왼쪽과 오른쪽이 정렬된 상태 -> 병합
    # i는 왼쪽의 시작위치, j는 오른쪽의 시작위치
    # k는 arr에서 복사해서 저장할 temp의 시작위치
    i,j,k = low, mid+1, low

    while i<=mid and j<=high:
        if arr[i] < arr[j]:
            temp[k]=arr[i]
            i, k = i + 1, k + 1
        else:
            temp[k]=arr[j]
            j, k = j + 1, k + 1

    while i <= mid:
        temp[k] = arr[i]
        i, k = i + 1, k + 1
    while j <= high:
        temp[k] = arr[j]
        j, k = j + 1, k + 1

    for i in range(low,high+1):
        arr[i] = temp[i]

arr = [69,10,30,2,16,8,32,21]
N = len(arr)
temp = [0]*N
print(arr)
merge_sort(0,N-1)
print(arr)