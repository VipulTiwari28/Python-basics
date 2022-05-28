n,m=(input().split())
arr_1=(input().split(" ",int(n)))
A=(input().split(" ",int(m)))
B=(input().split(" ",int(m)))
score=0
for i in range(len(A)):
    for j in range(len(arr_1)):
        if A[i]==arr_1[j]:
            score=score+1
            
        if B[i]==arr_1[j]:
            score=score-1
            

        

print(score)