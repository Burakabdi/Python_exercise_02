# Write a function to determine the highest number in a list of integer (do not use the max() function).


import random

list_of_num = [random.randint(1,100) for i in range (0,20)]

def find_highest(aList):
    highest=aList[0]
    for element in aList:
        if element > highest:
            highest = element
    return(highest)

print(find_highest(list_of_num))