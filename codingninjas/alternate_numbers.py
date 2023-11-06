from typing import *
from collections import defaultdict

def alternateNumbers(a : List[int]) -> List[int]:
    # Write your code here.
    signMap=defaultdict(list)
    for index in range(len(a)):
        if a[index]>0:
            signMap["positive"].append(index)
        else:
            signMap["negatives"].append(index)
    ret=[]
    for index in range(len(a)):
        if index%2==0:
            ret.append(a[signMap["positive"].pop(0)])
        else:
            ret.append(a[signMap["negatives"].pop(0)])
    return ret