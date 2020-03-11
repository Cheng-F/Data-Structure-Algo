# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 23:01:47 2020

@author: feng
"""
from mergesort import mergeSort
def Count_Inversions(arr):
    while len(arr) > 2:
        l = Count_Inversions(arr[:len(arr)//2])
        r = Count_Inversions(arr[len(arr)//2:])
        m = Count_Split(arr[:len(arr)//2],arr[len(arr)//2:])
        return l + r + m
    return bool(arr[1:] and arr[0] > arr[1])
     
    
  
        
def Count_Split(arr1,arr2):
    arr1 = mergeSort(arr1)
    arr2 = mergeSort(arr2)
    i = j = n = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] > arr2[j]:
            n += len(arr1) - i
            j += 1
        else:
            i += 1
    return n 

if __name__ == "__main__":
    with open("IntegerArray.txt","r") as file:
        l = [int(i.strip()) for i in file.readlines()]
     
    print ("Total inversions are {}".format( Count_Inversions(l)))
    

