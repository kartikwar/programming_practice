'''
Given a string A containing only lowercase characters.
Find the frequencies of the characters in order of their occurrence.

Example Input
Input 1:
A = "interviewbit"
Input 2:

A = "scaler"


Example Output
Output 1:
[3, 1, 2, 2, 1, 1, 1, 1]
Output 2:

[1, 1, 1, 1, 1, 1]

'''

class Solution:
    # @param A : string
    # @return a list of integers
    def solve(self, A):
        frequencies = {}
        result = []
        for ind, a in enumerate(A):
            if a in frequencies:
                result[frequencies[a][1]] += 1
                frequencies[a][0] +=1
            else:
                result.append(1)
                frequencies[a] = [1, len(result) -1]
        # print(result)
        return result

if __name__ == '__main__':
    sol = Solution()
    sol.solve(A='tmghjemxxb')