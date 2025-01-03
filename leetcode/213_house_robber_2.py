# Recursive back tracking solution(TLE)
# TC: O(2^n)
# SC: O(n), recursive stack
class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums)<2:
            return nums[0]
        # since we can't rob the first and last house
        # we will take max of starting from first house and ending at len(nums)-1 house
        # and starting from second house and ending at len(nums) house
        return max(self.lets_rob(0,len(nums)-1,nums),self.lets_rob(1,len(nums),nums))
    def lets_rob(self,house,end:int,nums:List[int])->int:
        # base case
        if house>=end:
            return 0
        # rob the house and move to next house to rob
        rob=nums[house]+self.lets_rob(house+2,end,nums)
        # dont rob to see if there's better loot possible
        dont_rob=self.lets_rob(house+1,end,nums)
        # return the max of rob and dont_rob
        return max(rob,dont_rob)
    
# Dynamic Programming(Top Down)
# TC: O(n*n)
# SC: O(n)+O(n), recursive stack + mem array
class Solution:
    def rob(self, nums: List[int]) -> int:        
        if len(nums)<2:
            return nums[0]
        # since we can't rob the first and last house
        # we will take max of starting from first house and ending at len(nums)-1 house
        # init mem array to remember previous solutions 
        mem=[inf]*len(nums)
        rob_first=self.lets_rob(0,len(nums)-1,nums,mem)        
        # init mem array to remember previous solutions 
        # and starting from second house and ending at len(nums) house
        mem=[inf]*len(nums)
        rob_second=self.lets_rob(1,len(nums),nums,mem)
        # to get maximum loot return max of rob_first and rob_second
        return max(rob_first,rob_second)
    def lets_rob(self,house,end:int,nums,mem:List[int])->int:
        # base case
        if house>=end:
            return 0
        # check if we have already found solution to this house
        if mem[house]!=inf:
            return mem[house]
        # rob the house and move to next house to rob
        rob=nums[house]+self.lets_rob(house+2,end,nums,mem)
        # dont rob to see if there's better loot possible
        dont_rob=self.lets_rob(house+1,end,nums,mem)
        # store the max of rob and dont_rob
        mem[house]=max(rob,dont_rob)
        # return mem[house]
        return mem[house]
    
# Dynamic Programming(Bottom Up with space optimization)
# TC: O(n*n)
# SC: O(1)
class Solution:
    def rob(self, nums: List[int]) -> int:
        return max(nums[0],self.robHouse(nums[1:]),self.robHouse(nums[:-1]))
    def robHouse(self,nums:List[int])->int:
        prev_rob,curr_rob=0,0
        for num in nums:
            prev_rob,curr_rob=curr_rob,max(curr_rob,prev_rob+num)
        return curr_rob