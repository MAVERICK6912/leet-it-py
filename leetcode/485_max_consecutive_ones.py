class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        nums.append(0)
        consecutive,maxConsecutive=0,0
        for num in nums:
            if num:                                
                consecutive+=1                
            else:
                maxConsecutive=max(consecutive,maxConsecutive)
                consecutive=0
        return maxConsecutive        