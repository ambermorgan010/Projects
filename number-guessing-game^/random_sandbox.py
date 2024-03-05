'''
CSCI 120 - Computer Science I
Instructors: Jeff Bush & Gregory Schaper
Description: Random Sandbox Example
Teammates Names:
'''

# In order to use the psuedo-random-number-generator in Python we need to
# import the random module
import random

# You must answer these questions.
# 
# To be able to answer them you will need to run this program several times
# and study the output. You may change the code however you want to help you
# understand the code.
#
# 1) What type of number does random.random() generate?
#
# 2) What type of number does random.randint() generate?
#
# 3) What type of number does random.randrange() generate?
#
# 4) What is the smallest number that random.random() can ever generate?
#
# 5) What is the largest number that random.random() can ever generate?
#
# 6) What is the smallest number that random.randint(1, 1000) can ever generate?
#
# 7) What is the largest number that random.randint(1, 1000) can ever generate?
#
# 8) What is the smallest number that random.randrange(1, 1000) can ever generate?
#
# 9) What is the largest number that random.randrange(1, 1000) can ever generate?
#
# 10) How would you generate a random integer between -56 and 753 that includes
#     the first number but not the second?
#


def main():
    # Demo of using random.random() to generate 5 random numbers
    print('random.random(): ', end='') # print a useful string to identify this line
    for count in range(5):       # the loop is only here so we get 5 different numbers
        x = random.random()      # generate the random number and save to the variable x
        print(x, end=' ')        # print the random number
    print()
    print()

    # Demo of using random.randint() to generate 5 random numbers
    print('random.randint(1, 10): ', end='')
    for count in range(5):
        x = random.randint(1, 10)
        print(x, end=' ')
    print()
    print()

    # Demo of using random.randrange() to generate 5 random numbers
    print('random.randrange(1, 10): ', end='')
    for count in range(5):
        x = random.randrange(1, 10)
        print(x, end=' ')
    print()
    print()

if __name__ == "__main__":
    main()
