class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        k = 0
        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        del nums[k:]
        return (k)


def main():
    solution = Solution()

    # Test case 1: normal case
    nums1 = [3, 2, 2, 3]
    val1 = 3
    print(solution.removeElement(nums1, val1))  # Expected output: 2
    print(nums1)  # The first 2 elements should be 2

    # Test case 2: normal case with more variety of numbers
    nums2 = [0, 1, 2, 2, 3, 0, 4, 2]
    val2 = 2
    print(solution.removeElement(nums2, val2))  # Expected output: 5
    print(nums2)  # The first 5 elements should be 0, 1, 4, 0, 3

    # Test case 3: edge case where nums is an empty list
    nums3 = []
    val3 = 0
    print(solution.removeElement(nums3, val3))  # Expected output: 0
    print(nums3)  # Should still be an empty list

    # Test case 4: edge case where nums has maximum length and all elements are equal to val
    nums4 = [50] * 100
    val4 = 50
    print(solution.removeElement(nums4, val4))  # Expected output: 0
    print(nums4)  # Should be an empty list


if __name__ == "__main__":
    main()
