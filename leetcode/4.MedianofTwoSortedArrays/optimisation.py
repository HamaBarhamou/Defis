class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        x, y = len(nums1), len(nums2)

        # Ensure nums1 is always the smaller list.
        if x > y:
            nums1, nums2, x, y = nums2, nums1, y, x

        debut = 0
        fin = x

        while debut <= fin:
            partitionX = (debut + fin) // 2
            partitionY = (x + y + 1) // 2 - partitionX

            maxLeftX = float('-inf') if partitionX == 0 else nums1[partitionX - 1]
            minRightX = float('inf') if partitionX == x else nums1[partitionX]

            maxLeftY = float('-inf') if partitionY == 0 else nums2[partitionY - 1]
            minRightY = float('inf') if partitionY == y else nums2[partitionY]

            if maxLeftX <= minRightY and maxLeftY <= minRightX:
                if (x + y) % 2 == 0:
                    return max(maxLeftX, maxLeftY) + (min(minRightX, minRightY) - max(maxLeftX, maxLeftY)) / 2
                else:
                    return max(maxLeftX, maxLeftY)
            elif maxLeftX > minRightY:
                fin = partitionX - 1
            else:
                debut = partitionX + 1

if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([], [2, 3]) == 2.5
    print("All tests passed!")
