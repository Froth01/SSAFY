import sys
input = sys.stdin.readline

N,M = map(int,input().split())
pokemon = {}

for n in range(N):
    name = input().strip()
    pokemon[name]=n+1
dic_no = [0]+list(pokemon)
for m in range(M):
    search = input().strip()
    if not search.isalpha():
        print(dic_no[int(search)])
    else:
        print(pokemon[search])