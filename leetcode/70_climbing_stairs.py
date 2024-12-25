# Recursive Solution
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        return self.climbStairs(n-2)+self.climbStairs(n-1)

# DP Solution(Top Down)
# TC: O(n)
# SC: O(n)+O(n), recursive stack + dp array
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        dp=[-inf]*(n+1)
        self.climb(n,dp)
        return dp[n]
    def climb(self,n:int,dp:List[int])->int:
        if n<=1:
            return 1
        if dp[n]!=-inf:
            return dp[n]
        dp[n]=self.climb(n-2,dp)+self.climb(n-1,dp)
        return dp[n]


# DP Solution(Bottom Up)
# TC: O(n)
# SC: O(n), dp array/list
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        dp=[-inf]*(n+1)
        dp[0],dp[1]=1,1
        for index in range(2,n+1):
            dp[index]=dp[index-2]+dp[index-1]
        return dp[n]        

# DP Solution(Bottom Up with space optimization)
# TC: O(n)
# SC: O(1)
class Solution:
    def climbStairs(self, n: int) -> int:
        if n<=1:
            return 1
        
        prev,curr=1,1
        for _ in range(2,n+1):
            prev,curr=curr,prev+curr
        return curr