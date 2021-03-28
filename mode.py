import csv
from collections import Counter
with open("project_c104\weight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][2]
    newdata.append(float(number))
data=Counter(newdata)
for height,occurance in data.items():
    if occurance==max(list(data.values())):
        print(height,occurance)