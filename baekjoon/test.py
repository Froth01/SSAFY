# from collections import Counter

# fruits =['사과','배','사과','파인애플','귤','파인애플',
#          '사과','파인애플','배','파인애플','사과','딸기','딸기']
# count_fruits = Counter(fruits)
# print(count_fruits)

# fruits_dic = {}
# for fruit in fruits:
#     fruits_dic[fruit]=fruits.count(fruit)
# print(fruits_dic)


a=['123','456','46464','4846556','13']
a_l=[]
for n in range(len(a)):
    a_l.append(len(a[n]))
print(max(a_l))