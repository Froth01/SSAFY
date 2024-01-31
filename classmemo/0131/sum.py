import sys
sys.stdin = open('input_sum.txt')

def sum_list(lst):
    result = 0
    for n in lst:
        result+=n
    return result

for test in range(10):
    frame = []
    sum_num = 0
    T = int(input())
    for n in range(100):
        frame.append(list(map(int, input().split())))

    for i in range(len(frame)):
        if sum_num < sum_list(frame[i]):
            sum_num = sum_list(frame[i])
        row_sum = []
        x_sum1 = []
        x_sum2 = []
        for j in range(len(frame)):
            row_sum.append(frame[j][i])
            x_sum1.append(frame[j][j])
            x_sum2.append(frame[-j][-j])
        if sum_num < sum_list(row_sum):
            sum_num = sum_list(row_sum)
        elif sum_num < sum_list(x_sum1):
            sum_num = sum_list(x_sum1)
        elif sum_num < sum_list(x_sum2):
            sum_num = sum_list(x_sum2)

    print(f'#{T} {sum_num}')



