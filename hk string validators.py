s = input()
a,b=0,0
for i in range(len(s)):
    if s[i].isalpha()==True:
        a=a+1
    elif s[i].isnumeric()==True:
        b=b+1
x="True"
y="false"
t,m,z,l=0,0,0,0
for i in range(len(s)):
    if s[i].isalpha()==True:
        t=t+1
        
            
    if s[i].isdigit()==True:
        m=m+1
        
            
    if s[i].islower()==True:
        z=z+1

    if s[i].isupper()==True:
            l=l+1



if a>0 and b>0:
    print(x)
elif a==0 and b==0:
    print(y)
if t>0:
    print(x)
elif t==0:
    print(y)
if m>0:
     print(x)
elif m==0:
    print(y)
if z>0:
    print(x)
elif z==0:
    print(y)
if l>0:
    print(x)
elif l==0:
    print(y) 
