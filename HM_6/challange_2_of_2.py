"""
print how many times word "Python" is presented in the example.txt
"""

search_word = 'Python'
count_word = 0

with open('challeng_2.txt', 'r') as my_read_file:
    for line in my_read_file:
        for wrd in line.split(" "):
            if search_word == wrd:
                count_word += 1

print(f"In the given text the '{search_word}' has been found {count_word} times")
