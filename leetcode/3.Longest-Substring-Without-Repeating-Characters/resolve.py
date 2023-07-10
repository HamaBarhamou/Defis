class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        taille = len(s)
        if taille == 0 or taille == 1: return taille

        longest = 1
        data = set([])
        start = 0
        end = 0
        
        while end < taille:
            _len = end - start 
            if longest < _len: longest = _len
            if s[end] not in data: data.add(s[end])
            else:    
                while s[start] != s[end]:
                    if s[start] in data: data.remove(s[start])
                    start += 1
                start += 1
                data.add(s[end])
            end += 1

        _len = end - start 
        if longest < _len: longest = _len

        return (longest)

def main():
    sol = Solution()

    # Test case 1 : Normal case
    print(sol.lengthOfLongestSubstring("abcabcbb")) # Expected output: 3

    # Test case 2 : All characters are the same
    print(sol.lengthOfLongestSubstring("bbbbbb")) # Expected output: 1

    # Test case 3 : Single character string
    print(sol.lengthOfLongestSubstring("b")) # Expected output: 1

    # Test case 4 : Empty string
    print(sol.lengthOfLongestSubstring("")) # Expected output: 0

    # Test case 5 : Long string with no repeating characters
    print(sol.lengthOfLongestSubstring("abcdefghijklmnopqrstuvwxyz")) # Expected output: 26

    # Test case 6 : Long string with repeating characters
    print(sol.lengthOfLongestSubstring("abcabcabcabcabcabcabcabcabc")) # Expected output: 3

if __name__ == "__main__":
    main()