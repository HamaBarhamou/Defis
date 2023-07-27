class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        majority = nums[0]
        cpt = 1
        for i in range(1,len(nums)):
            if nums[i] == majority:
                cpt += 1
            else:
                cpt -= 1
            if cpt == 0:
                majority = nums[i]
                cpt = 1
        
        return majority


def main():
    sol = Solution()

    # Test case 1
    assert sol.majorityElement([3,2,3]) == 3

    # Test case 2
    assert sol.majorityElement([2,2,1,1,1,2,2]) == 2

    # Test case 3: list with negative numbers
    assert sol.majorityElement([-1,-1,0]) == -1

    # Test case 4: list with one number
    assert sol.majorityElement([3]) == 3

    # Test case 5: majority element appears exactly n/2 times
    assert sol.majorityElement([2,2,1,1]) == 1 or sol.majorityElement([2,2,1,1]) == 2

    print("All test cases pass")

if __name__ == "__main__":
    main()
