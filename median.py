import csv
with open("project_c104\weight.csv",newline="") as f:
    reader=csv.reader(f)
    filedata=list(reader)
filedata.pop(0)
newdata=[]
for i in range(len(filedata)):
    number=filedata[i][2]
    newdata.append(float(number))
n=len(newdata)
newdata.sort()
if (n%2==0):
    median1=float(newdata[n//2])
    median2=float(newdata[n//2-1])
    median=(median1+median2)/2
else:
    median=newdata[n//2]
print("Median is "+str(median))