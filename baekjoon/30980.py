N,M = map(int,input().split())
paper = []
for n in range(3*N):
    paper.append(list(input()))
for n in range(N):
    line_answer = []
    for m in range(M):
        if '.' not in paper[1+3*n][1+8*m:7+8*m]:
            if int(paper[1+3*n][1+8*m])+int(paper[1+3*n][3+8*m])==int(''.join(paper[1+3*n][5+8*m:7+8*m])):
                line_answer.append(1)
            else:
                line_answer.append(0) 
            if line_answer[m]==1:
                paper[3*n][8*m:8+8*m]='.******.'
                paper[3*n+2][8*m:8+8*m]='.******.'
                paper[3*n+1][8*m]='*'
                paper[3*n+1][7+8*m]='*'
            else:
                paper[3*n][3+8*m]='/'
                paper[1+3*n][2+8*m]='/'
                paper[2+3*n][1+8*m]='/'
        else:
            if int(paper[1+3*n][1+8*m])+int(paper[1+3*n][3+8*m])==int(paper[1+3*n][5+8*m]):
                line_answer.append(1)
            else:
                line_answer.append(0)
            if line_answer[m]==1:
                paper[3*n][8*m:7+8*m]='.*****.'
                paper[3*n+2][8*m:7+8*m]='.*****.'
                paper[3*n+1][8*m]='*'
                paper[3*n+1][6+8*m]='*'
            else:
                paper[3*n][3+8*m]='/'
                paper[1+3*n][2+8*m]='/'
                paper[2+3*n][1+8*m]='/'
for n in range(3*N):
    print(''.join(paper[n]))