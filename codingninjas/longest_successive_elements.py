class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums)==0:
            return 0
        unique_elements=set()
        longest=1
        for num in nums:
            unique_elements.add(num)
        for num in nums:
            if num-1 not in unique_elements:
                current_longest_sequence=1
                while num+1 in unique_elements:
                    num+=1
                    current_longest_sequence+=1
                longest=max(longest,current_longest_sequence)
        return longest