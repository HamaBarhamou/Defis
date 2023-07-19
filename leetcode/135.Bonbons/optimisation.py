class Solution(object):
    def candy(self, ratings):
        """
        :type ratings: List[int]
        :rtype: int
        """
        bonbon = [1]*len(ratings)

        for i in range(1, len(ratings)):
            if ratings[i] > ratings[i - 1]:
                bonbon[i] = bonbon[i - 1] + 1

        for i in range(len(ratings) - 2, -1, -1):
            if ratings[i] > ratings[i + 1]:
                bonbon[i] = max(bonbon[i], bonbon[i + 1] + 1)

        return sum(bonbon)


def main():
    solution = Solution()
    # Test 1: cas normal
    print(solution.candy([1, 0, 2]))  # Doit afficher 5
    # Test 2: cas normal avec égalités
    print(solution.candy([1, 2, 2]))  # Doit afficher 4
    # Test 3: cas avec une seule note
    print(solution.candy([1]))  # Doit afficher 1
    # Test 4: cas avec toutes les notes identiques
    print(solution.candy([1, 1, 1]))  # Doit afficher 3
    # Test 5: cas avec notes décroissantes
    print(solution.candy([3, 2, 1]))  # Doit afficher 6
    # Test 6: cas avec notes croissantes
    print(solution.candy([1, 2, 3]))  # Doit afficher 6

if __name__ == "__main__":
    main()
