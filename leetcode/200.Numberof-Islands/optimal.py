class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m, n = len(grid), len(grid[0])
        
        def isValid(i, j):
            return 0 <= i < m and 0 <= j < n and grid[i][j] == "1"

        def DFS(i, j):
            if not isValid(i, j):
                return
            grid[i][j] = "-1"  # marquer comme visité
            DFS(i+1, j)
            DFS(i-1, j)
            DFS(i, j+1)
            DFS(i, j-1)
        
        nbIle = 0

        for i in range(m):
            for j in range(n):
                if isValid(i, j):
                    nbIle += 1
                    DFS(i, j)
        
        return nbIle


def main():
    sol = Solution()
    
    grid1 = [
      ["1","1","1","1","0"],
      ["1","1","0","1","0"],
      ["1","1","0","0","0"],
      ["0","0","0","0","0"]
    ]
    print(sol.numIslands(grid1))  # Output: 1

    grid2 = [
      ["1","1","0","0","0"],
      ["1","1","0","0","0"],
      ["0","0","1","0","0"],
      ["0","0","0","1","1"]
    ]
    print(sol.numIslands(grid2))  # Output: 3

    # Test case with maximum constraints
    #grid3 = [["1" for _ in range(300)] for _ in range(300)]
    #print(sol.numIslands(grid3))  # Output: 1

    # Test case with minimum constraints
    grid4 = [["0"]]
    print(sol.numIslands(grid4))  # Output: 0

if __name__ == "__main__":
    main()
