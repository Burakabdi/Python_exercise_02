# Write a Python program to filter a list of integers using Lambda

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(f"given list: {given_list}")

even_list = list(filter(lambda x: x%2 == 0, given_list))
print(f"Even numbers of given list: {even_list}")

odd_list = list(filter(lambda x: x%2 != 0, given_list))
print(f"Odd numbers of given list: {odd_list}")


