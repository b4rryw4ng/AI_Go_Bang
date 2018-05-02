import time


start = time.time()
print (start)
a = 0
b = 0
while True :
    #end = time.time()
    a += 1
    if a == 10000000:
        b+=1
        a =0
    if time.time() - start > 4.9:
        
        break


print (b,a)