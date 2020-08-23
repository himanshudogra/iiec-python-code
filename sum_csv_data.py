import csv
import numpy

with open('students_record.csv', newline='') as f:
    reader = csv.reader(f)
    data = list(reader)

y=numpy.array(data)

z=y[1:,1]

i=0;add=0

while i < len(z):
    add=add+int(z[i])
    i=i+1

print(add)


