T = int(input())
for t in range(T):
    frame = [list(input()) for _ in range(5)]
    max_len = 0
    for f in frame:
        if max_len<len(f):
            max_len=len(f)
    for f in frame:
        while len(f)<max_len:
            f.append('-')
    answer = ''
    for j in range(max_len):
        for i in range(5):
            if frame[i][j]=='-':
                continue
            else:
                answer+=frame[i][j]
    print(f'#{t+1} {answer}')
