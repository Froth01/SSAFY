def cal(x):
    if x%3 == 0:
        cnt+=1
        cal(x//3)
    elif x%2 == 0:
        cal(x//2)
