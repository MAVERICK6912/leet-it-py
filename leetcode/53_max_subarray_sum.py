# Recursive solution
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        return self.find_max_product(0, 0, nums)

    def find_max_product(self, max_so_far, index: int, nums: List[int]) -> int:
        if index == len(nums):
            return max_so_far
        # include number at index
        include = self.find_max_product(max_so_far + nums[index], index + 1, nums)
        # exclude number at index
        exclude = self.find_max_product(nums[index], index + 1, nums)
        if index == 0:
            max_so_far = nums[0]
        return max(max_so_far, max(include, exclude))


# Dynamic Programming Top Down(memoization)
# TC: O(n)
# SC: O(n)+O(n), recursive stack + mem dictionary
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        mem = {}
        return self.find_max_product(float("-inf"), 0, nums, mem)

    def find_max_product(self, max_so_far, index: int, nums: List[int], mem) -> int:
        if index == len(nums):
            return max_so_far
        key = str(index)+'|' + str(max_so_far)
        if key in mem:
            return mem[key]
        # include number at index
        include = self.find_max_product(max_so_far + nums[index], index + 1, nums, mem)
        # exclude number at index
        exclude = self.find_max_product(nums[index], index + 1, nums, mem)
        if index == 0:
            max_so_far = nums[0]
        mem[key] = max(max_so_far, max(include, exclude))
        return mem[key]

# Dynamic Programming Bottom Up(tabulation)
# TC: O(n)
# SC: O(n), mem array
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:        
        mem = [0] * len(nums)
        res = nums[0]
        for index in range(len(nums)):
            mem[index]=max(mem[index-1]+nums[index],nums[index])
            res=max(mem[index],res)        
        return res

# Dynamic Programming Bottom Up(space optimization)
# TC: O(n)
# SC: O(1), no extra space
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_so_far,max_ending_here=nums[0],nums[0]
        for index in range(1,len(nums)):
            max_ending_here=max(nums[index],max_ending_here+nums[index])
            max_so_far=max(max_so_far,max_ending_here)
        return max_so_far