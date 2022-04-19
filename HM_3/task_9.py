"""
9. Write a Python program which keeps a list of people and their corresponding age. (e.g. Mike
Johnson: 3, Jacob Maloney: 56……). Choose the proper data structure. When you run your program it
should ask the user to enter a name, and return the age of that person if he is in the list. If he is not
there, the output should be “I don’t know that person yet”.
"""

my_db = {
     "Mike Johnson": 3,
     "Jacob Maloney": 56,
     "Vankata Petkov": 24
}

user_quarry = input("Enter a name for verification: ")

if user_quarry in my_db:
    for key, value in my_db.items():
        if key == user_quarry:
            print(f"The name {user_quarry} is in our db and he is {my_db[key]} years old")

else:
    print(f" {user_quarry} - I don’t know that person yet")
