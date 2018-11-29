A = [10,16,18,12,11,13,15,17,14,19]
def left(i):
    return 2* i + 1
def right(i):
    return 2 * i + 2 
def parent(i):
    return (i+1)//2 - 1
def maxHeap(A,i):
    l = left(i)
    r = right(i)
    if l <  len(A) and A[l] > A[i]:
        largest = l
    else:
        largest = i

    if r < len(A) and A[r] > A[largest]:
        largest = r
    if largest != i:
        A[i],A[largest] = A[largest],A[i]
        maxHeap(A,largest)
    return A
def buildMaxHeap(A):
    low_parent = parent(len(A)-1)
    for i in range(low_parent,-1,-1):
        maxHeap(A,i)

def heapSort(A):
    buildMaxHeap(A)
    heap_size = len(A) - 1
    idx = -1
    for i in range(heap_size,0,-1):
        A[i],A[0] = A[0],A[i]
         
        A[:idx] = maxHeap(A[:idx],0)
        idx -= 1

        

        
        
        
    

    
