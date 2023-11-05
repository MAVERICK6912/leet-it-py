class Solution:
    def isAnagram(self, s: str, t: str) -> bool:        
        if len(s)!=len(t):
            return False
        countOfCharInS,countOfCharInT={},{}
        for index in range(len(s)):
            countOfCharInS[s[index]]=1+countOfCharInS.get(s[index],0)  # .get(,0) is used here to mitigate the issue of key not existing and python throwing error becase of that
            countOfCharInT[t[index]]=1+countOfCharInT.get(t[index],0)
        for key in countOfCharInS:
            if countOfCharInS[key]!=countOfCharInT.get(key,0):
                return False
        return True
            
        