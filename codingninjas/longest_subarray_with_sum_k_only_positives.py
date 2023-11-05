# two pointer approach where both pointers start at the same index
# we keep going right until we find the sum==k
# if sum>k we keep moving left pointer until either sum<k or left<=right
def longestSubarrayWithSumK(a: [int], k: int) -> int:
    right,left=0,0
    sum,subArrayLen=a[0],0
    while right<len(a):
        while left<=right and sum>k:
            sum-=a[left]
            left+=1
        if sum==k:
            subArrayLen=max(subArrayLen,right-left+1)        
        right+=1
        if right<len(a):
            sum+=a[right]
    return subArrayLen