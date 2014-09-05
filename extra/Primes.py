import math
for n in range(1,100):
    prime = 0
    for i in range(2,n):
        if n%i == 0:
            prime = 1
    if prime == 1:
        print n

