# 17 list comprehension problems in python

fruits = ['mango', 'kiwi', 'strawberry', 'guava', 'pineapple', 'mandarin orange']
numbers = [2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 13, 17, 19, 23, 256, -8, -4, -2, 5, -9]

'''
# Example for loop solution to add 1 to each number in the list
numbers_plus_one = []
for number in numbers:
    numbers_plus_one.append(number + 1)
# Example of using a list comprehension to create a list of the numbers plus one.
numbers_plus_one = [number + 1 for number in numbers]
# Example code that creates a list of all of the list of strings in fruits and uppercases every string
output = []
for fruit in fruits:
    output.append(fruit.upper())
'''

# 1 - rewrite the above example code using list comprehension syntax. 
fruity1 = [f for f in fruits]

# 2 - create a variable capitalized_fruits and use list comprehension syntax to produce output
fruity2 = [f.capitalize() for f in fruits]

# 3 - Use a list comprehension to make a variable fruits_with_more_than_two_vowels.
fruity3 = [f for f in fruits if len([v for v in f if v in 'aeiou']) > 2]

# 4 - make a variable fruits_with_only_two_vowels.
fruity4 = [f for f in fruits if len([v for v in f if v in 'aeiou']) == 2]

# 5 - make a list that contains each fruit with more than 5 characters
fruity5 = [f for f in fruits if len(f) > 5]

# 6 - make a list that contains each fruit with exactly 5 characters
fruity6 = [f for f in fruits if len(f) == 5]

# 7 - Make a list that contains fruits that have less than 5 characters
fruity7 = [f for f in fruits if len(f) < 5]

# 8 - Make a list containing the number of characters in each fruit.
fruity8 = [len(f) for f in fruits]

# 9 - Make a list of only the fruits that contain the letter "a"
fruity9 = [f for f in fruits if 'a' in f]

#----------------------------------------------------------------
from math import sqrt

# 10 - Make a variable that holds only the even numbers 
numbs10 = [n for n in numbers if n%2 == 0]

# 11 - Make a variable that holds only the odd numbers
numbs11 = [n for n in numbers if n%2 == 1]

# 12 - Make a variable that holds only the positive numbers
numbs12 = [n for n in numbers if n > 0]

# 13 - Make a variable that holds only the negative numbers
numbs13 = [n for n in numbers if n < 0]

# 14 - produce a list of numbers with 2 or more numerals
numbs14 = [n for n in numbers if abs(n) >= 10]

# 15 - Make a variable of numbers list with each element squared.
numbs15 = [n**2 for n in numbers]

# 16 - Make a variable w/ only the numbers that are both odd and negative.
numbs16 = [n for n in numbers if n in numbs11 and n in numbs13]

# 17 - Make a variable w/ each number plus five. 
numbs17 = [n+5 for n in numbers]

# B: Make a variable of primes
def is_prime(n):
    if n <= 1: return False
    if n == 2: return True
    for div in range(2, int(sqrt(n)+1)):
        if n%div == 0: return False
    return True

primes = [n for n in numbers if is_prime(n)]



if __name__ == "__main__":
    all_vars = dir()
    for name in all_vars:
        if not name.startswith("__"):
            print(name, eval(name))
