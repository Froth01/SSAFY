N, M = map(int, input().split())
paper = []

# 종이 입력 받기
for _ in range(3 * N):
    paper.append(input().strip())  # 개행문자 제거

# 종이를 확인하며 조건에 따라 수정하기
for n in range(N):
    for m in range(M):
        if '.' not in paper[3 * n + 1][1 + 8 * m:7 + 8 * m]:
            # 슬라이스 범위 수정
            if 1 + 8 * m + 6 <= len(paper[3 * n]):
                val1 = paper[3 * n][1 + 8 * m]
                val2 = paper[3 * n][3 + 8 * m]
                val3 = paper[3 * n][5 + 8 * m:7 + 8 * m]
                
                print("Values:", val1, val2, val3)  # 각 값 출력
                
                if val1.isdigit() and val2.isdigit() and val3.isdigit():
                    if int(val1) + int(val2) == int(val3):
                        paper[3 * n], paper[3 * n + 2] = map(str, f'.{"*"*6}.')
                        paper[3 * n + 1] = paper[3 * n + 1][:8 * m] + '*' + paper[3 * n + 1][8 * m + 1:7 + 8 * m] + '*'
        else:
            # 슬라이스 범위 수정
            if 1 + 8 * m + 6 <= len(paper[3 * n + 1]):
                val1 = paper[3 * n + 1][1 + 8 * m]
                val2 = paper[3 * n + 1][3 + 8 * m]
                val3 = paper[3 * n + 1][5 + 8 * m]
                
                print("Values:", val1, val2, val3)  # 각 값 출력
                
                if val1.isdigit() and val2.isdigit() and val3.isdigit():
                    if int(val1) + int(val2) == int(val3):
                        paper[3 * n] = '.*****.'
                        paper[3 * n + 2] = '.*****.'
                        paper[3 * n + 1] = paper[3 * n + 1][:8 * m] + '*' + paper[3 * n + 1][8 * m + 1:6 + 8 * m] + '*'

# 결과 출력
for n in range(3 * N):
    print(paper[n])
