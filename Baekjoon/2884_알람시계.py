
#백준 2884.알람시계(https://www.acmicpc.net/problem/2884)


h,m = map(int, input().split())

if m >= 45:
    print(h,m-45)
elif h>0 and m < 45:
    print(h-1,m+15)
else :
    print(23,m+15)
