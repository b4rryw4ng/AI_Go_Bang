import time


start = time.time()
print (start)
while True :
    #end = time.time()

    if time.time() - start > 4.8:
        print (time.time() - start)
        break
