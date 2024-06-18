# Recursive solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(self.lets_rob(0,nums),self.lets_rob(1,nums))
    def lets_rob(self,curr_house:int,loot:List[int]):
        if curr_house>=len(loot):
            return 0
        
        rob=loot[curr_house]+self.lets_rob(curr_house+2,loot)

        dont_rob=self.lets_rob(curr_house+1,loot)
        return max(rob,dont_rob)

# Dynamic Programming: Top Down
# TC: O(n)
# SC: O(n)+O(n), recursive stack + dp array
class Solution:
    def rob(self, nums: List[int]) -> int:
        dp=[-inf]*len(nums)
        return max(self.lets_rob(0,nums,dp),self.lets_rob(1,nums,dp))
    def lets_rob(self,curr_house:int,loot,dp:List[int]):
        if curr_house>=len(loot):
            return 0
        if dp[curr_house]!=-inf:
            return dp[curr_house]
        rob=loot[curr_house]+self.lets_rob(curr_house+2,loot,dp)

        dont_rob=self.lets_rob(curr_house+1,loot,dp)
        dp[curr_house]= max(rob,dont_rob)
        return dp[curr_house]

# Dynamic Programming: Bottom Up
# TC: O(n)
# SC: O(n), dp array
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)
        dp=[0]*(len(nums))
        dp[0],dp[1]=nums[0],max(nums[0],nums[1])
        for index in range(2,len(nums)):
            dp[index]=max(nums[index]++dp[index-2],dp[index-1])
        return dp[-1]

# Dynamic Programming: Space Optimization
# TC: O(n)
# SC: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums)<3:
            return max(nums)        
        prev_rob,curr_rob=nums[0],max(nums[0],nums[1])
        for index in range(2,len(nums)):
            prev_rob,curr_rob=curr_rob,max(nums[index]+prev_rob,curr_rob)
        return max(prev_rob,curr_rob)