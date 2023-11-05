class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far,max_ending_here=nums[0],nums[0]
        for index in range(1,len(nums)):
            max_ending_here=max(nums[index],max_ending_here+nums[index])
            max_so_far=max(max_so_far,max_ending_here)
        return max_so_far