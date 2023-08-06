class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if not s:
            return ""

        _len = len(s)
        # initialiser dp à False
        dp = [[False] * _len for _ in range(_len)]
        start = 0  # début de la sous-chaîne palindromique la plus longue
        max_len = 1  # longueur du palindrome le plus long

        # Chaque caractère unique est un palindrome
        for i in range(_len):
            dp[i][i] = True

        # Vérifier pour la sous-chaîne de longueur 2
        for i in range(_len - 1):
            if s[i] == s[i+1]:
                dp[i][i+1] = True
                start = i
                max_len = 2

        # Vérifier les sous-chaînes de longueur 3 à len(s)
        for k in range(3, _len+1):
            for i in range(_len - k + 1):
                j = i + k - 1
                if s[i] == s[j] and dp[i+1][j-1]:
                    dp[i][j] = True
                    if k > max_len:
                        start = i
                        max_len = k

        return s[start:start+max_len]

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
