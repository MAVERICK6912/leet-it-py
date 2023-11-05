def longestSubarrayWithSumK(a: [int], k: int) -> int:
    prefixSumMap={}
    prefixSum,subArrayLen=0,0   
    for index in range(len(a)):
        prefixSum+=a[index]
        if prefixSum==k:
            subArrayLen=max(subArrayLen,index+1)
        remainingSum=prefixSum-k
        if prefixSumMap.get(remainingSum,-1)!=-1:
            subArrayLen=max(subArrayLen,index-prefixSumMap.get(remainingSum))
        if prefixSumMap.get(prefixSum,-1)==-1:
            prefixSumMap[prefixSum]=index
    return subArrayLen