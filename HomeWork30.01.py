import time

start_time = time.time()

unique_list = [f"Unique string {number}" for number in range(10000)]

print(unique_list)

word = " Hello"
nev_list = [i + word for i in unique_list]
print (nev_list)

not_unique_items = [item for item in unique_list if item in nev_list]
print(f"Not unique items: {not_unique_items}")

print("--- %s seconds ---" % (time.time() - start_time))
