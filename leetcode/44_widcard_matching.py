# Recursive Solution
# TC: O(2^n)
# SC: O(n)
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        return self.match(s,p,len(s)-1,len(p)-1)
    def match(self,s,p:str,s_pointer,p_pointer:int)->bool:
        #  base cases
        if s_pointer<0 and p_pointer<0:
            return True
        # pattern is empty but string is not
        if p_pointer<0 and s_pointer>=0:
            return False
        # string is empty but pattern is not
        if s_pointer<0 and p_pointer>=0:
            # continue consuming the pattern if it is at *
            # as a pattern can contain ***?**, so we need to take care of that one ?
            if p[p_pointer]=='*':
                return self.match(s,p,s_pointer,p_pointer-1)
            # if it ain't * then it means we're matching "" with either ? or some other character
            # which can't match hence return False
            return False
        
        # if chars are same or pattern is ?
        if s[s_pointer]==p[p_pointer] or p[p_pointer]=='?':
            # if a sincgle match is found then we go ahead
            # with pattern and string
            return self.match(s,p,s_pointer-1,p_pointer-1)
        
        # if pattern is *
        if p[p_pointer]=='*':
            # we will consider the case:
            # when * matches with a char                    when * matches an empty string("")
            return self.match(s,p,s_pointer-1,p_pointer) or self.match(s,p,s_pointer,p_pointer-1)
        return False


# DP: Top Down
# TC: O(n!)
# SC: O(n)+O(n*m), recursive stack + dp array
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        dp=[[-1]*len(p) for _ in range(len(s))]
        return self.match(s,p,len(s)-1,len(p)-1,dp)
    def match(self,s,p:str,s_pointer,p_pointer:int,dp:List[List[int]])->bool:
        #  base cases
        if s_pointer<0 and p_pointer<0:
            return True
        # pattern is empty but string is not
        if p_pointer<0 and s_pointer>=0:
            return False        
        # string is empty but pattern is not
        if s_pointer<0 and p_pointer>=0:
            # continue consuming the pattern if it is at *
            # as a pattern can contain ***?**, so we need to take care of that one ?
            if p[p_pointer]=='*':                
                return self.match(s,p,s_pointer,p_pointer-1,dp)
            # if it ain't * then it means we're matching "" with either ? or some other character
            # which can't match hence return False
            return False
        
        # check if we have already found an answer
        if dp[s_pointer][p_pointer]!=-1:
            return dp[s_pointer][p_pointer]
        
        # if chars are same or pattern is ?
        if s[s_pointer]==p[p_pointer] or p[p_pointer]=='?':
            # if a sincgle match is found then we go ahead
            # with pattern and string
            dp[s_pointer][p_pointer]=self.match(s,p,s_pointer-1,p_pointer-1,dp)
            return dp[s_pointer][p_pointer]
        
        # if pattern is *
        if p[p_pointer]=='*':
            # we will consider the case:
            # when * matches with a char                                         when * matches an empty string("")
            dp[s_pointer][p_pointer]=self.match(s,p,s_pointer-1,p_pointer,dp) or self.match(s,p,s_pointer,p_pointer-1,dp)
            return dp[s_pointer][p_pointer]
        
        dp[s_pointer][p_pointer]= False
        return dp[s_pointer][p_pointer]

# DP: Top Down
# TC: O(nm)
# SC: O(n*m), dp array
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        dp=[[False]*(m+1) for _ in range(n+1)]
        # empty string and empty pattern always match, hence:
        dp[0][0]=True
        # initial conditions
        # pattern is empty but string is not
        for i in range(1,n+1):
            dp[i][0]=False
        # string is empty but pattern is not
        for i in range(1,m+1):
            if p[i-1]=='*':
                dp[0][i]=dp[0][i-1]
            else:
                dp[0][i]=False
        

        for i in range(1,n+1):
            for j in range(1,m+1):
                # chars are same in pattern and string or pattern is '?'
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    dp[i][j]=dp[i-1][j-1]
                # pattern is '*'
                elif p[j-1]=='*':
                    dp[i][j]=dp[i-1][j] or dp[i][j-1]
                else:
                    dp[i][j]=False
        return dp[n][m]

# DP: Space Optimization
# TC: O(nm)
# SC: O(m), dp array
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        n,m=len(s),len(p)
        prev,curr=[False]*(m+1),[False]*(m+1)        
        # empty string and empty pattern always match, hence:
        # initial conditions
        # pattern is empty but string is not
        prev[0]=True
        curr[0]=False
        # string is empty but pattern is not
        for i in range(1,m+1):
            if p[i-1]=='*':
                prev[i]=prev[i-1]
            else:
                prev[i]=False
        
        for i in range(1,n+1):            
            for j in range(1,m+1):
                # chars are same in pattern and string or pattern is '?'
                if s[i-1]==p[j-1] or p[j-1]=='?':
                    curr[j]=prev[j-1]
                # pattern is '*'
                elif p[j-1]=='*':
                    curr[j]=prev[j] or curr[j-1]
                else:
                    curr[j]=False
            prev=curr[:]
        return prev[m]