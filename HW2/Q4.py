import time

def hashfunc(k, m):
    a = 1664525
    b = 1013904223
    return (a * k + b) % m

for n in [16, 64, 256, 1024, 4096, 16384]:
    for m in [1000000000, 10000000000]:
        start_time = time.time()
        table = [0] * m
        for i in range(n):
            key = hashfunc(i, m)
            table[key] += 1
        end_time = time.time()
        print(f"n={n}, m={m}, time={end_time-start_time}")
