"""
Write a Python program which concatenates two text files . In the resulting file separate each in input
file’s content by a destinctive separator line (e.g. “---------------------------------”)
"""

read_only_file_1 = open("task_4_read_file_1.txt", 'r')
read_only_file_2 = open("task_4_read_file_2.txt", 'r')

lines = []
for line in read_only_file_1:
    lines.append(line)


lines.append("\r\n--------------------------------------------------------------------------------------------------- \r\n")

for line2 in read_only_file_2:
    lines.append(line2)

concatenated_file = open("task_4_read_file_output.txt", 'w')

for item in lines:
    concatenated_file.write(item)

