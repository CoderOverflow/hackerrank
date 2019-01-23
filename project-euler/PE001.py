#!/bin/python3

import sys

t = int(input().strip())
for a0 in range(t):
    n = int(input().strip())
    n1=(n-1)//3
    n2=(n-1)//5
    n3=(n-1)//15
    print(3*(n1*(n1+1)//2)+5*(n2*(n2+1)//2)-15*(n3*(n3+1)//2))
