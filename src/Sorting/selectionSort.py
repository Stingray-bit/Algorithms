import random
A = []
for i in range(0,10):
    n = random.randint(1,30)
    A.append(n)
print(A)
#A=[8,2,4,9,3]

def selectionSort(A,index=len(A)-1):
    if index==0:
        return A
    else:
        maxnumber=max(A[0:index+1])
        A[A.index(maxnumber)]=A[index]
        A[index]=maxnumber
        return selectionSort(A, index=index-1)
        
        
print(selectionSort(A))