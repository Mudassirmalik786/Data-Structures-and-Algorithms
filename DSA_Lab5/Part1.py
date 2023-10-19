def Partition(A,p,r):
    x= A[r]
    i = p - 1
    for j in range(p, r-1):
        if(A[j]<=x):
            i = j+1
            (A[i],A[j])=(A[j],A[i])
    
    (A[i+1],A[r])=(A[r],A[i+1])
    return i+1

def QuickSort(A,p,r):
    if(p<r):
        q = Partition(A,p,r)
        QuickSort(A,p,q-1)
        QuickSort(A,q+1,r)

#Example usage
A=[10,4,7,9,12]
QuickSort(A,0,len(A)-1)
print(A)