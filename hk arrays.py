n = int(input())

arr = list(map(int, input().rstrip().split()))
x=list(arr)
    
for i in range(int(n/2)):
    x[i],x[n-i-1]=x[n-i-1],x[i]
        
str1=""
for j in range(len(x)):
    str1=str1+" "+str(x[j])

str2=""
for k in range(len(str1)):
    if k!=0:
        str2=str2+str(str1[k])

print(str2)

        
