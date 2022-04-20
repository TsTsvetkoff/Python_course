"""
В лист от думи съставен от BG и EN думи , да преброим колко са BG думи и колко са EN думи
"""

mixed_list = ['Коч', 'Python', 'Бира', 'Metamorphosis', 'Скара', "Лято", 'Summer']


en_counter = 0
bg_counter = 0
for i in mixed_list:
    if ord(i[0]) < 128:
        en_counter += 1
    else:
        bg_counter += 1

print(f"Българските думи са {bg_counter} на брой, а Анлийските са {en_counter} на брой")


