"""
Given a maze, find if a path exists from start to finish
At each intersection, you have to decide between three or fewer choices:
* Go straight
* Go left
* Go right

This is just a pseudo code and should be used as a template 
in backtracking algorithms
"""

def options_from_point(p):
    options = ['left', 'right', 'straight']
    return 

def pathfound(p):
        found = False
        for option in options_from_point(p):
            if pathfound(option):
                found = True
                return found
        return found


if __name__ == '__main__':
    p = 'starting point'
    pathfound(p)