import sys
sys.path.insert(0,'../')
import lib

val = lib.checkPerfection(28)

for i in range(0,28):
    if(lib.checkPerfection(i) > 0):
        print(i)

print("Answer : ", val)
