
import time
start_time = time.time()

n = 10000
A = ["Hello"] * n
print (A)

b = " world!"
c = [i+b for i in A]
print (c)

print("--- %s seconds ---" % (time.time() - start_time))