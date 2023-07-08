class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        data = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in data:
                return [data[complement], i]
            else:
                data[nums[i]] = i
        return None

def main():
    s = Solution()
    print(s.twoSum([2,7,11,15], 9))  # Expected Output: [0, 1]
    print(s.twoSum([3,2,4], 6))      # Expected Output: [1, 2]
    print(s.twoSum([3,3], 6))        # Expected Output: [0, 1]
    print(s.twoSum([], 1))           # Expected Output: None
    print(s.twoSum([2,5,5,11], 10))  # Expected Output: [1, 2]
    
if __name__ == "__main__":
    main()
