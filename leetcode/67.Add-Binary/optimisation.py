class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        a = int(a, 2)
        b = int(b, 2)

        while b != 0:
            total = a ^ b
            carry = (a & b) << 1
            a = total
            b = carry
        
        return bin(a)[2:]

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
