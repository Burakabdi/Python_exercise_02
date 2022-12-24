# Write a Python program to calculate a dog's age in dog's years.
# Note: For the first two years, a dog year is equal to 10.5 human years. After that, each dog year equals 4 human years.
# Expected Output:

# Input a dog's age in human years: 15                                    
# The dog's age in dog's years is 73


dog_age_in_human = int(input("Input a dog's age in human years: "))

if dog_age_in_human < 0:
    print("dog age must be positive!")
    exit()
elif dog_age_in_human <= 2:
    dog_age_in_dog = dog_age_in_human*10.5
else:
    dog_age_in_dog = 21 + (dog_age_in_human-2)*4
    
print("The dog's age in dog's years is", dog_age_in_dog)