# Write a program that prints the length of the strings supplied by the user, until the user enters the
# string 'exit'


while True:
    line = input("Say something: ").lower()
    if line == "exit":
        break
    print(len(line))



