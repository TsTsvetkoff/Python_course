"""
Напишете програма, която врща последните два символа от String. Ако той има по-малко от
два символа, нека да се връща текста “Empty String”.
Пример  : Dimitar
          ar
Приемер 2   : a
            Empty String
"""


def task_4(my_string):
    checker = my_string[-2:]
    if len(checker) < 2:
        print("Empty string")
    else:
        print(checker)


task_4("Dimitar")
