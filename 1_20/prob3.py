import sys
sys.path.insert(0,'../')
import lib
import time
then = time.time()

value = 600851475143
answer = 0

for i in range (2,value):
    while(value%i == 0):
        if(i > answer):
            answer = i
        value /= i

now = time.time()

print("Answer",answer)
print(now-then)
