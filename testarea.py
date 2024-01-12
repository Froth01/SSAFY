a = [1,9,4,8,8,9,2,9,8,7,9,8]
b = []
a.sort()
a.reverse()
for x in range(len(a)):
    b.append(a.count(a[x]))
print(a[b.index(max(b))])

# for x in range(len(a)):
#     if ValueError :
#         pass
#     else :
#         a.remove(3+2)
    
# del a.(b for b in a if b == score[0])
