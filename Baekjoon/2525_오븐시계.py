
#백준 2525.오븐 시계(https://www.acmicpc.net/problem/2525)

a, b = map(int,input().split())
c = int(input())

a += c//60
b += c%60

print(a,b)

if b>=60:
    a += 1
    b -=60

if a>=24:
    a-= 24

print(a,b)