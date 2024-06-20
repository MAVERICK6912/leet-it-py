# Recursion
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_nums=sum(nums)
        if sum_nums%2!=0:
            return False
        target= sum_nums//2

        return self.partition(target,0,nums)
    
    def partition(self,target,index:int,nums:List[int])->bool:
        if target==0:
            return True
        if index>=len(nums):
            return False
        if target<0:
            return False
        
        # include num at index in subset
        if(self.partition(target-nums[index],index+1,nums)):
            return True
        # exclude num at index in subset
        if(self.partition(target,index+1,nums)):
            return True
        return False


# DP: Top Down
# TC: O(n!)
# SC: O(n)+O(n*target), recursive stack + dp array
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_nums=sum(nums)
        if sum_nums%2!=0:
            return False
        target= sum_nums//2
        dp=[[-inf]*(target+1)for _ in range(n)]
        return self.partition(target,0,nums,dp)
    
    def partition(self,target,index:int,nums,dp:List[int])->bool:
        if target==0:
            return True
        if index>=len(nums):
            return False
        if target<0:
            return False
        if dp[index][target]!=-inf:
            return dp[index][target]
        # include num at index in subset
        if self.partition(target-nums[index],index+1,nums,dp):
            dp[index][target]=True
            return dp[index][target]
        # exclude num at index in subset
        if self.partition(target,index+1,nums,dp):
            dp[index][target]=True
            return dp[index][target]
        dp[index][target]=False
        return dp[index][target]


# DP: Bottom Up
# TC: O(n*target)
# SC: O(n*target), dp array
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_nums=sum(nums)
        if sum_nums%2!=0:
            return False
        target= sum_nums//2
        dp=[[False]*(target+1)for _ in range(n+1)]

        # initial conditions
        # when target is zero
        for i in range(n+1):
            dp[i][0]=True

        for i in range(1,n+1):
            for j in range(1,target+1):
                # include number in subset
                if nums[i-1]<=j:
                    dp[i][j]=dp[i-1][j-nums[i-1]]
                # exclude number from subset
                dp[i][j]=dp[i][j] or dp[i-1][j]
        return dp[n][target]


# DP: Space Optimization
# TC: O(n*target)
# SC: O(target)+O(target), prev+curr
class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n=len(nums)
        sum_nums=sum(nums)
        if sum_nums%2!=0:
            return False
        target= sum_nums//2
        
        prev,curr=[False]*(target+1),[False]*(target+1)
        # initial conditions
        prev[0],curr[0]=True,True
        
        for i in range(1,n+1):
            for j in range(1,target+1):
                # include number in subset
                if nums[i-1]<=j:
                    curr[j]=prev[j-nums[i-1]]
                # exclude number from subset
                curr[j]=curr[j] or prev[j]
            prev=curr[:]
        return curr[target]