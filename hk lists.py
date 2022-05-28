N = int(input())
list1=[]
for i in range(N):
    command=list(input().split())
    list1.append(command)
list2=[]    
for i in range(len(list1)):
    if list1[i][0]=='insert':
        list2.insert(int(list1[i][1]),int(list1[i][2]))
    elif list1[i][0]=='remove':
        list2.remove(int(list1[i][1]))
    elif list1[i][0]=='append':
        list2.append(int(list1[i][1]))
    elif list1[i][0]=='pop':
        list2.pop()
    elif list1[i][0]=='sort':
        list2.sort()
    elif list1[i][0]=='reverse':
        list2.reverse()
    elif list1[i][0]=='print':
        print(list2)
