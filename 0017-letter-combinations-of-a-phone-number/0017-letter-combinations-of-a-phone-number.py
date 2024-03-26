class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letters = {
            '2' : 'abc', '3' : 'def', 
            '4' : 'ghi', '5' : 'jkl', '6' : 'mno', 
            '7' : 'pqrs', '8' : 'tuv', '9' : 'wxyz'
            }
        
        ans = []
        
        if len(digits) == 0:
            return ans 
        
        self.dfs(letters, ans, '', 0, digits)
        
        return ans

    def dfs(self, letters, ans, now_letter, idx, digits,):
        if idx == len(digits):
            ans.append(now_letter)
            return
        
        for l in letters[digits[idx]]:
            self.dfs(letters, ans, now_letter+l, idx+1, digits)
        
            
        
        