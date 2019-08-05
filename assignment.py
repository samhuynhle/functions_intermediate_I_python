# Assignment: Functions Intermediate I
# Objectives:
# Practice using default parameter values
# Practice passing in named arguments
# Become familiar with Python's random module
# With this concept of default parameters in mind, the goal of this assignment is to write a single function, randInt() that takes up to 2 arguments.

# If no arguments are provided, the function should return a random integer between 0 and 100.
# If only a max number is provided, the function should return a random integer between 0 and the max number.
# If only a min number is provided, the function should return a random integer between the min number and 100
# If both a min and max number are provided, the function should return a random integer between those 2 values.
# Here are a couple of important notes about using random.random() and rounding.
# (Create this function without using random.randInt() -- we are trying to build that method ourselves for this assignment!)

# random.random() returns a random floating number between 0.000 and 1.000
# random.random() * 50 returns a random floating number between 0.000 and 50.000
# random.random() * 25 + 10 returns a random floating number between 10.000 and 35.000
# round(num) returns the rounded integer value of num
# Here's a little bit of code to get you started, with some test cases and expected outputs.
# Test each function call one at a time and a few times each to make sure you're getting the correct range.

import random #importing Pytho's random module.
def randInt(min=0 , max=100):
    if max < 0:
        return "Sorry, let's make the maximum more than 0."
    elif min > max:
        return "No can do. The minimum is somehow greater than maximum, please set the maximum to be greater than the minimum."
    else:
        num = random.random() * max + min
        num = round(num)
    return num
print(randInt())
print(randInt(max=10000000000))
print(randInt(min=90))
print(randInt(max=25,min=20))
print(randInt(max=10, min=100))
print(randInt(max=-5))
