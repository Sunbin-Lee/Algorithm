from itertools import product

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        dp = [[] for _ in range(n+1)]
        dp[1] = ['()']
        
        for i in range(2, n+1):
            for j in range(1, i):
                list1 = dp[j]
                list2 = dp[i-j]
                prod = product(list1, list2)
                dp[i] += [p1+p2 for p1, p2 in list(prod)]

            dp[i] += ['('+p+')' for p in dp[i-1]]
            dp[i] = list(set(dp[i]))

        return dp[n]
