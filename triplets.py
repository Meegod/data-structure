# Complete the compareTriplets function below.
def compareTriplets(a, b):
    pointa=0
    pointb=0
    ar = []
    for i in range(3):
        if a[i]>b[i]:
            pointa+=1
            
        if a[i]<b[i]:
            pointb+=1
    ar.insert(0,pointa)
    ar.insert(1,pointb)        
    return(ar)