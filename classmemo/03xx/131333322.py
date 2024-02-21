import sys
sys.stdin = open('sample_input (2).txt')
import itertools
import operator

ops = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.floordiv}

def calculate(nums, ops_order):
    stack = [nums[0]]
    for i in range(len(ops_order)):
        a = stack.pop()
        b = nums[i + 1]
        stack.append(ops[ops_order[i]](a, b))
    return stack[0]

T = int(input())
for t in range(T):
    N = int(input())
    cal_input = list(map(int, input().split()))
    nums = list(map(int, input().split()))

    # 순열을 사용하지 않고 조합만 생성
    ops_order = []
    for op, count in zip(ops.keys(), cal_input):
        ops_order.extend([op] * count)

    # 중복 제거를 위해 set 사용
    ops_orders = set(itertools.permutations(ops_order))

    min_result = float('inf')
    max_result = float('-inf')
    for ops_order in ops_orders:
        result = calculate(nums, ops_order)
        min_result = min(min_result, result)
        max_result = max(max_result, result)

    print(f'#{t + 1} {max_result - min_result}')