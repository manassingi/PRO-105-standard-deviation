import csv
import math
from numpy import mod, square
from numpy.core.fromnumeric import mean

with open('myData.csv', newline='') as n:
    reader = csv.reader(n)
    my_data = list(reader)


#To remove headers from CSV

data= my_data[0]
def mean_data(data) :
    total_marks = 0
    total_entries = len(data)

    for marks in data:
        total_marks += int(marks)

    mean = total_marks / total_entries
    return mean


squarelist = []
for number in data :
    a= int (number) - mean_data(data)
    a= a**2
    squarelist.append(a)
sum =0
for w in squarelist :
    sum = sum+w
standard_data = sum/(len(data)-1)
standard_deviation= math.sqrt(standard_data)
print(standard_deviation)