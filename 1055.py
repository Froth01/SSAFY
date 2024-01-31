def endless(w,f,n):
    n-=1
    if n<0:
        return w
    for i in range(len(f)):
        if f[i]=='$':
            f[i]=word
    return endless(w,f,n)

word = input()
frame = input()
M = int(input())
mini,maxi = map(int,input().split())
print(endless(word,frame,M)[mini:maxi+1])
