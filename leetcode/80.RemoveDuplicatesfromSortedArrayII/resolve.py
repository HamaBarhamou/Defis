class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 2: return 2
        p1 = 0
        p2 = 1
        k = 2
        for i in range(2,len(nums)):
            if nums[p1] == nums[p2]:
                if nums[i] != nums[p2]:
                    nums[k] = nums[i]
                    k += 1
                    p1 += 1
                    p2 += 1
            else:
                nums[k] = nums[i]
                k += 1
                p1 += 1
                p2 += 1
                  
        return k

def main():
    solution = Solution()

    # Cas limite où la liste est vide
    nums = []
    print(solution.removeDuplicates(nums))  # Attendu : 0

    # Cas limite où la liste contient un seul élément
    nums = [1]
    print(solution.removeDuplicates(nums))  # Attendu : 1

    # Cas limite où la liste contient deux éléments identiques
    nums = [2, 2]
    print(solution.removeDuplicates(nums))  # Attendu : 2

    # Cas limite où la liste contient deux éléments différents
    nums = [2, 3]
    print(solution.removeDuplicates(nums))  # Attendu : 2

    # Cas limite où tous les éléments sont identiques
    nums = [2, 2, 2, 2, 2]
    print(solution.removeDuplicates(nums))  # Attendu : 2

    # Cas de test normaux
    nums = [1, 1, 1, 2, 2, 3]
    print(solution.removeDuplicates(nums))  # Attendu : 5

    nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
    print(solution.removeDuplicates(nums))  # Attendu : 7

if __name__ == "__main__":
    main()
