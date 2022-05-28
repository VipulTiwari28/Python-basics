n=int(input())
x=[]
y=[]
for i in range(n):
    num1=int(input())
    x.append(num1)

print(x)

for i in range(len(x)):
    t=0
    if x[i]==1:
        print("Neither")
    else:
        l=1
        for j in range(1,int(x[i])):
            
            if x[i]%j==0:
                
                t+=1
                
                if t>1:
                    break
                else:
                    continue
            
                
        y.append(t)

print(y)

                    
                
    
        
        
            


