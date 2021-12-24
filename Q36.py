d=[{'key1': 1, 'key2': 3, 'key3': 2}, {'key1': 1, 'key2': 2},{'key1':9,'key3':2}]
count=0
for i in d:
    for j in i:
        if j=='key1':
            count+=1
            if count>=2:
                pass
                print(j,count)
