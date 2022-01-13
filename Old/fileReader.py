import csv

points = 0
data = 0
with open('test.csv', newline='', encoding='utf-8') as f:
    points = sum(1 for row in f)

inter = 0
matrix = [[]]

matrix.pop(0)

with open('test.csv', newline='', encoding='utf-8') as f:
    read = csv.reader(f)
    for row in read:
        matrix.append(row)



print(matrix)

input("end")
