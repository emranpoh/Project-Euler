import time
then = time.time()

prime_list = []
prime_sum = 0

n = 2000000

for i in range(2, n+1):
    if i not in prime_list:
        prime_sum += i
        for j in range(i*i, n+1, i):
            prime_list.append(j)

now = time.time()
print("Answer", prime_sum)
print(now-then , "sec")
