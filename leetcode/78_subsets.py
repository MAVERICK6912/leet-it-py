# Recursive backtracking solution
# TC: O(2^n)
# SC: O(n)+O(n), recursive stack + curr_subset array
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.make_subsets(0,[],nums,res)
        return res
    def make_subsets(self,index:int,curr_subset,nums:List[int],res:List[List[int]]):
        # base case
        if index==len(nums):
            res.append(curr_subset[:])
            return
        
        # include number at index
        curr_subset.append(nums[index])
        self.make_subsets(index+1,curr_subset,nums,res)
        # exlude number at index
        curr_subset.pop()
        self.make_subsets(index+1,curr_subset,nums,res)