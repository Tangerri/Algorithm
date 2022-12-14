

# 백준 1110.더하기 사이클(https://www.acmicpc.net/problem/1110)

## case 1
### 26 -> 2+6=8 -> 68 -> 6+8=14 -> 84 -> 8+4=12 -> 42 -> 4+2=6 -> 26
### 26 값을 받으면 4번의 사이클 길이를 가짐. 

## case 2 
### 1 -> 0+1=1 -> 11 -> 1+1=2 -> 12 -> 1+2=3 ... 

## 로직
### 반복) 입력값의 각 자리 값 더하기 -> 입력값[1]합한값[1] = 출력값
### 중지) 입력값 = 출력값

n = input()    # 입력값 ex.26
num = N        # 비교값 
cycle = 0      # 사이클 값 

while True:
    a = num//10      #2
    b = num%10       #6
    c = (a+b)%10     #8
    num = (b*10)+c   #60+8=68

    cnt = cnt+1
    if(num == n):
        break

print(cnt)




