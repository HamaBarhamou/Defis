class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        som = []
        i = 0
        r = 0
        a_ = list(reversed(a))
        b_ = list(reversed(b))
        while i < len(a) and i < len(b):
            s = r + int(a_[i]) + int(b_[i])
            if s > 2:
                s = 1
                r = 1
            elif s == 2:
                s = 0
                r = 1
            else:
                r = 0
            som.append(str(s))
            i += 1
        
        if i < len(a): c = a_
        else: c = b_

        while i < len(c):
            s = r + int(c[i])
            if s > 2:
                s = 1
                r = 1
            elif s == 2:
                s = 0
                r = 1
            else:
                r = 0
            som.append(str(s))
            i += 1
        
        if r == 1: som.append(str(r))

        return ''.join(reversed(som))

def test_addBinary():
    solution = Solution()
    
    assert solution.addBinary("11", "1") == "100"
    assert solution.addBinary("1010", "1011") == "10101"
    assert solution.addBinary("1111", "1111") == "11110"
    assert solution.addBinary("0", "0") == "0"
    assert solution.addBinary("1", "0") == "1"
    assert solution.addBinary("0", "1") == "1"

    print("All test cases pass")

if __name__ == "__main__":
    test_addBinary()