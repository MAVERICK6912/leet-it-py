# Recursive backtracking(memoization)
# TC: O(n*amount), where 'n' is the number of coins
# SC: O(n*amount) + O(amount), mem dictionary + recursive stack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1        
        return self.find_change(0, amount, coins)

    def find_change(
        self, index, target: int, coins: List[int]
    ) -> int:
        if target == 0:
            return 1
        if index >= len(coins):
            return 0        
        exclude = self.find_change(index + 1, target, coins)
        include = 0
        if target >= coins[index]:
            include = self.find_change(index, target - coins[index], coins)        
        return include + exclude


# Dynamic Programming Top Down(memoization)
# TC: O(n*amount), where 'n' is the number of coins
# SC: O(n*amount) + O(amount), mem dictionary + recursive stack
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        mem = {}
        return self.find_change(0, amount, coins, mem)

    def find_change(
        self, index, target: int, coins: List[int], mem: Dict[int, int]
    ) -> int:
        if target == 0:
            return 1
        if index >= len(coins):
            return 0
        if (target,index) in mem:
            return mem[(target,index)]
        exclude = self.find_change(index + 1, target, coins,mem)
        include = 0
        if target >= coins[index]:
            include = self.find_change(index, target - coins[index], coins,mem)
        mem[(target,index)]= include + exclude
        return mem[(target,index)]


# Dynamic Programming Bottom UP(tabulation)
# TC: O(n*amount), where 'n' is the number of coins
# SC: O(n*amount), mem array
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n=len(coins)
        mem = [[0]*(amount+1) for _ in range(n+1)]
        # initial condition
        for col in range(amount+1):
            if col%coins[0]==0:
                mem[0][col]=1
        for row in range(1,n+1):
            for col in range(1,amount+1):
                exclude=mem[row-1][amount]
                include=0
                if coins[row]<=col:
                    include=mem[row][col-coins[row]]
                mem[row][col]=include+exclude
        return mem[n][amount]
    
# Dynamic Programming Bottom UP(space optimization)
# TC: O(n*amount), where 'n' is the number of coins
# SC: O(amount) + O(amount), prev + curr array
class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        if amount == 0:
            return 1
        n = len(coins)
        prev, curr = [0] * (amount + 1), [0] * (amount + 1)
        # initial condition
        for col in range(amount + 1):
            if col % coins[0] == 0:
                prev[col] = 1

        for row in range(1, n):
            for col in range(amount + 1):
                exclude = prev[col]
                include = 0
                if coins[row] <= col:
                    include = curr[col - coins[row]]
                curr[col] = include + exclude
            prev = curr[:]
        return prev[amount]
