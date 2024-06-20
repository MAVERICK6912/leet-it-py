# Recursion(backtracking)
# TC: O(n*n^n)
# SC: O(n!)+O(n)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.find_perm([],nums,res)
        return res
    def find_perm(self,curr_perm,nums:List[int],res:List[List[int]]):
        if len(curr_perm)==len(nums):
            res.append(curr_perm[:])
            return
        for i in range(len(nums)):
            # this op will take O(n) time
            if nums[i] in curr_perm:
                continue
            # include num at index
            curr_perm.append(nums[i])
            self.find_perm(curr_perm,nums,res)
            # exclude num at index
            curr_perm.pop()


# Recursion(backtracking), without extra space
# TC: O(n*n!)
# SC: O(n*n!)
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        self.find_perm(0,nums,res)
        return res
    def find_perm(self,index:int,nums:List[int],res:List[List[int]]):
        if index==len(nums):
            res.append(nums[:])
            return
        for i in range(index,len(nums)):
            # include num at index
            nums[index],nums[i]=nums[i],nums[index]
            self.find_perm(index+1,nums,res)
            # exclude num at index
            nums[index],nums[i]=nums[i],nums[index]