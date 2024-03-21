# def endless(word,base,cnt):
#     global trigger
#     if len(word) >= end:
#         print(word[start-1:end])
#         exit()
#     elif cnt > times:
#         for _ in range(end-len(word)):
#             word+='-'
#         print(word[start-1:end])
#         exit()
#     new_word = ''
#     for letter in range(len(base)):
#         if base[letter] == '$':
#             new_word += word
#             if len(new_word) >= end:
#                 print(new_word[start-1:end])
#                 exit()
#         else:
#             new_word += base[letter]
#             if len(new_word) >= end:
#                 print(new_word[start-1:end])
#                 exit()
#     endless(new_word,base,cnt+1)
#
# word = input()
# S = input()
# times = int(input())
# start,end = map(int,input().split())
# print(endless(word,S,1))

def endless(word, S, times, start, end):
    S = S.split('$')[1:]
    len_word = len(word)
    len_S = list(map(len, S))
    total_len_S = sum(len_S)

    initial = word + word.join(S)

    ans = ''
    # $ 1개뿐일 경우 / $로 split 했는데, 처음은 무조건 $이고 뗀 뒤 [1:]슬라이싱을 하면 본 문자열이 나온다.
    # 그 뒤 에 $가 문자열의 끝이면 빈 문자열 ''이 추가되므로 뒤에 안붙었다 = $로 안끝났다.
    # S의 길이가 1이라는 얘기 = $a 두글자짜리 문자열이다.
    if len(S) == 1:
        total_len = len_word + total_len_S * times  # 입력 문자열 뒤에 S 본 문자열이 반복하여 붙는다

        ans = '' # 최종 정답

        for k in range(start, end + 1):
            if k <= len_word:       # 시작이 무조건 $니까
                ans += word[k - 1]
            elif k <= total_len:
                ans += S[0][(k - len_word) % total_len_S - 1] # 입력 문자열의 나머지
            else:
                ans += '-' # 붙일게 없다면

    else:
        cycle = []
        cycle.append(total_len_S + len_word * len(S))

        limit = end
        if times <= 30:
            total_len = total_len_S * (len(len_S) ** times - 1) / (len(len_S) - 1) + (len(len_S) ** times) * len_word
            limit = min(end, total_len)
        while cycle[-1] < limit:
            cycle.append(total_len_S + cycle[-1] * len(S))

        for k in range(start, end + 1):
            temp = k

            if k > cycle[-1]:
                ans += '-'
                continue

            init_final = True
            for i in range(len(cycle) - 1, -1, -1):
                j = 0
                while j < len(S):
                    if cycle[i] >= temp:  # 첫번째 실행에 포함된 문자열
                        init_final = True
                        break
                    temp -= cycle[i]

                    if len_S[j] >= temp:
                        init_final = False
                        break
                    temp -= len_S[j]
                    j += 1

                if not init_final:
                    break

            if init_final:
                ans += initial[temp - 1]
            else:
                ans += S[j][temp - 1]
    return ans


word = input()
S = input()
times = int(input())
start, end = map(int,(input().split()))

print(endless(word, S, times, start, end))
