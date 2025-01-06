# Recursive backtracking solution(TLE)
# TC: O(2^n), in worst case we will make 2 calls for each recursive call
# SC: O(n), recursive stack
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        return self.findLIS(0, -inf, nums)[1]

    def findLIS(self, index, prev: int, nums: List[int]) -> (int, int):
        # base case
        if index == len(nums):
            return 0,1
        # intialize include_length and include_count
        include_length, include_count = 0, 0
        # if number at index is greater than prev
        if nums[index] > prev:
            # include that number in current LIS and go to next
            include_length,include_count = self.findLIS(index + 1, nums[index], nums)
            # include_length is incremented as we have added that element to LIS
            include_length+=1
        # if it is not greater then move to other number to find LIS
        exclude_length,exclude_count = self.findLIS(index + 1, prev, nums)

        # if include_length is greater then it means we found a larger LIS
        # while inlcuding the number
        if include_length>exclude_length:
            return include_length,include_count
        # if both the lengths are same then
        elif include_length==exclude_length:
            # we can keep any length and return count of both include and exclude
            # as both of them will contribute to the solution
            return include_length,include_count+exclude_count
        # otherwise it means that we got a LIS by excluding the number
        else:
            return exclude_length,exclude_count


# Dynamic Programming(Top Down)
# TC: O(n!)
# SC: O(n)+O(n), recursive stack + mem dictionary
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        mem={}
        return self.findLIS(0, -inf, nums,mem)[1]

    def findLIS(self, index, prev: int, nums: List[int],mem:Dict[Tuple[int,int],Tuple[int,int]]) -> (int, int):
        # base case
        if index == len(nums):
            return 0,1
        if (index,prev) in mem:
            return mem[(index,prev)]
        # intialize include_length and include_count
        include_length, include_count = 0, 0
        # if number at index is greater than prev
        if nums[index] > prev:
            # include that number in current LIS and go to next
            include_length,include_count = self.findLIS(index + 1, nums[index], nums,mem)
            # include_length is incremented as we have added that element to LIS
            include_length+=1
        # if it is not greater then move to other number to find LIS
        exclude_length,exclude_count = self.findLIS(index + 1, prev, nums,mem)

        # if include_length is greater then it means we found a larger LIS
        # while inlcuding the number
        if include_length>exclude_length:
            mem[(index,prev)]= include_length,include_count
        # if both the lengths are same then
        elif include_length==exclude_length:
            # we can keep any length and return count of both include and exclude
            # as both of them will contribute to the solution
            mem[(index,prev)]= include_length,include_count+exclude_count
        # otherwise it means that we got a LIS by excluding the number
        else:
            mem[(index,prev)]= exclude_length,exclude_count
        
        return mem[(index,prev)]


# Dynamic Programming(Bottom Up)
# TC: O(n^2)
# SC: O(n)+O(n), length + count array
class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0
        lengths=[1]*len(nums)
        counts=[1]*len(nums)
        for index in range(len(nums)):
            for start in range(index,len(nums)):
                prev=nums[index]
                if nums[start]>prev:
                    include_length=lengths[index]+1
                    exclude_length=lengths[start]
                    
                    if include_length>exclude_length:
                        lengths[start]=lengths[index]+1
                        counts[start]=counts[index]
                    elif include_length==exclude_length:
                        lengths[start]=lengths[index]+1
                        counts[start]+=counts[index]

        max_length=max(lengths)
        return sum(count for length,count in zip(lengths,counts) if length==max_length)

    