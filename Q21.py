# Write a Python program to print all unique values in a dictionary.
d=[{"V":"S001"}, {"V": "S002"}, {"VI": "S001"}, {"VI": "S005"}, {"VII":"S005"},
{"V":"S009"},{"VIII":"S007"}]
i=0
c=[]
while i<len(d):
    for j in d[i].values():
        c.append(j)
    i+=1
# print(c)
k=0
b=[]
while k<len(c):
    s=0
    count=0
    while s<len(c):
        if c[k]==c[s]:
            count+=1
            if count<2:
                if c[k] not in b:
                    b.append(c[s])
        s+=1
    k+=1
print(b)