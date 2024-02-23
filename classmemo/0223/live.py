# N,M = map(int,input().split())
# num = bin(M)[2:]
# result = 'ON'
# for n in num:
#     if n=='0':
#         result='OFF'
#         break
# print(result)
# #
# to_binary = {
#         '0':'0000','1':'0001', '2':'0010','3':'0011',
#         '4':'0100','5':'0101','6':'0110','7':'0111',
#         '8':'1000','9':'1001','A':'1010','B':'1011',
#         'C':'1100','D':'1101','E':'1110','F':'1111',
#     }
# a = '328D1AF6E4C9BB'
# result = ''
# for num in a:
#     result+=to_binary[num]
# print(result)
# print(bin(0x68B46DDB9346F4)[2:])
# print(len(result))
# print(len(bin(0x68B46DDB9346F4)[2:]))
lst = [1,2,3,4,5,6,7,8]
that = lst[::2]
print(that)