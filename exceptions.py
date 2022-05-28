N=int(input())

for i in range(N):
    x=(input().split())
    x1=list(x)
    if x1[1]==0:
        print("Error Code: integer division or modulo by zero")
    elif x1[1]!=int