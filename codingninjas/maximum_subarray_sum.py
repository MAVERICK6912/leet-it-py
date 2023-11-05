from os import *
from sys import *
from collections import *
from math import *

from sys import stdin,setrecursionlimit
setrecursionlimit(10**7)

def maxSubarraySum(arr, n) :
    max_so_far,max_ending_here=arr[0],arr[0]
    for index in range(1,n):
        max_ending_here=max(arr[index],max_ending_here+arr[index])
        max_so_far=max(max_so_far,max_ending_here)
    return max_so_far