# N=input()
# check = 0
# n=0
# num_lst = []
# while True:
#     try:
#         if N[n]=='+' or N[n]=='-':
#             num_lst.append(str(int(N[check:n])))
#             num_lst.append(N[n])
#             check = n+1
#         n+=1
#     except:
#         num_lst.append(str(int(N[check:])))
#         break
# spot = [0]
# for n in range(len(num_lst)):
#     if num_lst[n]=='+' or num_lst[n]=='-':
#         spot.append(n+1)
# spot.append(len(num_lst)+1)
# results = []
# for left in range(len(spot)-1):
#     for right in range(left+1,len(spot)):
#         num_lst.insert(spot[left],'(')
#         num_lst.insert(spot[right],')')
#         sentense = ''.join(num_lst)
#         results.append(eval(sentense))
#         num_lst.pop(spot[right])
#         num_lst.pop(spot[left])
# print(min(results))

S = input()
M = S.split('-')
ret = sum(map(int, M[0].split('+')))
for i in M[1:]:
	ret -= sum(map(int, i.split('+')))
print(ret)