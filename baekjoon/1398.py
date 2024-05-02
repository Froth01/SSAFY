coin = [i for i in range(100)]

for n in range(10,25):
    coin[n] = min(coin[n-1]+1, coin[n-10]+1)
for n in range(25,100):
    coin[n] = min(coin[n-1]+1, coin[n-10]+1, coin[n-25]+1)

T = int(input())
for t in range(T):
    price = int(input())
    total = 0
    while price:
        total += coin[price%100]
        price //= 100
    print(total)