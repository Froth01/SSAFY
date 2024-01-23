words = []
length = []
for n in range(5):
    word = str(input())
    words.append(word)
    length.append(len(words[n]))
for w in range(len(words)):
    if len(words[w])<max(length):
        words[w]+='+'*(max(length)-len(words[w]))
for m in range(max(length)):
    for n in range(5):
        if words[n][m]=='+':
            pass
        else:
            print(words[n][m],end='')

