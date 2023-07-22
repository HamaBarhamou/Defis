class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if target < matrix[0][0] or target > matrix[len(matrix)-1][len(matrix[0])-1]:
            return False

        # Recherche binaire sur les lignes
        gauche = 0
        droite = len(matrix) - 1
        i = (gauche + droite) // 2
        while gauche <= droite:
            if matrix[i][0] == target:
                return True
            elif target < matrix[i][0]:
                droite = i - 1
            else:
                gauche = i + 1
            i = (gauche + droite) // 2 

        ligne = matrix[droite]

        # Recherche binaire sur les colonnes
        gauche = 0
        droite = len(ligne) - 1
        i = (gauche + droite) // 2
        while gauche <= droite:
            if ligne[i] == target:
                return True
            elif target < ligne[i]:
                droite = i - 1
            else:
                gauche = i + 1 
            i = (gauche + droite) // 2 

        return False
    
def main():
    solution = Solution()
    
    # Test case 1
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 3
    print(solution.searchMatrix(matrix, target)) # Expected output: True
    
    # Test case 2
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(solution.searchMatrix(matrix, target)) # Expected output: False
    
    # Test case 3: testing lower boundary
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 1
    print(solution.searchMatrix(matrix, target)) # Expected output: True
    
    # Test case 4: testing upper boundary
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 60
    print(solution.searchMatrix(matrix, target)) # Expected output: True

    # Test case 5: testing value not in matrix
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 100
    print(solution.searchMatrix(matrix, target)) # Expected output: False

if __name__ == "__main__":
    main()
