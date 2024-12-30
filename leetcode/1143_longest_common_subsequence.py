# Recursive
# TC: O(2^(m+n))
# SC: O(m+n),recursive stack
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        return self.find_lcs(text1,text2,0,0)
    def find_lcs(self,s1,s2:str,ind1,ind2:int):
        if ind1>=len(s1) or ind2>=len(s2):
            return 0
        res=0
        if s1[ind1]==s2[ind2]:
            res=1+self.find_lcs(s1,s2,ind1+1,ind2+1)
        else:
            res=max(self.find_lcs(s1,s2,ind1+1,ind2),self.find_lcs(s1,s2,ind1,ind2+1))
        return res

# DP: Top Down
# TC: O(mn)
# SC: O(mn)(mem array)+O(mn)(recursive stack)
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        mem=[[-inf]*len(text2) for _ in range(len(text1))]
        return self.find_lcs(text1,text2,0,0,mem)
    def find_lcs(self,s1,s2:str,ind1,ind2:int,mem):
        if ind1>=len(s1) or ind2>=len(s2):
            return 0
        if mem[ind1][ind2]!=-inf:
            return mem[ind1][ind2]
        if s1[ind1]==s2[ind2]:
            mem[ind1][ind2]=1+self.find_lcs(s1,s2,ind1+1,ind2+1,mem)
        else:
            mem[ind1][ind2]=max(self.find_lcs(s1,s2,ind1+1,ind2,mem),self.find_lcs(s1,s2,ind1,ind2+1,mem))
        return mem[ind1][ind2]

# DP: Bottom Up
# TC: O(mn)
# SC: O(mn), mem array
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        mem=[[0]*(m+1) for _ in range(n+1)]
        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    mem[i][j]=1+mem[i-1][j-1]
                else:
                    mem[i][j]=max(mem[i-1][j],mem[i][j-1])
        return mem[n][m]


# DP: Space optimization
# TC: O(mn)
# SC: (m+n),prev and curr arrays
class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        n,m=len(text1),len(text2)
        prev,curr=[0]*(m+1),[0]*(m+1)

        for i in range(1,n+1):
            for j in range(1,m+1):
                if text1[i-1]==text2[j-1]:
                    curr[j]=1+prev[j-1]
                else:
                    curr[j]=max(prev[j],curr[j-1])
            prev=curr[:]
        return curr[m]

        