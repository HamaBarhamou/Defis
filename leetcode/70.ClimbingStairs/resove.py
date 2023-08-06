class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
            
        dp = [0] * (n+1)
        dp[1] = 1
        dp[2] = 2
        
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        
        return dp[n]


def main():
    solution = Solution()

    # Test des cas limites
    print(solution.climbStairs(1))  # attendu: 1
    print(solution.climbStairs(2))  # attendu: 2
    print(solution.climbStairs(3))  # attendu: 3
    print(solution.climbStairs(4))  # attendu: 5
    print(solution.climbStairs(5))  # attendu: 8
    print(solution.climbStairs(45)) # attendu: 1836311903

main()
