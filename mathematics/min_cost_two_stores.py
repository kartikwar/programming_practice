'''
You want to buy A candies, there are two candy stores in your town.
The stores sell candies in packets, first store sells B candies 
for C rupees and the other store sells D candies for E rupees.
Find minimum cost to buy exactly A candies if you can buy any 
amout of packets from both the stores.
If it is not possible to do so return -1.
'''

class Solution:
    # @param A : integer
    # @param B : integer
    # @param C : integer
    # @param D : integer
    # @param E : integer
    # @return an integer
    def solve(self, A, B, C, D, E):
        solutions = []
        n = 0
        m = 0
        min_cost = -1
        while A - n*D > -1:
            if (A - n*D) % B == 0:
                m = (A -n*D)//B
                solutions.append((m,n))
            n = n + 1
        
        if len(solutions) ==0:
            return -1
        else:
            for sol in solutions:
                cost = C*sol[0] + E*sol[1]
                if min_cost > 0:
                    if cost < min_cost:
                        min_cost = cost
                    # else:
                else:
                    min_cost = cost
            return min_cost


if __name__ == '__main__':
    # A = 7
    A = 7
    B = 1
    C = 1
    D = 3
    E = 2

    sol = Solution()
    print(sol.solve(A, B, C, D, E))
