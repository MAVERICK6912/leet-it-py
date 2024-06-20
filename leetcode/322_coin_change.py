# Recusrive solution(TLE)
# TC: O(2^n)
# SC: O(n)
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        res=self.find_change(0,amount,coins)
        return res if res!=float('inf') else -1
    def find_change(self,index,amount:int,coins:List[int]):
        if amount==0:
            return 0
        if index>=len(coins):
            return float('inf')
        if coins[index]<=amount:
            return min(1+ self.find_change(index,amount-coins[index],coins),self.find_change(index+1,amount,coins))
        else:
            return self.find_change(index+1,amount,coins)

# DP: Top Down
# TC: O(n!)
# SC: O(n)+O(n*amount),recursive stack + dp array
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[-inf]*(amount+1) for _ in range(n)]
        res=self.find_change(0,amount,coins,dp)
        return res if res!=float('inf') else -1
    def find_change(self,index,amount:int,coins:List[int],dp):
        if amount==0:
            return 0
        if index>=len(coins):
            return float('inf')
        if dp[index][amount]!=-inf:
            return dp[index][amount]
        if coins[index]<=amount:
            dp[index][amount]= min(1+ self.find_change(index,amount-coins[index],coins,dp),self.find_change(index+1,amount,coins,dp))
            return dp[index][amount]
        else:
            dp[index][amount]= self.find_change(index+1,amount,coins,dp)
            return dp[index][amount]

# DP: Bottom Up
# TC: O(n*amount)
# SC: O(n*amount), dp array
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        dp=[[0]*(amount+1) for _ in range(n+1)]
        # initial conditions
        for i in range(amount+1):
            # we set first row to 'inf' as we can't make the amount without any coins
            dp[0][i]=float('inf')
            # we set second row to value of coin if it is divisible by i(amount)
            # otherwise we set it to inf, meaning we can't make amount with it
            dp[1][i]=i// coins[0] if i % coins[0] == 0 else float('inf')
        
        for i in range(2,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    dp[i][j]=min(1+dp[i][j-coins[i-1]],dp[i-1][j])
                else:
                    dp[i][j]=dp[i-1][j]

        return dp[n][amount] if dp[n][amount]!=float('inf') else -1

# DP: Bottom Up
# TC: O(n*amount)
# SC: O(amount)+O(amount), prev+curr
class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        prev,curr=[float('inf')]*(amount+1),[float('inf')]*(amount+1)
        # initial conditions
        # we need zero coins to make 0 amount
        prev[0],curr[0]=0,0
        for i in range(1,n+1):
            for j in range(1,amount+1):
                if coins[i-1]<=j:
                    curr[j]=min(1+curr[j-coins[i-1]],prev[j])
                else:
                    curr[j]=prev[j]
            prev=curr[:]

        return curr[amount] if curr[amount]!=float('inf') else -1