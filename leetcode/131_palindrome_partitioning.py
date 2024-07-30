class Solution:
    def partition(self, s: str) -> List[List[str]]:
        n=len(s)
        dp=[[False]*n for _ in range(n)]

        # applying Gap Method here to find all the palindromic substrings
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i-l+1
                # single char case
                if i==j:
                    dp[i][j]=True
                elif j==i+1:
                    dp[i][j]=s[i]==s[j]
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
            
        res,curr=[],[]
        self.findPals(curr,res,s,0,dp)
        return res
    
    def findPals(self,curr,res,s,index,dp):
        # base case
        if index>=len(s):
            res.append(curr[:])
            return
        # partitioning the string
        for i in range(index,len(s)):
                # if index to i is palindrome
                # then partition
            if dp[index][i]:
                # include index to i in curr
                curr.append(s[index:i+1])
                self.findPals(curr,res,s,i+1,dp)
                # remove index to i from curr
                curr.pop()