import time

initial_time = time.time()
print(initial_time)

i = 0
while(i<10):
    print("Happy")
    print(time.time() - initial_time)
    i += 1

initial_time2 = time.time()
for i in range(10):
    print("Anurag")
    print(time.time() - initial_time2)
