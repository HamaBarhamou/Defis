class Solution(object):
    def estMaPaire(self, fermante, ouvrante):
        parentheses_pairs = {')':'(', '}':'{', ']':'['}
        return parentheses_pairs.get(fermante) == ouvrante

    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        
        if len(s) == 0: 
            return True

        pile = []
        opening_brackets = ['(','{','[']
        closing_brackets = [')','}',']']

        for c in s:
            if c in opening_brackets:
                pile.append(c)
            elif c in closing_brackets:
                if len(pile) == 0 or not self.estMaPaire(c, pile.pop()):
                    return False

        return len(pile) == 0

def main():
    solution = Solution()

    # Test avec des cas limites
    print(solution.isValid("()"))  # Doit retourner True
    print(solution.isValid("()[]{}"))  # Doit retourner True
    print(solution.isValid("(]"))  # Doit retourner False
    print(solution.isValid("([)]"))  # Doit retourner False
    print(solution.isValid("{[]}"))  # Doit retourner True
    print(solution.isValid("["))  # Doit retourner False
    print(solution.isValid("]"))  # Doit retourner False
    print(solution.isValid(""))  # Doit retourner True

if __name__ == "__main__":
    main()
