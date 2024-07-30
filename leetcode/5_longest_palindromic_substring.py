# DP: Bottm Up
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        n=len(s)
        dp=[[False]*n for _ in range(n)]
        res=""

        # in this loop we find if we have a palindromic substring from
        # i to j, if there exist a palindromic substring from i to j
        # then we mark it as True
        for l in range(1,n+1):
            for i in range(0,n-l+1):
                j=i+l-1

                # single char
                if i==j:
                    dp[i][j]=True
                # two chars
                elif j==i+1:
                    dp[i][j]=s[i]==s[j]
                elif s[i]==s[j]:
                    dp[i][j]=dp[i+1][j-1]
                else:
                    dp[i][j]=False
                # if dp[i][j] id true then we have a palindromic substring from i to j
                # hence it can be a solution to the problem
                # since we're using gap method we're going from lower length
                # that is l=1 to len(s), this means we will go to higher length strings
                if dp[i][j]:
                    res=s[i:j+1]        
        return res