class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count={}
        freq=[[]for i in range(len(nums)+1)]
        for num in nums:
            count[num]=1+count.get(num,0)
        for key,val in count.items():
            freq[val].append(key)
        res=[]
        for index in range(len(freq)-1,0,-1):
            for n in freq[index]:
                res.append(n)
                if len(res)==k:
                    return res
        