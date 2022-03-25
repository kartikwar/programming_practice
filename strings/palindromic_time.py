"""Given a string A which represents a time in 24 hour HH:MM format.
Find the minimum number of minutes need to pass to reach palindromic time.
Let some time be XY:ZW then it is palindromic if X == W and Y == Z."""

class Solution:
    # @param A : string
    # @return an integer

    def check_palindrom(self, hour, minute):
        if hour[0] == minute[-1] and hour[1] == minute[0]:
            return True


    def solve(self, A):
        start_hour, start_minute = A.split(':')[0], A.split(':')[1]        
        hour, minute = start_hour, start_minute

        difference = 0

        while not self.check_palindrom(hour, minute):
            min_ = int(minute) + 1
            
            min_ = min_ % 60
            hour_ = int(hour)

            if min_ == 0:
                # min_ = 0
                hour_ = (hour_ + 1)%24
            
            hour = str(hour_).zfill(2)
            minute = str(min_).zfill(2)

            difference += 1

        return difference        

if __name__ == '__main__':
    sol = Solution()
    print(sol.solve("23:59"))