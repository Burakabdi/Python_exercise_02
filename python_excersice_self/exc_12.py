# Write a function that given a list of integers, create another list containing only the elements of even
# position of the first list.

import random
list_of_num = [random.randint(1,100) for _ in range (0,20)] 
print(list_of_num)

even_list = list(filter(lambda x: x%2 ==0, list_of_num))
print(even_list)

# or

even_list = []
for i in list_of_num:
    if i%2 ==0:
        even_list.append(i)
    else: 
        pass

print(even_list)