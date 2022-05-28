list1=[]
list2=[]
for i in range(int(input())):
    name = input()
    score = float(input())
    list1=[score,name]
    list2.append(list1)
        
list2.sort()
list3=[]
list4=[]

for i in range(len(list2)):
    list3.append(list2[i][0])
    list4.append(list2[i][1])

print(list3)
print(list4)

x=min(list3)
print(x)

    



    
        
    


    
