# Write a Python program to calculate the sum of the positive and negative numbers of a given list of numbers using lambda function

given_list = [2, 4, -6, -9, 11, -12, 14, -5, 17]

check_if_positive = list(filter(lambda x: x > 0 , given_list))
sum_positive_list = sum(check_if_positive)
print(f"Sum of positive numbers: {sum_positive_list}")

check_if_negative = list(filter(lambda x: x < 0 , given_list))
sum_negative_list = sum(check_if_negative)
print(f"Sum of negative numbers: {sum_negative_list}")