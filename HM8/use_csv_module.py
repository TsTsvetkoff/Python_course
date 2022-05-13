import read_csv as rd
from csv import reader


rd.headings = ['Име', 'Телефон', 'Електронен адрес', 'Град', 'Адрес', 'Пол']
rd.headings_width = []


rd.open_csv("sample_data.csv")

with open('sample_data.csv', mode='r') as csv_file:
    csv_reader = reader(csv_file)
    for x in csv_reader:
        rd.people_list.append(x)


rd.make_table()
rd.draw_table()
#   RCA : the issue is that the people_list is empty in read_csv.py
#   Action : just introduce a csv reader and append the empty people list (rows 11-14)

