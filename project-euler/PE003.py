#!/bin/python3

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())

    i = 2
    while i * i <= n:
        #print(i)
        while n % i == 0: 
            n = n // i
            if n == i:
                break
        i += 1
    print(n)
