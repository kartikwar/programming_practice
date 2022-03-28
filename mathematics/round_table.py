'''
There is a party at Ram's house, he will be inviting A friends to his party.
There is round table at his house which has A+1 seats.
Among all those friends Shyam is Ram's best friend and Ram wants to sit with him.
Find the number of ways to sit such that Ram and Shayam will sit together.
Since this number can be very large take modulo 109 + 7.
'''

class Solution:
    # @param A : integer
    # @return an integer
    def solve(self, A):
        self.mod = (10**9) + 7
        return (2 * (self.get_fact(A))) % self.mod

    def get_fact(self, num):
        ans = 1
        for i in range(1, num+1):
            ans = (ans * i) % self.mod
        
        return ans % self.mod