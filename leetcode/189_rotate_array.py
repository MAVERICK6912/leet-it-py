class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        k=k%len(nums)
        nums.reverse()
        self.reverse(nums,0,k-1)
        self.reverse(nums,k,len(nums)-1)

    def reverse(self,arr:List[int],start:int,end:int):
        while(start<=end):
            temp=arr[start]
            arr[start]=arr[end]
            arr[end]=temp
            start+=1
            end-=1
        