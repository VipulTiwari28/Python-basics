def pairs(k, arr):
    
    

    list1=[]
    for i in range(len(arr)):

	    list1.append(arr[i])
    list1.sort(reverse=True)
    t=0
    for i in range(len(list1)):
        for j in range(i+1,len(list1)):
        
            if list1[i]-list1[j]==k:
                    t=t+1
    print(list1)
    print(t)
