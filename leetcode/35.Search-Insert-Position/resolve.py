class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        gauche = 0
        droite = len(nums)-1
        i = (gauche + droite)//2
        while gauche <= droite:
            if nums[i] == target:
                return i
            elif target < nums[i]:
                droite = i-1
            else:
                gauche = i + 1
            i = (gauche + droite)//2
        
        return gauche
        

def main():
    s = Solution()
    
    # Test cases
    print(s.searchInsert([1,3,5,6], 5)) # Expected output: 2
    print(s.searchInsert([1,3,5,6], 2)) # Expected output: 1
    print(s.searchInsert([1,3,5,6], 7)) # Expected output: 4
    print(s.searchInsert([1,3,5,6], 0)) # Expected output: 0
    print(s.searchInsert([1], 0))       # Expected output: 0
    print(s.searchInsert([1], 1))       # Expected output: 0
    print(s.searchInsert([], 1))        # Expected output: 0
    
if __name__ == "__main__":
    main()
