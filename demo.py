import csv

fields = ['Name', 'Branch', 'Year', 'CGPA']

rows = [ ['Nikhil', 'COE', '2', '9.0'],['Sanchit', 'COE', '2', '9.1'],['Aditya', 'IT', '2', '9.3'] ]

filename = 'record.csv'

with open(filename, 'w') as csvfile:
    csvwriter = csv.writer(csvfile)
    csvwriter.writerow(fields)
    csvwriter.writerows(rows)

print ('done !!')