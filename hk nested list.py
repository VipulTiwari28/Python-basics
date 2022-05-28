n=int(input())
dict1={}
for i in range(n):
    name = input()
    score = float(input()) 
    dict1[name]=[score]
      
x1=list(dict1.values())
    
x1.sort()
x2=[x1[1]]
for i in range(2,len(x1)):
    if x1[1]==x1[i]:
        x2.append((x1[i][0]))
            
x1=dict1.items()
x1=list(x1)
name_list=[]
for i in range(len(x1)):
    if x2[0]==x1[i][1]:
        name_list.append(x1[i][0])
        
name_list.sort()
for i in range(len(name_list)):
    print(name_list[i])
    
                    
