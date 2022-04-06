my_list = [2, 5, 10]
count = 0

while count < 3:
    guess_my_number = int(input("Please enter your number for verification: "))
    if guess_my_number in my_list:
        print(True, f"Congrats you got it your number {guess_my_number} is in the list")
        break
    else:
        print(False, f"Try again, your number {guess_my_number} is not in the list. More luck next time."
                     f"You have {2 - count} attempts left")
        count += 1

