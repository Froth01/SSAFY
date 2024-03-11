N,S = input().split()
total = 0
for n in range(int(N)):
    item,ea = input().split()
    name = list(item.split('_'))
    for i in name:
        if i==S:
            total+=int(ea)
            break
print(total)