class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n < 3:
            return n
            
        prev, curr = 1, 2
        for i in range(3, n+1):
            next_val = prev + curr
            prev, curr = curr, next_val
        
        return curr

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
