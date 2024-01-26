height = []
for n in range(9):
    height.append(int(input()))
def find(source):
    for i in range(len(source)):
        for j in range(1,len(source)):
            if sum(source)-(source[i]+source[j])==100:
                source.pop(i)
                source.pop(j-1)
                return source
find(height)
height.sort()
for h in height:
    print(h)
