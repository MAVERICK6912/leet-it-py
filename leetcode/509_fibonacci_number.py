# Recursive solution(n to 0)
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def fib(self, n: int) -> int:
        # bas case
        if n<=1:
            return n
        return self.fib(n-1)+self.fib(n-2)
    
# Dynamic Programming: Top Down
# TC: O(n)
# SC: O(n)+O(n), recursive stack + dp array/list
class Solution:
    def fib(self, n: int) -> int:
        # initialize the dp array
        # this array will store solutions that we have already calculated
        dp=[-inf]*(n+1)
        return self.find_fib(n,dp)
    def find_fib(self,n:int,dp:List[int])->int:
        # base case
        if n<=1:
            return n
        # if we have already calculated the solution
        # then return that solution
        if dp[n]!=-inf:
            return dp[n]
        # keep calculating solutions
        dp[n]=self.find_fib(n-1,dp)+self.find_fib(n-2,dp)
        # return current calculated solution
        return dp[n]
    
# Dynamic Programming: Bottom Up
# TC: O(n)
# SC: O(n)+O(n), dp array/list
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        dp=[0]*(n+1)
        dp[0],dp[1]=0,1

        for index in range(2,n+1):
            dp[index]=dp[index-1]+dp[index-2]
        return dp[n]
    
# Dynamic Programming: Space Otpimization
# TC: O(n)
# SC: O(1)
class Solution:
    def fib(self, n: int) -> int:
        if n<2:
            return n
        
        prev,curr=0,1
        for index in range(2,n+1):
            prev,curr=curr,prev+curr            
        return curr