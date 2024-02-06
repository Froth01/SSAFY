X = int(input())
zone = 0
num = 0
a=1
while X>num:
    num+=a
    a+=1
    zone+=1
if zone%2==0:
    print(f'{zone-(num-X)}/{num-X+1}')
else:
    print(f'{num-X+1}/{zone-(num-X)}')
