# Create a list containing 20 random integers in (0, 100) (0 included), print the number of even
# elements and the number of elements greater than 70.

import random

rand_list = [random.randint(0,100) for i in range(0,20)]
print(rand_list)

even_number = len(list(filter(lambda x: x%2 ==0 , rand_list)))
greater_than_70 = len(list(filter(lambda x: x>70 , rand_list)))

print(even_number)
print(greater_than_70)


