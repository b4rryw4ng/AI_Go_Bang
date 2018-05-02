a = [1,5,9,10,14,65,85,95,105]
ID = 99
for index, i in enumerate(a):
    
    if i > ID:
        a.insert(index, ID) 
        break  

print (a)