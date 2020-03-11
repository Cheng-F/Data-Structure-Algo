# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 11:40:07 2020

@author: feng
"""
 
 

def QuickSort(arr,l,r,option):
     
    if l < r:
        (p ,m)  = partition(arr,l,r,option)
        m += QuickSort(arr,l,p,option ) 
        m += QuickSort(arr,p+1,r,option )
        return m
    else:
        return  0
        
     
        
def partition(arr,l,r,option):
    if option == 'first':
        return partition_first(arr,l,r)
    elif option == 'last':
        return partition_last(arr,l,r)
    else:
        return partition_median(arr,l,r)
    

def partition_first(arr,l,r):
    
    pivot = arr[l]
    i = l + 1
     
    for j in range(l+1,r):
        if arr[j] < pivot :
            arr[j], arr[i] = arr[i],arr[j]
            i += 1
    arr[l],arr[i-1] = arr[i-1],arr[l] 
    return (i-1,r-l-1)


def partition_last(arr,l,r):
    pivot = arr[r-1]
    i = l
    for j in range(l,r-1,1):
        if arr[j] < pivot:
            arr[j], arr[i] = arr[i], arr[j]
            i += 1
    arr[r-1],arr[i] = arr[i],arr[r-1]
    return (i, r-l-1)

def partition_median(arr,l,r):
    if (r - l) % 2 == 0:
        p = int(l - 1 + (r - l)/2)
    else:
        p = int(l + (r - l)// 2)
    if arr[l] > arr[p]:
        arr[l], arr[p] = arr[p], arr[l]
    
    if arr[r-1] < arr[l]:
        arr[l], arr[r-1] = arr[r-1], arr[l]
        
    if arr[r-1] < arr[p]:
        arr[p], arr[r-1] = arr[r-1], arr[p]
        
    arr[l], arr[p] = arr[p], arr[l]
    return partition_first(arr,l,r)
    
         
    
if __name__ == "__main__":
    opt = ['first','last','median' ]
    for o in opt:
        with open("QuickSort.txt","r") as f:
            l = [int(i.strip()) for i in f.readlines()]
            print ("{}:{},sample list {}".format(o,QuickSort(l,0,len(l),o),l[20:30]))
            

    



    

    
 