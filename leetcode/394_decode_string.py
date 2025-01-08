# Recursive BackTracking solution(using recusrive stack)
# TC: O(n!)
# SC: O(n), recursive stack
class Solution:
    def decodeString(self, s: str) -> str:        
        return self.decode(s,0)[0]
    def decode(self,s:str,index:int)->(str,int):
        # declare number of reps and final_string
        rep,final_string=0,""
        # loop from index till length of input string
        while index<len(s):
            # if char at index is a digit
            if s[index].isdigit():
                # count it as a repetition
                # keep adding the numbers
                rep=rep*10+int(s[index])
            # if char at index is '['
            elif s[index]=='[':
                # do a DFS and find more coded strings
                resp,pos=self.decode(s,index+1)
                # append the resultant string from previous function call
                # to final_string rep number of times
                final_string+=resp*rep
                # reset index to pos
                index=pos
                # make repititions 0
                rep=0
            # if char at index is a ']'
            elif s[index]==']':
                # just return the final string and index
                return final_string,index            
            else:
                # else just append the char at current index to final_string
                final_string+=s[index]
            # increment the index by 1
            index+=1
        # finally return final_stirng and index
        return final_string,index
        

# Stack solution
# TC: O(n!)
# SC: O(n), stack
class Solution:
    def decodeString(self, s: str) -> str:
        stack=[]
        rep,final_string=0,""
        # loop from index till length of input string
        for char in s:
            # if char at index is a digit
            if char.isdigit():
                # count it as a repetition
                # keep adding the numbers
                rep=rep*10+int(char)
            # if char at index is '['
            elif char=='[':
                # append final string and rep to stack
                stack.append((final_string,rep))
                # reset final_string and rep
                # make final_string empty
                final_string=""
                # make repititions 0
                rep=0
            # if char at index is a ']'
            elif char==']':                
                last_string,rep_count=stack.pop()
                # append the popped string and 
                # final_string rep number of times
                final_string=last_string+final_string*rep_count                
            else:
                # else just append the char at current index to final_string
                final_string+=char                        
        # finally return final_stirng
        return final_string