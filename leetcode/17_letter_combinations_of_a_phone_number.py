# Recsursive back tracking
# TC: O(2^n)
# SC: O(n)+O(n)+O(n), recursive stack + res array + curr_comb array
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        # make the key map dictionary
        key_map={
            '2':'abc',
            '3':'def',
            '4':'ghi',
            '5':'jkl',
            '6':'mno',
            '7':'pqrs',
            '8':'tuv',
            '9':'wxyz'
        }
        # init res array
        res=[]
        # find all letter combinations from key_map and digits
        self.make_combinations(0,digits,[],res,key_map)
        # return the res
        return res

    def make_combinations(self,index:int,digits:str,curr_comb,res:List[str],key_map):
        # base case
        # when index is equql to number of digits
        # it means we have found an answer 
        # by picking an alphabet from each digit's map
        if index==len(digits):
            # append to res
            res.append(''.join(curr_comb))
            # return from here as we have found an answer
            return
        # loop over all the alphabets represented yb a digit
        for alpha in key_map[digits[index]]:
            # include current alphabet in combination
            curr_comb.append(alpha)
            # move to next digit's alphabets
            self.make_combinations(index+1,digits,curr_comb,res,key_map)
            # exclude current alphabet to get more combinations
            curr_comb.pop()
