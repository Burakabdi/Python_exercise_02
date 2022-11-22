# Write a Python program to find numbers divisible by nineteen or thirteen from a list of numbers using Lambda


original_list = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]

divisible_list = list(filter(lambda x: x%19 == 0 or x%13 ==0 , original_list))
print(divisible_list)