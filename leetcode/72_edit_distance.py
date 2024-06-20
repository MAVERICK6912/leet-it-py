# Recursive
# TC: O(3^(n+m))
# SC: O(n+m)
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        return self.find_min_distance(w1,w2,0,0)

    def find_min_distance(self,w1,w2:str,ind1,ind2:int):
        if ind1>=len(w1):
            return len(w2)-ind2
        if ind2>=len(w2):
            return len(w1)-ind1

        res=0
        # if chars are same we don't have to do anything
        if w1[ind1]==w2[ind2]:
            res=self.find_min_distance(w1,w2,ind1+1,ind2+1)
            return res
        # if chars are not same we can do these three ops
        # replace a char to make chars at ind1 and ind2 same
        replace=self.find_min_distance(w1,w2,ind1+1,ind2+1)
        # insert a char
        insert=self.find_min_distance(w1,w2,ind1+1,ind2)
        # delete a char
        delete=self.find_min_distance(w1,w2,ind1,ind2+1)

        # since doing any of these ops has cost of 1
        # we will add 1
        # since we need the minimum cost of converting w1 to w2
        # we take min of replace, insert and delete 
        res=1+min(replace,insert,delete)
        return res

# DP: Top Down
# TC: O(n*m)
# SC: O(n+m),O(n*m),recursive stack + dp array
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n,m=len(w1),len(w2)
        dp=[[-inf]*m for _ in range(n)]
        return self.find_min_distance(w1,w2,0,0,dp)

    def find_min_distance(self,w1,w2:str,ind1,ind2:int,dp:List[List[int]]):
        if ind1>=len(w1):
            return len(w2)-ind2
        if ind2>=len(w2):
            return len(w1)-ind1
        if dp[ind1][ind2]!=-inf:
            return dp[ind1][ind2]
        
        # if chars are same we don't have to do anything
        if w1[ind1]==w2[ind2]:
            dp[ind1][ind2]=self.find_min_distance(w1,w2,ind1+1,ind2+1,dp)
            return dp[ind1][ind2]
        # if chars are not same we can do these three ops
        # replace a char to make chars at ind1 and ind2 same
        replace=self.find_min_distance(w1,w2,ind1+1,ind2+1,dp)
        # insert a char
        insert=self.find_min_distance(w1,w2,ind1+1,ind2,dp)
        # delete a char
        delete=self.find_min_distance(w1,w2,ind1,ind2+1,dp)

        # since doing any of these ops has cost of 1
        # we will add 1
        # since we need the minimum cost of converting w1 to w2
        # we take min of replace, insert and delete 
        dp[ind1][ind2]=1+min(replace,insert,delete)
        return dp[ind1][ind2]

# DP: Bottom Up
# TC: O(n*m)
# SC: O(n*m), dp array
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n,m=len(w1),len(w2)
        dp=[[0]*(m+1) for _ in range(n+1)]

        for index in range(1,n+1):
            dp[index][0]=index

        for index in range(1,m+1):
            dp[0][index]=index

        for i in range(1,n+1):
            for j in range(1,m+1):
                # if chars are same we will get the solution from left diagonal element
                if w1[i-1]==w2[j-1]:
                    dp[i][j]=dp[i-1][j-1]
                else:
                    replace=dp[i-1][j-1]
                    insert=dp[i-1][j]
                    delete=dp[i][j-1]
                    dp[i][j]=1+min(replace,insert,delete)

        return dp[n][m]

# DP: Space Optimization
# TC: O(n*m)
# SC: O(m)+O(m), prev and curr array
class Solution:
    def minDistance(self, w1: str, w2: str) -> int:
        n,m=len(w1),len(w2)
        prev,curr=[0]*(m+1),[0]*(m+1)                

        for index in range(1,m+1):
            prev[index]=index

        for i in range(1,n+1):
            curr[0]=i
            for j in range(1,m+1):
                # if chars are same we will get the solution from left diagonal element
                if w1[i-1]==w2[j-1]:
                    curr[j]=prev[j-1]
                else:
                    replace=prev[j-1]
                    insert=prev[j]
                    delete=curr[j-1]
                    curr[j]=1+min(replace,insert,delete)
            prev=curr[:]
                
        return prev[m]