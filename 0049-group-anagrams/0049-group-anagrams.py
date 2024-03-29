from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans_dict = defaultdict(list)
        
        for s in strs: # O(N)
            ans_dict[''.join(sorted(s))].append(s) # O(LlogL)
            
        ans = []
        for k, v in ans_dict.items():
            ans.append(v)
            
        return ans
            