class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """
        if not matrix or target < matrix[0][0] or target > matrix[-1][-1]:
            return False
        
        n, m = len(matrix), len(matrix[0])
        gauche, droite = 0, m * n - 1
        
        while gauche <= droite:
            mid = (gauche + droite) // 2
            mid_val = matrix[mid // m][mid % m]
            
            if mid_val == target:
                return True
            elif mid_val < target:
                gauche = mid + 1
            else:
                droite = mid - 1
                
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
