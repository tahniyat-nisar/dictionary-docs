#output: [[1, 'red'], [2, 'green'], [3, 'black'], [4, 'white'], [5, 'black']]
d={1: 'red', 2: 'green', 3: 'black', 4: 'white', 5: 'black'}
c=[]
for k,v in d.items():
    c.append([k,v])
print(c)