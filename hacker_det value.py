import numpy
n=int(input())
list1=[]
for i in range(n):
    list2=[]
    
    x=map(float,input().split())
    x=list(x)
    
    list1.append(x)
    
    
arr=numpy.array(list1)
arr1=numpy.linalg.det(arr)
print("%0.2f"%(arr1))