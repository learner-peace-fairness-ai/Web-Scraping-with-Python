import csv

with open('test.csv', 'w+', newline='', encoding='utf-8') as csv_file:
    writer = csv.writer(csv_file)
    writer.writerow(('number', 'number plus 2', 'number times2'))
    for i in range(10):
        writer.writerow((i, i+2, i*2))
