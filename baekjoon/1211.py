def digit_product(num):
    num = str(num)
    result = 1
    for n in num:
        result *= int(n)
    return result

def self_product(num):
    return num * digit_product(num)

for i in range(1,10**18+1):
    print(self_product(i))