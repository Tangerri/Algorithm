
#백준 10950.A+B-3(https://www.acmicpc.net/problem/10950)

## 값을 한번만 입력받는 것이 아니라 여러번 입력받게 됨. 
## 테스트 케이스 개수 T만큼 입력을 받음.

t = int(input())

for i in range(t) :
    a, b=map(int,input().split())
    print(a+b)
    