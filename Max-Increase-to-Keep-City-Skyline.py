"""

### The Skyline Problem ###

In a 2 dimensional array grid, each value grid[i][j] represents the height of a building located there. We are allowed to increase the height of any number of buildings, by any amount (the amounts can be different for different buildings). Height 0 is considered to be a building as well. 

At the end, the "skyline" when viewed from all four directions of the grid, i.e. top, bottom, left, and right, must be the same as the skyline of the original grid. A city's skyline is the outer contour of the rectangles formed by all the buildings when viewed from a distance. See the following example.

What is the maximum total sum that the height of the buildings can be increased?

Example:
Input: grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
Output: 35
Explanation: 
The grid is:
[ [3, 0, 8, 4], 
  [2, 4, 5, 7],
  [9, 2, 6, 3],
  [0, 3, 1, 0] ]

The skyline viewed from top or bottom is: [9, 4, 8, 7]
The skyline viewed from left or right is: [8, 7, 9, 3]

The grid after increasing the height of buildings without affecting skylines is:

gridNew = [ [8, 4, 8, 7],
            [7, 4, 7, 7],
            [9, 4, 8, 7],
            [3, 3, 3, 3] ]

Notes:

1 < grid.length = grid[0].length <= 50.
All heights grid[i][j] are in the range [0, 100].
All buildings in grid[i][j] occupy the entire grid cell: that is, they are a 1 x 1 x grid[i][j] rectangular prism.
"""

def maxIncreaseKeepingSkyline(grid):
  
    ### Solution ###
    max_row = list(map(lambda x: max(x), grid))
    t_grid = list(zip(*grid))
    max_column = list(map(lambda x: max(x), t_grid))
    i_index = 0
    sum_list = []
    for i in grid:        
        j_index = 0
        for j in i:            
            if j < max_row[i_index] and j < max_column[j_index]:
                sum_list.append(min(max_row[i_index], max_column[j_index])-j)
            else:
                sum_list.append(0)
            j_index += 1
        i_index += 1
    result = sum(sum_list)
    return result

def main():
    grid = [[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]
    print(maxIncreaseKeepingSkyline(grid))
    
if __name__ == "__main__":
    main()
