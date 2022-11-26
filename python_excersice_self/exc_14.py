# Write a Python program to reverse a string.

sample_str = "1234abcd"

def sort_reverse(x):
    x = "".join(sorted(x, reverse= True))
    print(x)

sort_reverse(sample_str)