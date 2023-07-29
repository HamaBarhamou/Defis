class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        def getIndice(i):
            return ((i + k) % len(nums))
        
        dic = {}
        
        for i in range(len(nums)):
            dic[getIndice(i)] = nums[i]
        
        for key, value in dic.items():
            nums[key] = value


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
