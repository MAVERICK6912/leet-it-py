# Recursive solution
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        return self.find_max_product(1, 0, nums)

    def find_max_product(self, max_so_far, index: int, nums: List[int]) -> int:
        if index == len(nums):
            return max_so_far
        # include number at index
        include = self.find_max_product(max_so_far * nums[index], index + 1, nums)
        # exclude number at index
        exclude = self.find_max_product(nums[index], index + 1, nums)
        if index == 0:
            max_so_far = nums[0]
        return max(max_so_far, max(include, exclude))

# Dynamic Programming Top Down(memoization)
# TC: O(n)
# SC: O(n)+O(n), recursive stack + mem dictionary
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        mem = {}
        return self.find_max_product(1, 0, nums, mem)

    def find_max_product(self, max_so_far, index: int, nums: List[int], mem) -> int:
        if index == len(nums):
            return max_so_far
        key = str(index) + "|" + str(max_so_far)
        if key in mem:
            return mem[key]
        # include number at index
        include = self.find_max_product(max_so_far * nums[index], index + 1, nums,mem)
        # exclude number at index
        exclude = self.find_max_product(nums[index], index + 1, nums,mem)
        if index == 0:
            max_so_far = nums[0]
        mem[key] = max(max_so_far, max(include, exclude))
        return mem[key]
    
# Dynamic Programming Bottom Up(tabulation)
# TC: O(n)
# SC: O(n)+O(n), max_prod + min_prod arrays
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        max_prod = [0]*len(nums)
        min_prod = [0]*len(nums)
        max_prod[0]=nums[0]
        min_prod[0]=nums[0]
        res=nums[0]
        for index in range(1,len(nums)):
            if nums[index]>=0:
                max_prod[index]=max(nums[index]*max_prod[index-1],nums[index])
                min_prod[index]=min(nums[index]*min_prod[index-1],nums[index])
            else:
                max_prod[index]=max(nums[index]*min_prod[index-1],nums[index])
                min_prod[index]=min(nums[index]*max_prod[index-1],nums[index])
            
            res=max(res,max_prod[index])
        return res


# Dynamic Programming Bottom Up(space optimization)
# TC: O(n)
# SC: O(1), no extra space
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        res=max(nums)
        max_prod,min_prod=1,1
        for num in nums:
            curr_max=max_prod*num
            
            max_prod=max(curr_max,min_prod*num,num)
            min_prod=min(curr_max,min_prod*num,num)

            res = max(res, max_prod)
        return res
