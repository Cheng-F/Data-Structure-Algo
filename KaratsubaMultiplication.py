# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 21:52:51 2020

@author: feng
"""

def KaratsubaMultiplication(num1,num2):
    while num1 > 10 and num2 >10:
        n1 = len(str(num1))
        
        a = int(str(num1)[:n1//2])
        b = int(str(num1)[n1//2:])
        c = int(str(num2)[:n1//2])
        d = int(str(num2)[n1//2:])
        prod1 = KaratsubaMultiplication(a,c)
        prod2 = KaratsubaMultiplication(b,d)
        prod3 = KaratsubaMultiplication((a+b),(c+d))
        prod4 = prod3 - prod2 - prod1
        
        return 10**n1*prod1 + 10**(n1//2)*(prod4) + prod2
    
    return num1 * num2

