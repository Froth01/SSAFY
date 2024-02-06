T = int(input())
for t in range(T):
    word = input()
    backword = list(word)
    result = 0
    for n in range(len(word)//2):
        backword[n], backword[-n-1]=backword[-n-1], backword[n]
    if word == ''.join(backword):
        result = 1
    print(f'#{t+1} {result}')
