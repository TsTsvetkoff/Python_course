"""
Напишете програма, която проверява дали даден String може да бъде преобразуван в Integer.
Пример : “building”
         This is not an integer
Пример 2: “22”
         Yes, 22 can be represented as an integer.
"""


def task_6(check_this):
    is_int = True
    try:
        int(check_this)
    except ValueError:
        is_int = False
    if is_int:
        print('This value IS an integer')
    else:
        print('This is NOT an integer')


task_6("building")
