"""
Напишете програма, която принтира таблицата за умножение (от 1 до 5) за число, въведено
от потребителя.
Пример: 6
         6 x 1 = 6
         6 x 2 = 12
         6 x 3 = 18
         6 x 4 = 24
         6 x 5 = 30

"""

user_number = int(input("Enter your number please: "))
count = 0
for i in range(5):
    result = (user_number * (count+1))
    count += 1
    print(f"{user_number}" + " x " + str(count) + " = "+str(result))
