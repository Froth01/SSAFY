import sys
sys.stdin = open('sample_input.txt')

# 기본정보 및 테스트케이스 입력부
T = int(input())
for t in range(T):
    N,M = map(int,input().split())
    big_frame = set(input().rstrip() for _ in range(N))
    to_binary = {
        '0':'0000','1':'0001', '2':'0010','3':'0011',
        '4':'0100','5':'0101','6':'0110','7':'0111',
        '8':'1000','9':'1001','A':'1010','B':'1011',
        'C':'1100','D':'1101','E':'1110','F':'1111',
    }
    code = {
        '0001101':'0','0011001':'1','0010011':'2',
        '0111101':'3','0100011':'4','0110001':'5',
        '0101111':'6','0111011':'7','0110111':'8','0001011':'9'
    }
# 주어진 배열 안에서 암호코드 정보 추출
    candidates = []
    for i in big_frame:
        if i=='0'*M:
            continue
        else:
            word = i
            new_word=''
            for w in word:
                if w == '0':
                    new_word+='0'
                else:
                    new_word+=to_binary[w]
            candidates.append(new_word)
#암호 추출
    final_passwords = []
    password_code = ''
    compare = ''
    password = ''
    for c in candidates:
        n=len(c)-1
        while n>=0:
            if c[n]!='0':
                for m in range(1,6):
                    if c[n-7*m+1:n+1] in code:
                        password_code=c[n-56*m+1:n+1]
                        n-=56*m
                        break
            n-=1
        for m in range(0,len(password_code),len(password_code) // 56):
            compare += password_code[m]
            if len(compare) == 7:
                password += code[compare]
                compare = ''
        final_passwords.append(password)
# 암호 적합성 평가
    result = []
    for p in final_passwords:
        odd_sum = 0
        even_sum = 0
        verification = int(p[-1])
        for odd in range(0,len(p),2):
            odd_sum+=int(p[odd])
        for even in range(1,len(p)-1,2):
            even_sum+=int(p[even])
        if (odd_sum*3+even_sum+verification)%10==0:
            result.append(even_sum+odd_sum+verification)
    print(f'#{t+1} {sum(result)}')
