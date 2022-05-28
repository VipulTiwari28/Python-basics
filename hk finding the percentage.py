x1=[]
dict1={}
n=int(input())
for i in range(n):
    x=(input().split())
    x1.append(list(x))
    dict1[i][0]={int(x1[i][1]),int(x1[i][2]),int(x1[i][3])}

print(dict1)



