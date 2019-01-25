import sys


t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    p, c, s = 0, 2, 0
    while c <= n:
        s += c
        p, c = c, p + 4 * c
    print(s)
