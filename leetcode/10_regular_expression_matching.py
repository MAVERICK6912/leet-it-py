# Recursive Solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s,p,len(s)-1,len(p)-1)
    def match(self,s,p:str,s_pointer,p_pointer:int)->bool:
        # base case
        # both string and pattern are empty
        if s_pointer<0 and p_pointer<0:
            return True
        # pattern is empty but string is not
        if p_pointer<0:
            return False
        # string is empty but pattern is not
        if s_pointer<0:
            # * matches 0 of the preceding element
            if p[p_pointer]=='*':
                return self.match(s,p,s_pointer,p_pointer-2)
            else:
                return False
        
        # when string and pattern match or the pattern is '.'
        if s[s_pointer]==p[p_pointer] or p[p_pointer]=='.':
            return self.match(s,p,s_pointer-1,p_pointer-1)
        # when pattern is '*'
        if p[p_pointer]=='*':
            # * matches 0 of the preceding element
            if self.match(s,p,s_pointer,p_pointer-2):
                return True
            # if s[s_pointer] is a part of sequence represented by *
            if s[s_pointer]==p[p_pointer-1] or p[p_pointer-1]=='.':
                return self.match(s,p,s_pointer-1,p_pointer)
        # when nothing matches
        return False
        
# DP: Top Down
# TC: O(n*m)
# SC: O(n)+O(n*m)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1]*len(p) for _ in range(len(s))]
        return self.match(s,p,len(s)-1,len(p)-1,dp)
    def match(self,s,p:str,s_pointer,p_pointer:int,dp)->bool:
        # base case
        # if string and pattern are empty
        if s_pointer<0 and p_pointer<0:
            return True
        # pattern is empty but string is not
        if p_pointer<0:
            return False
        # string is empty but pattern is not
        if s_pointer<0:
            if p[p_pointer]=='*':
                return self.match(s,p,s_pointer,p_pointer-2,dp)
            else:
                return False
        if dp[s_pointer][p_pointer]!=-1:
            return dp[s_pointer][p_pointer]
        # when string and pattern match or the pattern is '.'
        if s[s_pointer]==p[p_pointer] or p[p_pointer]=='.':
            dp[s_pointer][p_pointer]=self.match(s,p,s_pointer-1,p_pointer-1,dp)
            return dp[s_pointer][p_pointer]
        # when pattern is '*'
        if p[p_pointer]=='*':
            if self.match(s,p,s_pointer,p_pointer-2,dp):
                dp[s_pointer][p_pointer]=True
                return dp[s_pointer][p_pointer]
            if s[s_pointer]==p[p_pointer-1] or p[p_pointer-1]=='.':
                dp[s_pointer][p_pointer]=self.match(s,p,s_pointer-1,p_pointer,dp)
                return dp[s_pointer][p_pointer]
        dp[s_pointer][p_pointer]=False
        return dp[s_pointer][p_pointer]

# DP: Bottom Up
# TC: O(n*m)
# SC: O(n*m)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        # initial conditions
        dp[0][0]=True
        # pattern is empty string is not
        for i in range(1,n+1):
            dp[i][0]=False
        # string is empty but pattern is not
        for j in range(1,m+1):
            if p[j-1]=='*':
                dp[0][j]=dp[0][j-2]
            else:
                dp[0][j]=False
                
        for i in range(1,n+1):
            for j in range(1,m+1):
                # when chars a re same or pattern is '.'
                if s[i-1]==p[j-1] or p[j-1]=='.':
                    dp[i][j]=dp[i-1][j-1]
                elif p[j-1]=='*':
                    # * matches zero chars in s
                    dp[i][j]=dp[i][j-2]
                    # s[i-1] is part of seq represented by *
                    if (j>1 and (s[i-1]==p[j-2] or p[j-2]=='.')):
                        dp[i][j]=dp[i][j] or dp[i-1][j]
                else:
                    dp[i][j]=False
        return dp[n][m]