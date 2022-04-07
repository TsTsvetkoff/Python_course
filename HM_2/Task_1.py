"""
Напишете функция, която проверява дали дадено число е просто.
Пример: 43
        43 is prime number
"""


def task1(number):
    if number > 1:
        for i in range(2, number):
            if number % i == 0:
                print(f"Your number {number} is NOT prime")
                break
        else:
            print(f"Your number {number} IS prime")
    else:
        print("Please enter a greater than 1 number")


task1(43)