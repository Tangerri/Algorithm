
#백준 2884.알람시계(https://www.acmicpc.net/problem/2884)


hh = int(input())
mm = int(input())

print(((hh*60)+mm-45)//60, ((hh*60)+mm-45)%60)