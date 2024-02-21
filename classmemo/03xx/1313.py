import itertools
import operator
ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}

T = int(input())
for t in range(T):
    N = int(input())
    cal_input = list(map(int,input().split()))
    nums = list(map(int,input().split()))
    cal_use = '+'*cal_input[0]+'-'*cal_input[1]+'*'*cal_input[2]+'/'*cal_input[3]
    per_cal = set(itertools.permutations(cal_use))
    max_result = 0
    min_result = 999999999999
    for p in per_cal:
        stack = nums[::-1]
        for c in p:
            a = stack.pop()
            b = stack.pop()
            stack.append(ops[c](a,b))
        if max_result<stack[0]:
            max_result=stack[0]
        if min_result>stack[0]:
            min_result=stack[0]
    result = max_result-min_result
    print(f'#{t+1} {result}')