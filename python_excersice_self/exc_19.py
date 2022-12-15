# Write a Python function that takes a number as a parameter and check the number is prime or not. 
# Note : A prime number is a natural number greater than 1 and that has no positive divisors other than 1 and itself.


def test_prime(number):
    if (number==1):
        return False
    elif (number==2):
        return True
    else:
        for x in range(2,number):
            if(number % x==0):
                return False
        return True        

     
print(test_prime(7))