class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        _len = len(s)
        dp = [[False] * _len for _ in range(_len)]
        longestPalidromic = None
        pas = 0
        while pas <= _len:
            for i in range(_len - pas):
                j = i + pas
                longest = j - i + 1
                if (longest == 1) or (s[i] == s[j]) and ((longest == 2) or (longest > 2 and dp[i+1][j-1])):
                    dp[i][j] = True
                    longestPalidromic = s[i:j+1]
            pas += 1
        return longestPalidromic

def main():
    sol = Solution()
    
    # Test des cas limites
    print(sol.longestPalindrome("babad"))  # "bab" ou "aba"
    print(sol.longestPalindrome("cbbd"))   # "bb"
    print(sol.longestPalindrome(""))       # ""
    print(sol.longestPalindrome("a"))      # "a"
    print(sol.longestPalindrome("aa"))     # "aa"
    print(sol.longestPalindrome("ab"))     # "a" ou "b"
    print(sol.longestPalindrome("abcba"))  # "abcba"
    print(sol.longestPalindrome("a" * 1000)) # "a" * 1000 (le cas le plus long possible)

if __name__ == "__main__":
    main()