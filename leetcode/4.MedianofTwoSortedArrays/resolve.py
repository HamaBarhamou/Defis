class Solution(object):
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        m = len(nums1)
        n =  len(nums2)
        if m > n:
           save = nums1
           nums1 = nums2
           nums2 = save
           save = m
           m = n
           n = save

        if m == 0:
            if n % 2 == 0:
                return((nums2[n//2 -1]+nums2[n//2]) / 2.0)
            else:
                return float(nums2[n//2])

        debut = 0
        fin = m

        while debut <= fin:
            i = (debut + fin) // 2
            j = (m + n + 1) // 2 - i

            maxAGauche1 = nums1[i-1] if i > 0 else float('-inf')
            minADroite1 = nums1[i] if i < m else float('inf')
            maxAGauche2 = nums2[j-1] if j > 0 else float('-inf')
            minADroite2 = nums2[j] if j < n else float('inf')

            if maxAGauche1 <= minADroite2 and maxAGauche2 <= minADroite1:
                if (m + n) % 2 == 0:
                    return (((max(maxAGauche1, maxAGauche2)) + min(minADroite1, minADroite2)) / 2.0)
                else:
                    return (max(maxAGauche1, maxAGauche2))
            elif maxAGauche1 > minADroite2:
                fin -= 1 #i - 1
            else:
                debut += 1 #i + 1

if __name__ == '__main__':
    s = Solution()
    assert s.findMedianSortedArrays([1, 3], [2]) == 2.0
    assert s.findMedianSortedArrays([1, 2], [3, 4]) == 2.5
    assert s.findMedianSortedArrays([0, 0], [0, 0]) == 0.0
    assert s.findMedianSortedArrays([], [1]) == 1.0
    assert s.findMedianSortedArrays([], [2, 3]) == 2.5
    print("All tests passed!")