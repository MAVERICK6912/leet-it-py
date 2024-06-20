# Recursive Backtracking solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res=[]
        self.find_combi(1,n,k,[],res)
        return res
    def find_combi(self,index,n,k:int,curr_combi:List[int],res:List[List[int]]):
        if len(curr_combi)==k:
            res.append(curr_combi[:])
            return
        
        for i in range(index,n+1):
            # include i in curr combination
            curr_combi.append(i)
            self.find_combi(i+1,n,k,curr_combi,res)
            # exclude i from curr combination
            curr_combi.pop()