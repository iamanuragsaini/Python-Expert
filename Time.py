import time

initial_time = time.time()
print(initial_time)

local_time = time.asctime(time.localtime(time.time()))
print(local_time)