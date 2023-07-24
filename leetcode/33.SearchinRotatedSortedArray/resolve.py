class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        if len(nums) <= 3:
            for i in range(len(nums)):
                if nums[i] == target: return i
            return -1

        i_pivot = None
        gauche = 0
        droite = len(nums) - 1

        def findPivot(nums):
            gauche = 0
            droite = len(nums)-1
            while gauche < droite:
                i = (gauche + droite) // 2
                if nums[i] > nums[droite]:
                    gauche = i+1
                else:
                    droite = i
            return gauche
        
        i_pivot = findPivot(nums)
        if nums[0] < nums[-1]:
            i_pivot = None
      
        if i_pivot is None:
            gauche = 0
            droite = len(nums) - 1
        elif nums[0] <= target <= nums[i_pivot-1]:
            gauche = 0
            droite = i_pivot-1
        else:
            gauche = i_pivot
            droite = len(nums)-1 

        #print('pivo={} tab={}'.format(i_pivot, nums[gauche:droite+1]))
        # Recherche de target
        while gauche <= droite:
            i = (gauche + droite) // 2
            if nums[i] == target:
                return i
            elif target < nums[i]:
                droite = i-1
            else:
                gauche = i+1
        
        return -1
        
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
