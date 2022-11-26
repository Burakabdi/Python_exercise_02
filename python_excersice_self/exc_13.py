# Write a Python function to multiply all the numbers in a list.

sample_list = [8, 2, 3, -1, 7]

def multiply_list(x):
    result = 1
    for i in x:
        result *= i   
    print(result) 

multiply_list(sample_list)



