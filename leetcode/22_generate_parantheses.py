# Recursive Solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        self.generate(n,0,0,'',res)
        return res
    def generate(self,n,no_of_open,no_of_closed:int,curr_seq:str,res:List[str]):
        # base case
        if no_of_open+no_of_closed==2*n:
            res.append(curr_seq)
            return
        # we can add an open parantheses, if no_of_open is less than n
        if no_of_open<n:
            self.generate(n,no_of_open+1,no_of_closed,curr_seq+'(',res)
        # we can add closing parantheses, if no_of_open>no_of_closed
        if no_of_open>no_of_closed:
            self.generate(n,no_of_open,no_of_closed+1,curr_seq+')',res)
