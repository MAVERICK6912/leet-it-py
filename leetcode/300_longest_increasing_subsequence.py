# Dynamic Programming(Top Down)
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        return self.findLIS(0,-inf,nums)
    def findLIS(self,index,prev:int,nums:List[int])->int:
        # base case
        if index==len(nums):
            return 0
        # length of LIS found when number oat index is included
        include=0
        # include the number at index if it is greater than prev
        if nums[index]>prev:
            # since we have included number at index
            # we will increment by 1(this number is part of LIS)
            include= 1+self.findLIS(index+1,nums[index],nums)
        # since we're excluding number at index
        # we move to next position to check if it
        # can be part of LIS
        exclude= self.findLIS(index+1,prev,nums)
        # we return max of include and exclude
        # as both of them can give solutions
        return max(include,exclude)
    

# Dynamic Programming(Top Down)
# TC: O(n!)
# SC: O(n)+O(n), recursive stack+mem array
class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # mem represents length of LIS till ith index
        mem = [-inf] * (len(nums)+1)
        self.findLIS(0, -inf,0, nums, mem)        
        return mem[-1]

    def findLIS(self, index, prev,curr_lis: int, nums, mem: List[int]) -> int:
        # base case
        if index == len(nums):
            # we return max of include and exclude
            # as both of them can give solutions
            mem[index] = max(mem[index], curr_lis)
            return mem[index]

        if mem[index] != -inf:
            return mem[index]
        # length of LIS found when number oat index is included
        include = 0
        # include the number at index if it is greater than prev
        if nums[index] > prev:
            # since we have included number at index
            # we will increment by 1(this number is part of LIS)
            self.findLIS(index + 1, nums[index],curr_lis+1, nums, mem)
        # since we're excluding number at index
        # we move to next position to check if it
        # can be part of LIS
        self.findLIS(index + 1, prev,curr_lis, nums,mem)
    

# Dynamic Programming(Bottom Up)
# TC:O(n^2)
# SC:O(n), mem array
class Solution:    
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        n=len(nums)
        # mem represents the LIS including nums[index] or current number
        mem=[1]*n
        res=1
        for i in range(1,n):
            for j in range(i):
                # we will only check for LIS if nums[i]>nums[j]
                # and we get a better answer, i.e: mem[i]<=mem[j]
                if nums[i] > nums[j] and mem[i] <= mem[j]:
                    mem[i]=mem[j]+1
            res=max(res,mem[i])        
        return res
