class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if len(nums) == 1: return 0

        gauche = 0
        droite = len(nums) - 1

        while gauche <= droite:
            i = (gauche + droite) // 2
            v1 = nums[i-1] if i > 0 else float('-inf')
            v2 = nums[i+1] if i < len(nums)-1 else float('-inf')
            if v1 < nums[i] > v2:
                return i
            elif v1 > nums[i]:
                droite = i - 1
            elif v2 > nums[i]:
                gauche = i + 1


def main():
    s = Solution()
    
    # Test 1: Expected output: Any of 2, 5
    print(s.findPeakElement([1,2,1,3,5,6,4]))
    
    # Test 2: Expected output: 2
    print(s.findPeakElement([1,2,3,1]))
    
    # Test 3: Expected output: 0
    print(s.findPeakElement([3,2,1]))
    
    # Test 4: Expected output: 2
    print(s.findPeakElement([1,2,3]))

    # Test 5: Expected output: 0
    print(s.findPeakElement([1]))

if __name__ == "__main__":
    main()
