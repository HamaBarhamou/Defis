class Solution(object):
    def findPeakElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        nums = [float('-inf')] + nums + [float('-inf')]
        gauche = 1
        droite = len(nums) - 2

        while gauche <= droite:
            i = (gauche + droite) // 2
            if nums[i-1] < nums[i] > nums[i+1]:
                return i - 1
            elif nums[i] < nums[i+1]:
                gauche = i + 1
            else:
                droite = i - 1

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
