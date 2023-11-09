def superiorElements(a : List[int]) -> List[int]:
    # Write your code here.
    superior=[]
    max=-1
    for index in range(len(a)-1,-1,-1):
        if a[index]>max:
            superior.append(a[index])
            max=a[index]
    superior.sort()  # since the returned value is expected to be sorted
    return superior