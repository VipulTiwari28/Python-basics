n = int(input())
arr = map(int, input().split())
    
    
x3=list(arr)
x1=max(x3)
x3.sort()    
for i in range(len(x3)):
    k=n-1
    while k>=0:
        if x3[k]<x1:
            x2=x3[k]
            k=k-1
        else:
            k=k-1
                
                
print(x2)    
