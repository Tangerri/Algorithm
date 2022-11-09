
# 백준 15552.빠른A+B(https://www.acmicpc.net/problem/15552)

import sys

t = int(input())

for i in range(t):
    a, b=map(int,sys.stdin.readline().split())
    print(a+b)