import csv
import math

with open("class1.csv", newline='') as m:
    reader = csv.reader(m)
    fileData = list(reader)

fileData.pop(0)

totalMarks = 0

for x in range(len(fileData)):
    marks = fileData[x][1]
    totalMarks += float(marks)

numberOfStudents = len(fileData)

mean = totalMarks / numberOfStudents

squaredList = []
numeratorSummation = 0

for n in range(len(fileData)):
    number = fileData[x][1]
    numerator = float(number) - float(mean)
    numerator = numerator**2
    squaredList.append(float(numerator))
    numeratorSummation += float(numerator)

denominator = (len(fileData) - 1)

standardDeviation = math.sqrt(numeratorSummation / denominator)

print("The standard deviation is" + ' ' + ":" + ' ' + str(standardDeviation))
