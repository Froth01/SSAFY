

# while True:
#     if bomb not in word :
#         if word == '':
#             print('FRULA')
#             break
#         else:
#             print(word)
#             break
#     for w in range(len(word)):
#         if word[w] == bomb[0]:
#             for b in range(len(bomb)):
#                 if word[w+b] != bomb[b]:
#                     break
#             else:
#                 word = word[:w]+word[w+len(bomb):]
#                 break
word = input().rstrip()
bomb = list(input())
answer = []
for w in word:
    answer.append(w)
    if w == bomb[-1]:
        if answer[-len(bomb):] == bomb:
            for _ in range(len(bomb)):
                answer.pop()
if not answer:
    print('FRULA')
else:
    print(''.join(answer))