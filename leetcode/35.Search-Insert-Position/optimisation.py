from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums) - 1

        while left <= right:
            mid = left + (right - left) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return left

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
