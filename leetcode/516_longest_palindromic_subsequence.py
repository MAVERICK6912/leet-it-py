# DP: Bottom Up
# TC: O(n^2)
# SC: O(n^2)
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        # we store the length of longest palidromic subsequence
        # form i to j
        dp =[[0]*n for _ in range(n)]

        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                # single char
                if i==j:
                    dp[i][j]=1
                # two chars
                elif j==i+1:
                    # if both match then length will be 2
                    # otherwise it will be 1
                    dp[i][j]=2 if s[i]==s[j] else 1
                elif s[i]==s[j]:
                    # generic case
                    # we add teo since s[i] and s[j] are equal hence contribute
                    # rest of the answer we will get from middle sub-problem(i+1,j-1)
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    # this case means that s[i]!=s[j]
                    # therefore we will find the answer from left side and right side
                    # basically including char at i and excluding it in the next
                    dp[i][j]=max(dp[i+1][j],dp[i][j-1])
        return dp[0][n-1]