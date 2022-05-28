def sort_array(a):
        
    m=0
    for i in range(len(a)):
        for j in range(len(a)-1):
            if a[j]>a[j+1]:
                x=a[j]
                a[j]=a[j+1]
                a[j+1]=x
                m+=1
                print(m)
            else:
                
                continue
    print("Array is sorted in",m,"swaps.")
    
list1=[]        
n=int(input())
x=list(input().split())
for i in range(len(x)):
    num1=x[i]
    list1.append(int(num1))
    
    
a=list1
sort_array(a)

print("First Element:",a[0])
print("Last Element:",a[len(a)-1])
