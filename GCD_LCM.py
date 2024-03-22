# 최대공약수
def GCD(x,y):
    if x < y:
        x,y = y,x
    while y>0 :
        x,y = y,x%y
    return x

# 최소공배수
def LCM(x,y):
    return (x*y)//GCD(x,y)