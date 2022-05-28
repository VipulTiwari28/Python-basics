def diagonalDifference(arr):
    m=0
    t=0
    for i in range(len(arr)):
        
        m=m+(arr[i][i])
    for k in range(len(arr)):
        t=t+(arr[k][2-k])
        
    if m>t:
        z=m-t
    else:
        z=t-m
    return z
        
