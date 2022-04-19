"""
Write a Python function to multiply all the numbers in a list.
Sample: [3,6,2]
         36
"""


def list_multiply(my_list):
    result = 1
    for x in my_list:
        result = result * x
    return result


my_list = [3, 6, 2]

print(list_multiply(my_list))
