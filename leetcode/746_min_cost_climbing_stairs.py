# Recursive solution
# TC:O(2^n)
# SC: O(n)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        return min(self.find_min_cost(0,cost),self.find_min_cost(1,cost))
    def find_min_cost(self,index:int,cost:List[int])->int:
        if index>=len(cost):
            return 0
        return cost[index]+min(self.find_min_cost(index+1,cost),self.find_min_cost(index+2,cost))

# DP: Top Down
# TC:O(n)
# SC: O(n)+O(n), recursive stack, dp array
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp=[-inf]*len(cost)
        return min(self.find_min_cost(0,cost,dp),self.find_min_cost(1,cost,dp))
    def find_min_cost(self,index:int,cost,dp:List[int])->int:
        if index>=len(cost):
            return 0
        if dp[index]!=-inf:
            return dp[index]
        dp[index]=cost[index]+min(self.find_min_cost(index+1,cost,dp),self.find_min_cost(index+2,cost,dp))
        return dp[index]

# DP: Bottom Up
# TC:O(n)
# SC: O(n), dp array
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost)<3:
            return min(cost)
        dp=[-1]*len(cost)
        dp[0],dp[1]=cost[0],cost[1]
        for index in range(2,len(cost)):
            dp[index]=cost[index]+min(dp[index-1],dp[index-2])
        return min(dp[-1],dp[-2])

# DP: Bottom Up
# TC:O(n)
# SC: O(1)
class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        if not cost:
            return 0
        if len(cost)<3:
            return min(cost)
        # dp=[-1]*len(cost)
        prev,curr=cost[0],cost[1]
        for index in range(2,len(cost)):
            prev,curr=curr,cost[index]+min(prev,curr)
        return min(prev,curr)