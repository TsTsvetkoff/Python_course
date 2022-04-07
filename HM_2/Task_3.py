"""
Напишете функция, която приема като аргумент година и връща века.
Пример: 1952
        20
"""


def task3(year):
    century_converter = str(year)
    print(f"Your year {year} is in", int(century_converter[0:2]) + 1, "century")


task3(1952)
