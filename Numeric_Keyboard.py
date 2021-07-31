class Solution:
    def num(self,x,N):
        if N==1:
            return 1
        l=[0]*10
        for i in range(10):
            l[i]=[0]*N
            l[i][0]=1
        for j in range(1,N):
            for i in range(10):
                if i==0:
                    l[0][j]=l[0][j-1]+l[8][j-1]
                elif i==1:
                    l[i][j]=l[i][j-1]+l[2][j-1]+l[4][j-1]
                elif i==2:
                    l[i][j]=l[i][j-1]+l[1][j-1]+l[3][j-1]+l[5][j-1]
                elif i==3:
                    l[i][j]=l[i][j-1]+l[2][j-1]+l[6][j-1]
                elif i==4:
                    l[i][j]=l[i][j-1]+l[1][j-1]+l[5][j-1]+l[7][j-1]
                elif i==5:
                    l[i][j]=l[i][j-1]+l[2][j-1]+l[4][j-1]+l[6][j-1]+l[8][j-1]
                elif i==6:
                    l[i][j]=l[i][j-1]+l[3][j-1]+l[5][j-1]+l[9][j-1]
                elif i==7:
                    l[i][j]=l[i][j-1]+l[8][j-1]+l[4][j-1]
                elif i==8:
                    l[i][j]=l[i][j-1]+l[5][j-1]+l[7][j-1]+l[9][j-1]+l[0][j-1]
                elif i==9:
                    l[i][j]=l[i][j-1]+l[6][j-1]+l[8][j-1]
        return l[x][N-1]
                
                    
                    
        
        
        
	def getCount(self, N):
	    ct=0
	    for i in range(10):
	        ct+=self.num(i,N)
	    return ct