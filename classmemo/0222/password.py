# 기본정보 및 테스트케이스 입력부
T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    big_frame = [input() for _ in range(N)]
    frame = ''
    frame_i = 0
    frame_j = 0
    code = {
        '0001101':'0','0011001':'1','0010011':'2',
        '0111101':'3','0100011':'4','0110001':'5',
        '0101111':'6','0111011':'7','0110111':'8','0001011':'9'
    }
# 주어진 배열 안에서 암호코드 정보 추출 및 암호 추출
    for j in range(M-1,-1,-1):
        for i in range(N):
            if big_frame[i][j]=='1':
                frame_i,frame_j = i,j
                break
        if frame_i or frame_j:
            break
    frame=big_frame[frame_i][frame_j-55:frame_j+1]
    password = ''
    for n in range(0,50,7):
        password+=code[frame[n:n+7]]
# 암호 적합성 평가
    even_sum = 0
    odd_sum = 0
    for even in range(0,len(password),2):
        even_sum+=int(password[even])
    for odd in range(1,len(password),2):
        odd_sum+=int(password[odd])
    if (even_sum*3+odd_sum)%10==0:
        print(f'#{t+1} {even_sum+odd_sum}')
    else:
        print(f'#{t+1} {0}')
