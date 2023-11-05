def majorityElement(v: [int]) -> int:
    candidate,count=None,0
    for num in v:
        if count==0:
            candidate=num
            count+=1
        elif num==candidate:
            count+=1
        else:
            count-=1
    return candidate    
