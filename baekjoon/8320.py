N = int(input())
plus=0
for n in range(1,N+1):
    if n!=2 and n%2==0:
        plus+=1
print(N+plus)