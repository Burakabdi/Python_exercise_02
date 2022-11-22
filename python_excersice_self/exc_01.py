# Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
# If the number is a multiple of 4, print out a different message.

user_number = int(input("Please enter a number: "))

def odd_or_even(number):
    if number % 2 == 0 and number % 4 != 0:
        print(f"Number {number} is even!")
    elif number % 2 == 0 and number % 4 == 0:
        print(f"number {number} is even and dividible by four")
    else:
        print(f"number {number} is odd")

odd_or_even(user_number)