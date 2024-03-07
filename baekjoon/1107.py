import itertools

N = input()
M = int(input())
start = 100
possible = [0,1,2,3,4,5,6,7,8,9]
broke=[]
if M:
    broke = list(map(int,input().split()))
for b in broke:
    possible.remove(b)
# push_lst = list(itertools.product)
# print(push_lst)
push_num = ['','']
push = [0, 0, abs(int(N) - 100)]
n=0
while n<=(len(N)-1) and int(N[n]) in possible:
    push[0] += 1
    push_num[0] += N[n]
    push[1] += 1
    push_num[1] += N[n]
    n+=1
if len(push_num[0])!=len(N):
    for case in range(2):
        start = case%2
        if not start:
            i = 1
            while int(N[n])-i>=0:
                if int(N[n])-i in possible:
                    push[case]+=1
                    push_num[case]+=str(int(N[n])-i)
                    while len(push_num[case])<len(N):
                        push_num[case]+=str(max(possible))
                        push[case]+=1
                    break
                else:
                    i+=1
        else:
            i = 1
            while int(N[n])+i <= 9:
                if int(N[n])+i in possible:
                    push[case] += 1
                    push_num[case]+=str(int(N[n])+i)
                    while len(push_num[case])<len(N):
                        push_num[case] += str(min(possible))
                        push[case]+=1
                    break
                else:
                    i+=1
        if len(push_num[case])!=len(N):
            push[case]=9999999999
        else:
            push[case]+=abs(int(push_num[case])-int(N))
result = min(push)
print(result)

