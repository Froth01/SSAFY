word = input()
result = word[1:-1]
if word[0]!='"' or word[-1]!='"':
    result = 'CE'
elif len(word)==2:
    result = 'CE'
check = 0
for w in word[1:-1]:
    if w.isalpha():
        check+=1
if not check:
    result = 'CE'
print(result)