my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
odd = []
for i in range(len(my_list)):
        if my_list[i]%2!=0:
            odd.append(my_list.pop(i))
            
print(my_list)