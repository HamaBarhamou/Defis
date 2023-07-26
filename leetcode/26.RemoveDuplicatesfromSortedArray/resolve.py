class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 0
        for i in range(len(nums)):
            if nums[i] not in nums[0:k]:
                nums[k] = nums[i]
                k += 1
        del nums[k:]
        return k

# Testons la fonction avec quelques cas de test
def main():
    s = Solution()

    # Cas limite : tableau vide
    print(s.removeDuplicates([])) # Résultat attendu : 0

    # Cas limite : tableau contenant un seul élément
    print(s.removeDuplicates([1])) # Résultat attendu : 1

    # Cas limite : tableau contenant des doublons
    print(s.removeDuplicates([1,1,2])) # Résultat attendu : 2

    # Cas normal : tableau contenant plusieurs éléments avec des doublons
    print(s.removeDuplicates([0,0,1,1,1,2,2,3,3,4])) # Résultat attendu : 5

    # Cas limite : tableau avec le plus grand nombre d'éléments
    print(s.removeDuplicates([1] * 30000)) # Résultat attendu : 1

if __name__ == "__main__":
    main()