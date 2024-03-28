class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        def recursion(now, visited):
            if len(now) == len(nums):
                ans.append(now)
                return
            
            for i in range(len(nums)):
                if visited[i] == 0:
                    visited[i] = 1
                    recursion(now+[nums[i]], visited)
                    visited[i] = 0
                    
        ans = []
        recursion([], [0 for _ in range(len(nums))])
        return ans
    
        