"""
Given a boolean 2D matrix, find the number of islands. 
A group of connected 1s forms an island. 
For example, the below matrix contains 5 islands

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1} 
Output : 5

Question link :- geeksforgeeks.org/find-number-of-islands/
"""



def count_islands(A):
    count = 0
    #can be optimized by using a 2d array of visited, visited positions can be set to 1
    #and non visited can remain 0, but for now just using append logic
    visited = []
    positions = []
    
    for row in range(len(A)):
        for col in range(len(A)):
            if (row, col) in visited:
                continue
            else:
                ele = A[row][col]
                if len(positions) == 0 and ele == 1:
                    count += 1
                    positions.append((row, col))

            #apply dfs algo
            while(len(positions)!=0):
                # for pos in positions:
                pos = positions.pop(0)
                row_, col_ = pos
                neighbour_present = False
                
                valid_neighbours = []

                if col_-1 in range(len(A)):
                    neighbour = (row_, col_-1)
                    if (A[row_][col_-1] == 1) and (neighbour not in positions) and (neighbour not in visited):
                        neighbour_present = True
                    valid_neighbours.append(neighbour)

                if col_ + 1 in range(len(A)):
                    neightbour = (row_, col_ + 1)
                    if A[row_][col_+1] == 1 and (neightbour not in positions) and (neightbour not in visited):
                        neighbour_present = True
                    valid_neighbours.append(neightbour)


                if row_ + 1 in range(len(A)):
                    neighbour = (row_ + 1, col_)
                    if A[row_+1][col_] == 1 and (neighbour not in positions) and (neighbour not in visited):
                        neighbour_present = True
                    valid_neighbours.append(neighbour)

                if row_ - 1 in range(len(A)):
                    neighbour = (row_ - 1, col_)
                    if A[row_ - 1][col_] == 1 and (neighbour not in positions) and (neighbour not in visited):
                        neighbour_present = True
                    valid_neighbours.append(neighbour)

                if neighbour_present:
                    #add all the valid neighbours
                    valid_neighbours = [neighbour for neighbour in valid_neighbours if neighbour not in visited]
                    valid_neighbours = [neighbour for neighbour in valid_neighbours if neighbour not in positions]
                    positions += valid_neighbours
                
                visited.append(pos)


    return count






if __name__ == "__main__":
    A = [
        [1,1,0,0,0],
        [0,1,0,0,1],
        [1,0,0,1,1],
        [0,0,0,0,0],
        [1,0,1,0,1]
    ]


    print(count_islands(A))

