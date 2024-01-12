def solution(array):
    repeat_list=[]
    for x in range(1,100):
        repeat_list.append(array.count(array(x))
    if repeat_list.count(max(repeat_list))>1:
        result = -1
    else :
        result = array.index(max(repeat_list))
    
    return result

if __name__ == "__main__":
    array = list(map(int,input().split()))
    
    answer = solution(array)
    print (answer)
