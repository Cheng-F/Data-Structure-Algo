# -*- coding: utf-8 -*-
"""
Created on Wed Mar  4 21:38:16 2020

@author: feng
"""

def mergeSort(A):
    if len(A)>1:
        if len(A) % 2 == 0:
            m = int(len(A)/2)
        else:
            m = int((len(A) + 1)/2)
        left = A[:m]
        right = A[m:]
       
        mergeSort(left)
       
        mergeSort(right)

        
        i = 0
        j = 0
        k = 0
        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                A[k] = left[i]
                i += 1
            else:
                A[k] = right[j]
                j += 1
            k += 1
        if i < len(left):
            A[k:] = left[i:]
                    
        else:
            A[k:] = right[j:]
         
                
    return A