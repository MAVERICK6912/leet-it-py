class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        res=[1]*len(nums)
        prefix=1
        for index in range(len(nums)):
            res[index]=prefix
            prefix*=nums[index]
        postfix=1
        for index in range(len(nums)-1,-1,-1):
            res[index]*=postfix
            postfix*=nums[index]
        return res