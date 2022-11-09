
# 백준 10952.A+B-5(https://www.acmicpc.net/problem/10952)


# 입력값을 계속 받다가 0,0이면 중단되어야 하므로 while 사용
while 1:
    a,b=map(int, input().split())
    if (a==0 & b==0):
        break
    else:
        print(a+b)


