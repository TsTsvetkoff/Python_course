"""
Напишете програма, която връща сумата от цифрите на положително число.
Пример: 456
        15
"""


def task_5(my_number):
    my_list = []
    if my_number > 0:
        get_all_digits = str(my_number)
        for digit in get_all_digits:
            my_list.append(int(digit))
        print(sum(my_list))


task_5(456)
