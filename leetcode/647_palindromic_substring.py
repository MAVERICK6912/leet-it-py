# DP: Top Down
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res,n=0,len(s)
        dp=[[-1]*n for _ in range(n)]
        # find all palindromic substrings
        self.count(0,n-1,s,dp)
        # count all palindromic substrings
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if dp[i][j]:
                    res+=1
        return res

    def count(self,i,j:int,s:str,dp:List[List[int]])->bool:
        # base cases
        # invalid index
        if j<i:
            return False
        # single character case
        if i==j:
            dp[i][j]=True
            return dp[i][j]
        if dp[i][j]!=-1:
            return dp[i][j]
        # find palindromic substrings while excluding char at i and including char at j
        self.count(i+1,j,s,dp)
        # find palindromic substrings while excluding char at j and including char at i
        self.count(i,j-1,s,dp)

        # general case
        if s[i]==s[j] and (j==i+1 or self.count(i+1,j-1,s,dp)):
            dp[i][j]=True
            return dp[i][j]
        dp[i][j]=False
        return dp[i][j]



# DP: Bottom Up
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def countSubstrings(self, s: str) -> int:
        res,n=0,len(s)
        # this represents if chars between i to j form a palindrome
        dp=[[False]*n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                # single char case
                if i==j:
                    dp[i][j]=True
                # two char case
                elif j==i+1:
                    dp[i][j]=s[i]==s[j]
                elif s[i]==s[j]:
                    # general case
                    dp[i][j]=dp[i+1][j-1]
                if dp[i][j]:
                    res+=1
        return res
