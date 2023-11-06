class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        breakPoint,n=-1,len(nums)
        for index in range(n-2,-1,-1):
            if nums[index]<nums[index+1]:
                breakPoint=index
                break        
        if breakPoint==-1:
            nums[:]=nums[::-1]
            return
        for index in range(n-1,breakPoint,-1):
            if nums[index]>nums[breakPoint]:
                nums[index],nums[breakPoint]=nums[breakPoint],nums[index]
                break        
        nums[breakPoint+1:]=nums[breakPoint+1:][::-1]