import sys
input = sys.stdin.readline

def Z_search(N,r,c):
  if r+c == 0:
    return 0
  elif r==1 and c==0:
    return 2
  elif c==0 and r==1:
    return 1
  elif r==1 and c==1:
    return 3
  else:
    K=2**(N-1)
    start=K**2
    if r<=K-1 and c<=K-1:
      return Z_search(N-1,r,c)
    elif r<=K-1 and c>K-1:
      return start+Z_search(N-1,r,c-K)
    elif r>K-1 and c<=K-1:
      return start+start+Z_search(N-1,r-K,c)
    elif r>K-1 and c>K-1:
      return start+start+start+Z_search(N-1,r-K,c-K)

N,r,c=map(int,input().split())
print(Z_search(N,r,c))