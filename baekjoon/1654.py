def Padoban(n):
    global padoban
    if n in padoban:
        return padoban[n]
    elif n<=3:
        padoban[n]=1
        return 1
    elif n<=5:
        padoban[n]=2
        return 2
    else:
        padoban[n]=Padoban(n-1)+Padoban(n-5)
        return padoban[n]

T = int(input())
for t in range(T):
    N = int(input())
    padoban = {}
    print(Padoban(N))