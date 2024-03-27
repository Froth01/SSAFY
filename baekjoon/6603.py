def lotto(x):
    if len(pick)==6:
        print(*pick)
        return
    for i in range(x,len(S)):
        pick.append(S[i])
        lotto(i+1)
        pick.pop()

while True:
    k, *S = map(int,input().split())
    if k == 0:
        exit()
    used = [0]*len(S)
    result = set()
    pick = []
    lotto(0)
    print()