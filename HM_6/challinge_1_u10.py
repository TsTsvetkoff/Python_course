import xlwings as xw

xl_data = [{'name': 'Bate_Cveti', 'age': 33, 'height': 190, 'weight': 100},
           {'name': 'Peshkata', 'age': 23, 'height': 150, 'weight': 150},
           {'name': 'Na_Peshkata_brat_mu', 'age': 32, 'height': 110, 'weight': 110},
           {'name': 'Kolio', 'age': 13, 'height': 100, 'weight': 100},
           {'name': 'Ganio', 'age': 55, 'height': 900, 'weight': 900},
           {'name': 'Na_ganio_bra4ed_mu', 'age': 25, 'height': 120, 'weight': 120},
           ]


totals = [{'name': 'Totals', 'age': f'=SUM(B2:B{len(xl_data)+1})', 'height': f'=SUM(C2:C{len(xl_data)+1})', 'weight':
    f'=SUM(D2:D{len(xl_data)+1})'}]

with open('my_sheet.csv', 'w') as my_file:
    my_file.write('Name;Age;Height;Weight\n')

    for x in xl_data:
        my_file.write(f"{x['name']};{x['age']};{x['height']};{x['weight']}\n")

    for tot in totals:
        my_file.write(f"{tot['name']};{tot['age']};{tot['height']};{tot['weight']}\n")


def write_data_to_excel(workbooklocation,sheetname,columnletter):
    wb = xw.Book(workbooklocation)
    X = wb.sheets[sheetname].range(columnletter + str(wb.sheets[sheetname].cells.last_cell.row)).end('up').row + 1
    cell = columnletter + str(X)
    print(cell)
    return cell

write_data_to_excel('my_sheet.csv','my_sheet','A')
