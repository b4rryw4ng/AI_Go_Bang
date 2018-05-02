import time


start = time.time()
print (start)
while True :
    end = time.time()

    if end - start > 4.8:
        print (end - start)
        break


#return 