"""
Write a Python program to read a random line from a file.
"""

import random

read_only_file = open("task_2_read_file.txt", 'r')
random_line = random.randrange(8) #The text file has 8 rows

lines = []
for line in read_only_file:
    lines.append(line)

print(lines[random_line])



