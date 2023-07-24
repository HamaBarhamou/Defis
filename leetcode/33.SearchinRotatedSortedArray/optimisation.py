class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        def findPivot(nums):
            if len(nums) == 1 or nums[0] < nums[-1]:
                return None
            gauche = 0
            droite = len(nums)-1
            while gauche <= droite:
                mid = gauche + (droite - gauche) // 2
                if nums[mid] > nums[mid + 1]:
                    return mid + 1
                else:
                    if nums[mid] < nums[gauche]:
                        droite = mid - 1
                    else:
                        gauche = mid + 1
            return gauche

        def binarySearch(nums, gauche, droite, target):
            while gauche <= droite:
                mid = gauche + (droite - gauche) // 2
                if nums[mid] == target:
                    return mid
                elif nums[mid] > target:
                    droite = mid - 1
                else:
                    gauche = mid + 1
            return -1

        i_pivot = findPivot(nums)

        if i_pivot is None:
            return binarySearch(nums, 0, len(nums) - 1, target)

        if nums[i_pivot] == target:
            return i_pivot
        elif nums[0] <= target:
            return binarySearch(nums, 0, i_pivot, target)
        return binarySearch(nums, i_pivot, len(nums) - 1, target)


def main():
    sol = Solution()

    # Test de cas simples
    print(sol.search([4,5,6,7,0,1,2], 0)) # Devrait retourner 4
    print(sol.search([4,5,6,7,0,1,2], 3)) # Devrait retourner -1

    # Test avec des tableaux déjà triés
    print(sol.search([1,2,3,4,5,6], 1))   # Devrait retourner 0
    print(sol.search([1,2,3,4,5,6], 7))   # Devrait retourner -1

    # Test avec des tableaux de taille 1
    print(sol.search([1], 0))              # Devrait retourner -1
    print(sol.search([1], 1))              # Devrait retourner 0

    # Test avec des tableaux de taille 2
    print(sol.search([1,3], 0))            # Devrait retourner -1
    print(sol.search([1,3], 1))            # Devrait retourner 0
    print(sol.search([3,1], 0))            # Devrait retourner -1
    print(sol.search([3,1], 1))            # Devrait retourner 1

    # Test avec des tableaux de taille 3
    print(sol.search([1,2,3], 0))          # Devrait retourner -1
    print(sol.search([1,2,3], 1))          # Devrait retourner 0
    print(sol.search([2,3,1], 0))          # Devrait retourner -1
    print(sol.search([2,3,1], 1))          # Devrait retourner 2
    print(sol.search([3,1,2], 0))          # Devrait retourner -1
    print(sol.search([3,1,2], 1))          # Devrait retourner 1

if __name__ == "__main__":
    main()
