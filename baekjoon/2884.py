H,M = map(int,input().split())
if M > 45 :
    M-=45
    print(H,M)
else :
    M+=15
    if M==60:
        H+=1
        M=0
    H-=1
    if H==-1:
        H=23
    print(H,M)
