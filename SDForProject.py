import math
import csv

with open("dataForProject.csv") as f:
    reader=csv.reader(f)
    filedata=list(reader)
data = filedata[0]
def mean(data):
    n=len(data)
    total=0
    for i in data:
        total=total+int(i)
    mean=total/n
    print("mean",mean)
    return mean
squareList=[]
for num in data:
    a=int(num)-mean(data)
    a=a**2
    squareList.append(a)
sum=0
for i in squareList:
    sum=sum+i
result=sum/(len(data)-1)
sd=math.sqrt(result)
print("Standard Deviation",sd)