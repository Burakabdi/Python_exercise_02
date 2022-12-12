# Write a Python program to square and cube every number in a given list of integers using Lambda

given_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

def square_qube(list_of_numbers):
    square_list = []
    qube_list = []
    for i in list_of_numbers:
        square_list.append(i*i)
    for i in list_of_numbers:
        qube_list.append(i**3)
    print("Original list: ")
    print(list_of_numbers)
    print("square of original list: ")
    print(square_list)
    print("qube of original list: ")
    print(qube_list) 


square_qube(given_list)