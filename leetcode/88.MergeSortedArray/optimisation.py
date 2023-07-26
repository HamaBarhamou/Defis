class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: None Do not return anything, modify nums1 in-place instead.
        """

        # pointer for the end of nums1
        p1 = m - 1
        # pointer for the end of nums2
        p2 = n - 1
        # pointer for the end of the result in nums1
        p = m + n - 1

        while p1 >= 0 and p2 >= 0:
            if nums1[p1] >= nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1
        
        # add remaining elements from nums2
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p -= 1
            p2 -= 1


def main():
    s = Solution()

    # Test case 1: Standard test case with non-empty nums1 and nums2
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Expected output: [1,2,2,3,5,6]

    # Test case 2: nums2 is empty
    nums1 = [1]
    m = 1
    nums2 = []
    n = 0
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Expected output: [1]

    # Test case 3: nums1 is initially empty
    nums1 = [0]
    m = 0
    nums2 = [1]
    n = 1
    s.merge(nums1, m, nums2, n)
    print(nums1)  # Expected output: [1]

if __name__ == "__main__":
    main()
