"""
Напишете функция, която приема като аргумент число и връща лист с делителите му.
Пример: 3
        [1,3]
"""


def task2(number):
    list_with_divisors = []
    for i in range(1, number + 1):
        if number % i == 0:
            list_with_divisors.append(i)
    print(f"All divisors of your {number} are : ", list_with_divisors)


task2(12)
