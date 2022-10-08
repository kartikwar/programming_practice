'''https://www.interviewbit.com/problems/path-in-matrix/'''

class Solution:
    # @param A : list of list of integers
    # @return an integer
    def checkPath(self, A):
        src=[]
        des=[]
        sz=len(A)
        for i in range (sz):
            for j in range (sz):
                if (A[i][j]==1):
                    src=[i,j]
                elif (A[i][j]==2):
                    des=[i,j]
        
        dx=[0,0,1,-1]
        dy=[1,-1,0,0]
        vis=[[False for _ in range (sz)] for _ in range (sz)]
        stack=[]
        stack.append(src)
        while (stack):
            x,y=stack.pop()
            vis[x][y]=True
            for i in range (4):
                newx,newy=x+dx[i], y+dy[i]
                if (newx<0 or newy<0 or newx>=sz or newy>=sz or vis[newx][newy] or A[newx][newy]==0):
                    continue
                if (A[newx][newy]==2):
                    return 1
                stack.append([newx,newy])
                vis[newx][newy]=True
        return 0