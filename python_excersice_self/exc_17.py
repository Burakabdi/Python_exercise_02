# Write a Python function that takes a list and returns a new list with unique elements of the first list.


def unique_maker(x):
    unique_list = []
    for i in x:
        if i not in unique_list:
            unique_list.append(i)
    return unique_list

print(unique_maker([1,2,3,4,4,4,5,5,5,6,7,8]))

