N = int(input())
group1 = []
all_list = ['1','2','3']
for x in range(N):
    source = all_list[N-1-x]
    group1.append(source)
result = ''.join(group1)
print(result)