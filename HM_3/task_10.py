"""
Write a recursive Python function to calculate the value of 'a' to the power 'b'. Do not use the math
module.
Sample: power(2,3)
            8
"""


def power(a, b):
    if b == 0:
        return 1
    else:
        return a*power(a, b-1)


print("Result=", power(2, 3))

