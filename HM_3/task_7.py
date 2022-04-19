"""
Write a Python program to find the single element which appears once in a list where every element
appers two times except for one/
Sample: [2,2,3,4,3]
              4
"""

my_list = [2, 2, 3, 4, 3]


def list_unique(my_list):
    for numb in my_list:
        if my_list.count(numb) != 1:
            continue
        else:
            print(numb)


list_unique(my_list)
