my_list = []
first_number = int(input("Please enter your first number out of 3: "))
second_number = int(input("Please enter your second number out of 3: "))
third_number = int(input("Please enter your third number out of 3: "))

my_list.extend([first_number, second_number, third_number])
print(f"Based on your input {first_number}, {second_number} and {third_number} the max is : ", max(my_list))
