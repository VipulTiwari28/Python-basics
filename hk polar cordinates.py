
      
import cmath
x=input()
if x[0]=="-":
    
    if x[3]=="+":
        i=int(x[1:3])
        j=int(x[4:6])
        x1=cmath.phase(complex(-i,j))
        x2=abs(complex(-i,j))
    
    elif x[3]=="-":
        i=int(x[1:3])
        j=int(x[4:6])
        x1=cmath.phase(complex(-i,-j))
        x2=abs(complex(-i,-j))
    elif x[2]=="+":
        i=int(x[1:2])
        j=int(x[3:4])
        x1=cmath.phase(complex(-i,j))
        x2=abs(complex(-i,j))
        
    elif x[2]=="-":
        i=int(x[1:2])
        j=int(x[3:4])
        x1=cmath.phase(complex(-i,-j))
        x2=abs(complex(-i,-j))
        
else:
    if x[2]=="+":
        i=int(x[0:2])
        j=int(x[3:5])
        x1=cmath.phase(complex(i,j))
        x2=abs(complex(i,j))
    
    elif x[2]=="-":
        i=int(x[0:2])
        j=int(x[3:5])
        x1=cmath.phase(complex(i,-j))
        x2=abs(complex(i,-j))
    elif x[1]=="+":
        i=int(x[0:1])
        j=int(x[2:3])
        x1=cmath.phase(complex(i,j))
        x2=abs(complex(i,j))
        
    elif x[1]=="-":
        i=int(x[0:1])
        j=int(x[2:3])
        x1=cmath.phase(complex(i,-j))
        x2=abs(complex(i,-j))



print(x1)
print(x2)

    


















    
