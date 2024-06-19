# Recursive solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def numDecodings(self, s: str) -> int:
        # it is not possible to decode if the first character of stirng is zero
        if s[0]=='0':
            return 0
        return self.decode(0,s)
    def decode(self,index:int,s:str)->int:
        if index>=len(s):
            return 1
        if s[index]=='0':
            return 0

        # consider number at index as single digit
        res=self.decode(index+1,s)
        # consider number at index and index+1 as two digit number
        if index+1<len(s) and (s[index]=='1' or (s[index]=='2' and s[index+1]<'7')):
            res+=self.decode(index+2,s)
        return res

# DP: Top Down
# TC: O(n)
# SC: O(n)+O(n), recursive stack + dp array
class Solution:
    def numDecodings(self, s: str) -> int:
        # it is not possible to decode if the first character of stirng is zero
        if s[0]=='0':
            return 0
        # initialize the dp array
        dp=[-inf]*len(s)
        return self.decode(0,s,dp)
    def decode(self,index:int,s:str,dp:List[int])->int:
        if index>=len(s):
            return 1
        if s[index]=='0':
            dp[index]=0
            return 0
        if dp[index]!=-inf:
            return dp[index]
        # consider number at index as single digit
        dp[index]=self.decode(index+1,s,dp)
        # consider number at index and index+1 as two digit number
        if index+1<len(s) and (s[index]=='1' or (s[index]=='2' and s[index+1]<'7')):
            dp[index]+=self.decode(index+2,s,dp)
        return dp[index]

# DP: Bottom Up
# TC: O(n)
# SC: O(n), dp array
class Solution:
    def numDecodings(self, s: str) -> int:
        # it is not possible to decode if the first character of stirng is zero
        if s[0]=='0':
            return 0
        # initialize the dp array
        dp=[0]*(len(s)+1)
        dp[0]=1
        for index in range(1,len(s)+1):
            if s[index-1]!='0':
                dp[index]=dp[index-1]
            if index>1 and (s[index-2]=='1' or (s[index-2]=='2' and s[index-1]<'7')):
                dp[index]+=dp[index-2]
        return dp[len(s)]

# DP: Space Optimization
# TC: O(n)
# SC: O(1)
class Solution:
    def numDecodings(self, s: str) -> int:
        # it is not possible to decode if the first character of stirng is zero
        if s[0]=='0':
            return 0
        # initialize prev and curr
        prev,curr=1,1        
        for index in range(1,len(s)+1):
            ways=0
            # consider char at index-1 as single digit
            if s[index-1]!='0':
                # hence ways will be ways+curr
                ways+=curr
            # consider char at index-2 and index-1 as two digit number
            if index>1 and (s[index-2]=='1' or (s[index-2]=='2' and s[index-1]<'7')):
                # hence way will be ways+prev
                ways+=prev
            # interchange values of prev to curr and curr to ways
            prev,curr=curr,ways
        # return curr as that will have the solution to last decoded value
        return curr