# Write a Python function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument..

def fact(n):
    if n == 0:
        return 1
    else:
        return n* fact(n-1)

n = int(input("enter a number to calculate the factorial: "))
print(fact(n))