import time
T = int(input())
for t in range(T):
    N = int(input())
    start = time.time()
    cards = list(range(1,N+1))+[0]*100000
    front = 0
    rear = N-1
    for _ in range(N-2):
        front+=1
        cards[rear+1]=cards[front]
        rear+=1
        front+=1
    print(time.time()-start)
    print(f'#{t+1} {cards[rear]}')
