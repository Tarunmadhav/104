import csv
with open("dice game\project_c104\weight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][2]
    newdata.append(float(number))
n=len(newdata)
total=0
for i in newdata:
    total=total+i
mean=total/n
print("Mean of weights is "+str(mean))