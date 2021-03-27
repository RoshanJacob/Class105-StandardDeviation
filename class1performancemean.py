import csv
import pandas as pd
import plotly.express as px

with open("class1.csv", newline='') as d:
    reader = csv.reader(d)
    fileData = list(reader)

fileData.pop(0)

# newData = []
totalMarks = 0

for i in range(len(fileData)):
    marks = fileData[i][1]
    totalMarks += float(marks)

numberOfStudents = len(fileData)

mean = totalMarks / numberOfStudents
print("The mean is equal to" + ' ' + ':' + ' ' + str(mean))

dataFile = pd.read_csv("class1.csv")

figure = px.scatter(dataFile, x="Student Number", y="Marks")

figure.update_layout(shapes=[
    dict(type="line",
         x0=0, x1=len(fileData),
         y0=mean, y1=mean
         )
])
figure.update_yaxes(rangemode="tozero")

figure.show()
