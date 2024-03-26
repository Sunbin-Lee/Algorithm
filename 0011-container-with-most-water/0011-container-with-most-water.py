class Solution:
    def maxArea(self, height: List[int]) -> int:
        s, e = 0, len(height) - 1
        ans = 0
        while s < e:
            now = (e-s) * min(height[e], height[s])
            ans = max(ans, now)

            if height[s] < height[e]:
                s += 1
            else:
                e -= 1

        return ans