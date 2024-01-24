N = int(input())
n=1
m=0
while not 6*(n+m-1)+1<=N<6*(n+m)+1:
    m+=n
    n+=1       
print(n+1)