class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        def DFS(i, j):
            grid[i][j] = "-1" #marquer comme visité
            
            if i < m-1 and grid[i+1][j] == "1":
                DFS(i+1, j)
            if i > 0 and grid[i-1][j] == "1":
                DFS(i-1, j)
            if j < n-1 and grid[i][j+1] == "1":
                DFS(i, j+1)
            if j > 0 and grid[i][j-1] == "1":
                DFS(i, j-1)
        
        nbIle = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == "1":
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
