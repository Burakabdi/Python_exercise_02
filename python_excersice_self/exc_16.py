# Write a Python function that accepts a string and calculate the number of upper case letters and lower case letters.

def string_test(x):
    d = {"UPPER LETTERS": 0, "LOWER LETTERS": 0}
    for i in x:
        if i.isupper():
            d["UPPER LETTERS"] += 1
        elif i.islower():
            d["LOWER LETTERS"] += 1
        else:
            pass
    print(f"Original string: {x}")
    print(f"Number of upper letters: {d['UPPER LETTERS']}")
    print(f"Number of lower letters: {d['LOWER LETTERS']}")

string_test("TesT mY sTrinG")