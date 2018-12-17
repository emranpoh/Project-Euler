# MAIN -------------------------------------------------------------------------
import math

count = 0
output = 0
output = math.pow(2,1000)
data = str("%.0f" % (output))
print(list(data))

for i in list(data):
    count = int(i) + count
    print("Count = ",i)

print(count)
