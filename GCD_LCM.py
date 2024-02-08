# 최대공약수
def GCD(x,y):
    while(y):
        x,y=y,x%y
    return x

# 최소공배수
def LCM(x,y):
    return (x*y)//GCD(x,y)