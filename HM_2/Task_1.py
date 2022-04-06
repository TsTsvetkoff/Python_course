number = int(input("Enter your number for prime verification: "))

if number > 1 and number % number == 0:
    print(f"Your number {number} is prime")
else:
    print(f"Your number {number} is NOT prime")


#TODO - re-factor here