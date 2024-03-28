class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ans = []
        self.recursion([], nums, ans)
        return ans
    
    def recursion(self, now, nums, ans):
        if len(nums) == 1:
            ans.append(now+[nums[0]])
            return
        
        for i in range(len(nums)):
            self.recursion(now+[nums[i]], nums[:i]+nums[i+1:], ans)