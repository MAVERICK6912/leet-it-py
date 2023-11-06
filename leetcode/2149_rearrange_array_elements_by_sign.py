from collections import defaultdict
class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        signMap=defaultdict(list)
        for index in range(len(nums)):
            if nums[index]>0:
                signMap["+"].append(nums[index])
            else:
                signMap["-"].append(nums[index])
        ret=[]
        for index in range(len(nums)):
            if index%2==0:
                ret.append(signMap["+"].pop(0))
            else:
                ret.append(signMap["-"].pop(0))
        return ret