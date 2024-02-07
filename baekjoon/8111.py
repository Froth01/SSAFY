# def binary(num):
#     i = 0
#     result = 0
#     while True:
#         result+=(num%2)*(10**i)
#         num//=2
#         i+=1
#         if num<2:
#             result+=(num%2)*(10**i)
#             return result

# def compare(num):
#     i = 1
#     while True:
#         binary = int(bin(i)[2:])
#         if len(str(binary))>100:
#             return 'BRAK'
#         elif len(str(binary))<len(str(num)):
#             i+=1
#             continue
#         elif binary%num==0:
#             return binary
#         i+=1
#
# T = int(input())
# for t in range(T):
#     N = int(input())
#     print(compare(N))


def compare(i):
    global n,N
    while True:
        if len(str(i))>100:
            return 'BRAK'
        n+=1
        if i%N==0:
            return i
        else:
            compare(int(str(i)+str((1 + n)%2)))

T = int(input())
for t in range(T):
    N = int(input())
    n = 0
    print(compare(1))