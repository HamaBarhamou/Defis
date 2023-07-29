class Solution:
    def rotate(self, nums, k):
        k = k % len(nums)
        self.reverse(nums, 0, len(nums) - 1)
        self.reverse(nums, 0, k - 1)
        self.reverse(nums, k, len(nums) - 1)
    
    def reverse(self, nums, start, end):
        while start < end:
            nums[start], nums[end] = nums[end], nums[start]
            start += 1
            end -= 1

def main():
    s = Solution()

    # Test case 1
    nums = [1,2,3,4,5,6,7]
    k = 3
    s.rotate(nums, k)
    print(nums) # Expected: [5,6,7,1,2,3,4]

    # Test case 2
    nums = [-1,-100,3,99]
    k = 2
    s.rotate(nums, k)
    print(nums) # Expected: [3,99,-1,-100]

    # Test case 3: Single rotation
    nums = [1, 2, 3, 4, 5]
    k = 1
    s.rotate(nums, k)
    print(nums) # Expected: [5, 1, 2, 3, 4]

    # Test case 4: No rotation
    nums = [1, 2, 3, 4, 5]
    k = 0
    s.rotate(nums, k)
    print(nums) # Expected: [1, 2, 3, 4, 5]

    # Test case 5: Rotation count > array size
    nums = [1, 2, 3, 4, 5]
    k = 7
    s.rotate(nums, k)
    print(nums) # Expected: [4, 5, 1, 2, 3]

if __name__ == "__main__":
    main()
