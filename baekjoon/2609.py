def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

def LCM(x,y):
    return (x*y)//GCD(x,y)


N,M = map(int,input().split())
print(GCD(N,M))
print(LCM(N,M))