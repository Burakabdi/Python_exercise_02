# Write a Python function that takes a sequence of numbers and determines whether all the numbers are different from each other

def check_dist(x):
    if len(x) == len(set(x)):
        return True
    else:
        return False 

print(check_dist([1,2,3]))
print(check_dist([1,2,3,3]))