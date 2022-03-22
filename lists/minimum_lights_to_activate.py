'''
There is a corridor in a Jail which is N units long. Given an array A of size N. 
The ith index of this array is 0 if the light at ith position is 
faulty otherwise it is 1.

All the lights are of specific power B which if is placed at position X, 
it can light the corridor from [ X-B+1, X+B-1].

Initially all lights are off.

Return the minimum number of lights to be turned ON to light the 
whole corridor or -1 if the whole corridor cannot be lighted.
'''


class Solution:
    # @param A : list of integers
    # @param B : integer
    # @return an integer
    def solve(self, A, B):
        if len(A) < 1:
            return -1
        else:
            count = 0
            start_index = 0
            bulb_index = 0
            right_index = 0

            end_index = len(A) - 1

            range_covered = B - 1

            while right_index <= len(A) - 1 and start_index <= len(A) - 1:

                bulb_found = False

                curr_range = range(min((start_index + range_covered), end_index), max(start_index - 1 , -1) , -1)

                #right pass
                for bulb_ind in curr_range:
                    if A[bulb_ind] == 1:
                        bulb_found = True
                        count += 1
                        right_index = bulb_ind + range_covered
                        start_index = right_index + 1
                        break


                #left pass
                if not bulb_found:
                    curr_range = range(start_index, start_index - range_covered, -1)
                    for bulb_ind in curr_range:
                        if A[bulb_ind] == 1:
                            bulb_found = True
                            count += 1
                            right_index = bulb_ind + range_covered
                            start_index = right_index + 1
                            break


                if not bulb_found:
                    count = -1
                    break 

            return count


if __name__ == '__main__':
    sol = Solution()
    A = [ 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0 ]
    B = 6
    print(sol.solve(A, B))
