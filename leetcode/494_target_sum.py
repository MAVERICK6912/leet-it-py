# Recursive back tracking solution
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        return self.make_comb(0, 0,target, nums)

    def make_comb(self, index, curr_sum, target: int, nums: List[int]) -> int:
        if index >= len(nums):
            return 1 if target == curr_sum else 0

        # add number at index
        plus = self.make_comb(index + 1, curr_sum + nums[index], target, nums)
        # subtract number at index
        minus = self.make_comb(index + 1, curr_sum - nums[index], target, nums)
        return plus + minus


# Dynamic Programming Top Down(memoization)
# TC: O(n*S), where is the nuber of unique states(index,curr_sum) combinations
# SC: O(nS)+O(n), recursive stack + mem dictionary
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        mem = {}
        return self.make_comb(0, 0, target, nums, mem)

    def make_comb(self, index, curr_sum, target: int, nums: List[int], mem) -> int:
        if index >= len(nums):
            return 1 if target == curr_sum else 0
        if (index, curr_sum) in mem:
            return mem[(index, curr_sum)]

        # add number at index
        plus = self.make_comb(index + 1, curr_sum + nums[index], target, nums, mem)
        # subtract number at index
        minus = self.make_comb(index + 1, curr_sum - nums[index], target, nums, mem)
        mem[(index, curr_sum)] = plus + minus
        return mem[(index, curr_sum)]
    
# Dynamic Programming Bottom Up(tabulation)
# TC: O(n*S), where is the number of unique states(index,curr_sum) combinations
# SC: O(nS), mem dictionary
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        # Calculate the total sum of nums
        total_sum = sum(nums)

        # Edge case: if target is out of bounds of achievable sums
        if target > total_sum or (total_sum - target) % 2 != 0:
            return 0

        # The actual sum we need to find in subset (derived from equation)
        s = (total_sum - target) // 2

        # Initialize the DP table where dp[j] is the number of ways to sum to j
        dp = [0] * (s + 1)
        dp[0] = 1  # There's one way to get sum 0, by choosing nothing

        # Update dp table for each number in nums
        for num in nums:
            for j in range(s, num - 1, -1):  # Traverse backward to avoid overwriting
                dp[j] += dp[j - num]

        return dp[s]