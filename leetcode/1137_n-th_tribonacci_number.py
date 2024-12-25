# Recursive Solution(n to 0)
# TC: O(3^n)
# SC: O(n)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        return self.tribonacci(n-3)+self.tribonacci(n-2)+self.tribonacci(n-1)

# DP: Top Down
# TC: O(n)
# SC: O(n)+O(n), recursive stack + dp array
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        dp=[-inf]*(n+1)
        self.find_trib(n,dp)        
        return dp[n]
    
    def find_trib(self,n:int,dp:List[int]):
        if n<=1:
            return n
        if n==2:
            return 1
        if dp[n]!=-inf:
            return dp[n]
        dp[n]=self.find_trib(n-3,dp)+self.find_trib(n-2,dp)+self.find_trib(n-1,dp)
        return dp[n]


# DP solution(Bottom Up)
# TC: O(n), loop
# SC: O(n), memory array
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1
        mem=[0]*(n+1)
        mem[0],mem[1],mem[2]=0,1,1
        for index in range(3,n+1):
            mem[index]=mem[index-1]+mem[index-2]+mem[index-3]
        return mem[n]

# DP: Bottom Up with space optimization
# TC: O(n), loop
# SC: O(1)
class Solution:
    def tribonacci(self, n: int) -> int:
        if n<=1:
            return n
        if n==2:
            return 1        
        one,two,three=0,1,1        
        for index in range(3,n+1):
            one,two,three=two,three,one+two+three        
        return three