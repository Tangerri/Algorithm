
# 백준 1330.두수비교하기(https://www.acmicpc.net/source/51205263)

a,b = map(int,input().split())

if a>b:
    print(">")    
elif a<b:
    print("<")
elif a==b:
    print("==")