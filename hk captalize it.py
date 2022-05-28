s=input()
s1=s.capitalize()
list1=[]
for i in range(len(s)):
    list1.append(s1[i])

for i in range(len(list1)):
    if list1[i]==" ":
        x=list1[i+1].upper()
        list1[i+1]=x
s=""
for i in range(len(list1)):
    s=s+str(list1[i])

print(s)
    


