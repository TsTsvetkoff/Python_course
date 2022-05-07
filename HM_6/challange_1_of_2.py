"""
# Challenge ;)
# Transform data to csv file and open filled file with MS Excel automatically (if you are on Windows)

# Python dictionary with initial data

"""
import os

my_data = [{"name": 'John Doe', "department": 'Marketing', "position": 'Analyst', "salary": 1500},
           {"name": 'Peter Jackson', "department": 'Sales', "position": 'Consultant', "salary": 1200},
           {"name": 'Kate Richardson', "department": 'Sales', "position": 'Consultant', "salary": 1400},
           {"name": 'Jane Peterson', "department": 'Sales', "position": 'Director', "salary": 1700}]

with open("challange1.csv", 'w') as challange1:
    challange1.write("name;department;position;salary\n")

    for i in my_data:
        challange1.write(f"{i['name']};{i['department']}; {i['position']};{i['salary']}\n")


os.startfile("challange1.csv")
