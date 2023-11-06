from typing import *

def nextGreaterPermutation(A : List[int]) -> List[int]:    
    breakPoint,n=-1,len(A)
    for index in range(n-2,-1,-1):
        if A[index]<A[index+1]:
            breakPoint=index
            break
    if breakPoint==-1:
        return A[::-1]
    for index in range(n-1,breakPoint,-1):
        if A[index]>A[breakPoint]:
            A[index],A[breakPoint]=A[breakPoint],A[index]
            break
    A[breakPoint+1:]=A[breakPoint+1:][::-1]
    return A