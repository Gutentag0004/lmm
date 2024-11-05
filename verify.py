
import math

file = open("true.txt","r")
res = open("result.csv","r")
trueRes = []
for i in file.readlines():
    trueRes.append(i.strip())

print(trueRes)
total = 104
onTarget = 0
count = 1
for i in res.readlines():
    count +=1
    if count >= total:
        break
    r = i.strip().split(",")
    
    idx = int(r[3])
    matched = "-"
    
    if(math.fabs(int(trueRes[idx -1]) -  int(r[1])) < 10000):
        onTarget+=1
        matched = "+"
    print(r[0],r[2], trueRes[idx -1], r[1], matched, math.fabs(int(trueRes[idx -1]) -  int(r[1])))
print(onTarget)



