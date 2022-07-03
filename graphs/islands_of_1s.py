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

# from sklearn import neighbors


def get_neighbours(A, pos, visitor_stack, visited):
    i, j = pos
    neighbours = []

    if j -1 in range(len(A)):
        neighbours.append((i, j-1))
    if j + 1 in range(len(A)):
        neighbours.append((i, j+1))
    if i -1 in range(len(A)):
        neighbours.append((i-1, j))
    if i + 1 in range(len(A)):
        neighbours.append((i+1, j))

    valid_neighbours = []
    found = False
    for row_i, col_i in neighbours:
        if visited[row_i][col_i] == False:
            if (row_i, col_i) not in visitor_stack:
                valid_neighbours.append((row_i, col_i))
                if A[row_i][col_i] == 1:
                    found = True
    if not found:
        valid_neighbours = []    

    return valid_neighbours
    
def count_islands(A):
    count = 0
    #can be optimized by using a 2d array of visited, visited positions can be set to 1
    #and non visited can remain 0, but for now just using append logic
    visited = [[False for i in range(len(A))] for j in range(len(A))]
    
    visitor_stack = []
    
    for row in range(len(A)):
        for col in range(len(A)):
            if visited[row][col]:
                continue
            else:
                ele = A[row][col]
                if ele == 1:
                    count += 1
                    visitor_stack.append((row, col))

            #apply dfs algo
            while(len(visitor_stack)):
                # for pos in positions:
                pos = visitor_stack.pop(0)
                visitor_stack += get_neighbours(A, pos, visitor_stack, visited)
                visited[pos[0]][pos[1]] = True

            # visited[row][col] = True


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

