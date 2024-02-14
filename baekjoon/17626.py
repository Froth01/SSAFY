# def rootminus(num,lst):
#     if num == 0:
#         return
#     elif num==1:
#         lst.append(1)
#         return
#     else:
#         minus = int(num**0.5)
#         lst.append(minus)
#         rootminus(num-minus**2,lst)
def min_sq_sum(num):
    sqs = [i ** 2 for i in range(1, int(num ** 0.5) + 1)]
    min_need = [50000] * (num+1)
    min_need[0] = 0
    for i in range(1,num+1):
        for sq in sqs:
            if sq <= i:
                min_need[i] = min(min_need[i], min_need[i - sq] + 1)
            else:
                break
    return min_need[num]

N = int(input())
print(min_sq_sum(N))